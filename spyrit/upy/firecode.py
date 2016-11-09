'''Imports'''

import spirit1, os, pyb

#TODO
#Configure signal receiver quality indicators (SQI, PQI, CS)
#

#Globals
IRQ_STATUS = False

#Config
RSSI_VALUE = 22#dBm
AES_KEY = os.urandom(16) #128 bit AES key
RESET_TIME = 3000 #ms
GPIO_BITS = 0b01100111
IRQ_BITS = 0b00000000000000000000000000000000

#Constants
IRQ_BIT_RSSI = 14
IRQ_BIT_RX_READY = 0
IRQ_BIT_AES_DONE = 30

def testBit(int_type, offset):
    mask = 1 << offset
    return (int_type | mask)

def irqReceived(pin):
    IRQ_STATUS = True
    print(pin)
    
def tasks10ms():
    pass

def tasks50ms():
    pass

def tasks1s():
    pass

class FirecodeFSM:
    IDLE = 0
    LISTEN = 1
    HANDLE = 2
    RESET = 3
    def __init__(self, spirit):
        self.state = self.IDLE
        self.spirit = spirit
        
        self.spirit.configureGPIO(GPIO_BITS)
        self.spirit.configureIRQ(IRQ_BITS)
        
    def event_loop(self):
        while True:
            if IRQ_STATUS:
                intBits = self.spirit.readInterrupt()
                if self.state == self.IDLE:
                    if testBit(intBits, IRQ_BIT_RSSI):
                        self.state = self.LISTEN
                        
                elif self.state == self.LISTEN:
                    if testBit(intBits, IRQ_BIT_RX_READY):
                        self.state = self.HANDLE
                        
                elif self.state == self.HANDLE:
                    if testBit(intBits, IRQ_BIT_AES_DONE):
                        self.state = self.RESET
                
                IRQ_STATUS = False
            
            
            pyb.delay(10)

def main():
    spirit = spirit1.SPIRIT1(1)
    spirit.sendCommand()
    
if __name__ == '__name__':
    main()