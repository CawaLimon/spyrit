import pyb
import xmltok

REGISTER_SETTINGS_FILE = "Register_Setting.xml"
XTAL_FREQ = 26000000 #Hz

state_dict = {0x40:'STANDBY',
              0x36:'SLEEP',
              0x03:'READY',
              0x0F:'LOCK',
              0x33:'RX',
              0x5F:'TX',
              0x13:'LOCKWON'}

class SPIRIT1:
    def __init__(self, pos):
        if pos == 1:
            self.SDN = pyb.Pin('X12', pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
            self.SDN.low()
        elif pos == 2:
            self.SDN = pyb.Pin('Y12', pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
            self.SDN.low()
        self._init_spi(pos)
        self._init_gpio(pos)
        self._init_led(pos)
        regTable = xmltok.tokenize(open(REGISTER_SETTINGS_FILE))
        for _ in regTable:
            try:
                address = int(xmltok.text_of(regTable, 'Address'))
                value = int(xmltok.text_of(regTable, 'Value'))
            except StopIteration:
                break
            self.writeRegisters(address, bytearray([value]))
        
        ##clock init
        
            
####SPI FUNCTIONS
    def _init_spi(self, pos):
        if pos == 1:
            self.bus = pyb.SPI(1, pyb.SPI.MASTER, polarity=0)
            self.CSn = pyb.Pin("X5", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_UP)
        elif pos == 2:
            self.bus = pyb.SPI(2, pyb.SPI.MASTER, polarity=0)
            self.CSn = pyb.Pin("Y5", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_UP)
        self.CSn.high()
        
    def _init_gpio(self, pos):
        if pos == 1:
            self.gpio0 = pyb.Pin("X4", pyb.Pin.IN)
            self.gpio1 = pyb.Pin("X3", pyb.Pin.IN)
            self.gpio2 = pyb.Pin("X2", pyb.Pin.IN)
            self.gpio3 = pyb.Pin("X1", pyb.Pin.IN)
        elif pos == 2:
            self.gpio0 = pyb.Pin("Y4", pyb.Pin.IN)
            self.gpio1 = pyb.Pin("Y3", pyb.Pin.IN)
            self.gpio2 = pyb.Pin("Y2", pyb.Pin.IN)
            self.gpio3 = pyb.Pin("Y1", pyb.Pin.IN)
            
    def _init_led(self, pos):
        if pos == 1:
            self.led1 = pyb.Pin("X9", pyb.Pin.OUT_PP)
            self.led2 = pyb.Pin("X10", pyb.Pin.OUT_PP)
            self.led3 = pyb.Pin("X11", pyb.Pin.OUT_PP)
        if pos == 2:
            self.led1 = pyb.Pin("Y9", pyb.Pin.OUT_PP)
            self.led2 = pyb.Pin("Y10", pyb.Pin.OUT_PP)
            self.led3 = pyb.Pin("Y11", pyb.Pin.OUT_PP)
        self.led1.low()
        self.led2.low()
        self.led3.low()
            
    def _send_receive(self, buff):
#         print(buff)
        irq = pyb.disable_irq()
        self.CSn.low()
        self.bus.send_recv(buff, buff)
        self.CSn.high()
        pyb.enable_irq(irq)
        self._parse_status(buff[:2])
#         print(buff)
        return buff
    
    def writeRegisters(self, regAddress, buff):
        return list(self._send_receive(bytearray([0x00, regAddress]) + buff))
        
    def readRegisters(self, regAddress, numBytes=1):
        return list(self._send_receive(bytearray([0x01, regAddress]) + bytearray(numBytes)))
    
    def sendCommand(self, commandCode):
        self._send_receive(bytearray([0x80, commandCode]))
        
    def writeLinearFifo(self, buff):
        self._send_receive(bytearray([0x00, 0xFF]) + buff)
        
    def readLinearFifo(self, numBytes=1):
        return self._send_receive(bytearray([0x01, 0xFF]) + bytearray(numBytes))

####STATUS FUNCITONS
    def _parse_status(self, statusBuff):
        self.XO_On = statusBuff[1] & 0x01
        self.state = statusBuff[1] >> 1
#         print(self.state)
        self.state = state_dict.get(statusBuff[1] >> 1, "INVALID")
        self.errorLock = statusBuff[0]  & 0x01
        self.rxFifoEmpty = statusBuff[0] & 0x02
        self.txFifoFull = statusBuff[0] & 0x04
        self.antSelect = statusBuff[0] & 0x08
        
    def refreshStatus(self):
        statusBuff = self.spi.readRegisters(0xC0, 2)
        self._parseStatus(statusBuff)
    
    def waitForState(self, state):
        while True:
            if self.state == state:
                return True
            self.refreshStatus()
            
####AES FUNCITONS
    def writeAESin(self, buff):
        self.writeRegisters(0x80, buff)
        
    def startAESkeydec(self):
        self.sendCommand(0x6D)
        
    def startAESenc(self):
        self.sendCommand(0x6A)
        
    def startAESkey(self):
        self.sendCommand(0x6B)
        
    def startAESdec(self):
        self.sendCommand(0x6C)
        
    def writeAESkeyin(self, key):
        self.writeRegisters(0x70, key)
        
    def readAESout(self):
        return self.readRegisters(0xD4, 16)
    
####FIFO FUNCTIONS
    def rxFIFObytes(self):
        return self.readRegisters(0xE7)[0]
    
    def txFIFObytes(self):
        return self.readRegisters(0xE6)[0]
    
    def readFIFO(self, size):
        return self.readRegisters(0xFF, size)
    
    def writeFIFO(self, buff):
        self.writeRegisters(0xFF, buff)
        
####LDCR CONFIG
    def enableLDCR(self, en):
        if en == True:
            buff = self.readRegisters(0x50)
            buff[0] = buff[0] | 0x01
            self.writeRegisters(0x50, buff)
        elif en == False:
            buff = self.readRegisters(0x50)
            buff[0] = buff[0] & 0xFE
            self.writeRegisters(0x50, buff)
    
#     def setRXTimeout(self, desiredMsec):#in ms
#         if desiredMsec > 3026.0:
#             a0 = 0xFF
#             b0 = 0xFF
#         
#         else:
#             error_min, n =  desiredMsec * 1000/XTAL_FREQ
#             
#             rxPrescalerVal, a0 = ((n-1)/0xFF)+1
#             rxCounterVal, b0 = (n / rxPrescalerVal)
#             
#             for _ in range(rxPrescalerVal):
#                 rxCounterVal = n / rxPrescalerVal
#                 err = 1+int(rxPrescalerVal+1)*int(rxCounterVal) - n
#                 if abs(err) > abs(error_min):
#                     error_min = err
#                     a0 = rxPrescalerVal
#                     b0 = rxCounterVal
#                     if err == 0:
#                         break
#                 if rxPrescalerVal == 0xFF:
#                     break
#             
#         buff = bytearray([a0, b0])
#         self.writeRegisters(0x53, buff)
#         
#     def setWakeupTimeout(self, desiredMsec):
#         if 
            
####CONFIG
    def configureGPIO(self, selections):
        self.writeRegisters(0x02, bytearray(selections))
    
    def configureIRQ(self, irqMask):
        self.writeRegisters(0x90, bytearray(irqMask))

####PUBLIC FUNCTIONS
    def addPacket(self, data):
        self.writeLinearFifo(data)
         
    def recvPacket(self):
        return []
    
    def readInterrupt(self):
        intVal = self.readRegisters(0xFA, 4)
        return intVal
        