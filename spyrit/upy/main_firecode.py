import pyb
import spirit1
import debug
import os

def tenmsTasks():
    global tenms
    global tenmsFlag
    if tenms < 9:
        tenms += 1
    else:
        tenms = 0
        hmsTasks()
        
        
def hmsTasks():
    global hms
    if hms < 9:
        hms += 1
    else:
        hms = 0
        secTasks()
        
def secTasks():
    global seconds
    global spirit
    
    global mins
    print('Time Active: {}:{}'.format(mins, seconds))
    
    print('SPIRIT1 State: {}'.format(spirit.state))
    
    numBytes = spirit.rxFIFObytes()
    print('RX Queue Size: {} bytes'.format(numBytes))
    
    data = spirit.readRegisters(0xFF, numBytes)
    print('Data: {}'.format(data))
    print('\n')
    
    if seconds < 59:
        seconds += 1
    else:
        seconds = 0
        minTasks()
        
def minTasks():
    global mins
    
    if mins < 59:
        mins += 1
    else:
        mins = 0

def tenmsInt():
    global tenmsFlag
    tenmsFlag = True
    
def irqSet():
    global irqFlag
    print('interrupt')
    irqFlag = True
        
def setReset():
    global spirit
    spirit.led1.high()
    spirit.led2.high()
    spirit.led3.high()
    
def resetReset():
    global spirit
    spirit.led1.low()
    spirit.led2.low()
    spirit.led3.low()
    
## constants
AES_KEY = os.urandom(16) #128 bit AES key
RESET_CODE = "fireCODE"
RESET_TIME = 3000 #ms
    
## main
state = 'INIT'
debug.log('Mode = ' + state)

print("Initialize Firecode")

intCount = 0 #counter

rtc = pyb.RTC()
now = rtc.datetime()
then = now

tenmsFlag = False
tenms = 0
hms = 0
seconds = 1
mins = 0

rxFifoSize = 0

irqFlag = False

spirit = spirit1.SPIRIT1(1)
spirit.writeAESkeyin(AES_KEY)
spirit.configureGPIO([0xA2, 0x02, 0xA2, 0x0A])
# spirit.gpio2.mode(pyb.Pin.OUT)
#spirit.gpio2.irq(trigger=pyb.Pin.IRQ_FALLING, handler=irqSet)
irqPin = pyb.ExtInt(spirit.gpio2, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, irqSet)
spirit.configureIRQ([0x40, 0x00, 0x00, 0x01])
# 
# spirit.enableLDCR(True)
# spirit.writeRegisters(0x53, bytearray([0xFF, 0xFF]))
# spirit.writeRegisters(0x55, bytearray([0xFF, 0xFF]))

tim7 = pyb.Timer(7, freq=100)
tim7.callback(lambda t: tenmsInt())

# spirit.sendCommand(0x61)

# resetPin = pyb.Pin()

# taskScheduler = scheduler.Scheduler(100, 1)
# 
# task_OneSecond = [tasks.TestTask, 100, 0]
# taskScheduler.AddTask(task_OneSecond)


# while taskScheduler.StateGet() == False:
while True:
    
#     taskScheduler.Run()
#     pyb.wfi()
    #print(spirit.rxFIFObytes())
    
    if irqFlag:
        inqBits = spirit.readInterrupt()
        print(inqBits)
        if inqBits[3] & 0x01: #RX data ready
            print('Rx Data Ready')
            numBytes = spirit.rxFIFObytes()
            print(numBytes)
            payload = spirit.readFIFO(numBytes)
            print(payload)
            spirit.writeAESin(payload)
            spirit.startAESkeydec()
            
        if (inqBits[0] >> 7) & 0x01: #AES end of op
            print('AES end of op')
            output = spirit.readAESout()
            #cast output into string
            if output == RESET_CODE:
#                 resetPin.high()
                setReset()
                pyb.delay(RESET_TIME)
                resetReset()
#                 resetPin.low()
                intCount += 1
            
            else:
                print('invalid code')
    
    if tenmsFlag:
        tenmsTasks()
        tenmsFlag = False
        
#         rxData = spirit.readall() #check the RX queue for data receieved
#         if rxData != None and len(rxData) > 0:
#             print rxData
        