import pyb
import xmltok

REGISTER_SETTINGS_FILE = "Register_Setting.xml"

class SPIRIT1:
    def __init__(self, pos):
        if pos == 1:
            self.SDN = pyb.Pin('X9', pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
            self.SDN.low()
        elif pos == 2:
            self.SDN = pyb.Pin('Y9', pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_DOWN)
            self.SDN.low()
        self._init_spi(pos)
        regTable = xmltok.tokenize(open(REGISTER_SETTINGS_FILE))
        for _ in regTable:
            try:
                address = int(xmltok.text_of(regTable, 'Address'))
                value = int(xmltok.text_of(regTable, 'Value'))
            except StopIteration:
                break
            self.writeRegisters(address, bytearray([value]))
            
####SPI FUNCTIONS
    def _init_spi(self, pos):
        if pos == 1:
            self.bus = pyb.SPI(1, pyb.SPI.MASTER, polarity=0)
            self.CSn = pyb.Pin("X5", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_UP)
        elif pos == 2:
            self.bus = pyb.SPI(2, pyb.SPI.MASTER, polarity=0)
            self.CSn = pyb.Pin("Y5", pyb.Pin.OUT_PP, pull=pyb.Pin.PULL_UP)
        self.CSn.high()
        
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

####OTHER FUNCITONS
    def _parse_status(self, statusBuff):
        self.XO_On = statusBuff[1] & 0x01
        self.state = statusBuff[1] >> 1
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

####INTERFACE FUNCTIONS
#     def addPacket(self, data):
#         self.writeLinearFifo(data)
#         
#     def recvPacket: