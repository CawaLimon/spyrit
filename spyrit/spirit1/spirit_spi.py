import serial

WRITE_BYTE = 0x00
READ_BYTE = 0x01
COMMAND_BYTE = 0x80
FIFO_BYTE = 0xFF

DEFAULT_TIMEOUT = 1

class SPI:
    """SPI connector object.
    Provides a way for the parent class to have access to
    all SPI communications.
    """
    def __init__(self, port=None, callbackFunc=None):
        
        self.notifyFunc = callbackFunc
        if port:
            self.open(port)
        
    def open(self, port):
        self.ser = serial.Serial(port, 9600, timeout=DEFAULT_TIMEOUT)
        
    def close(self):
        self.ser.close()
        
    def _send_receive(self, buff):
        print buff
        self.ser.flushOutput()
        self.ser.write(buff)
        buff = bytearray(self.ser.readline())
        print buff
        return buff
    
    def setCallback(self, callbackFunc):
        self.notifyFunc = callbackFunc
    
    def writeRegisters(self, regAddress, buff):
        self._send_receive(bytearray([0x00, regAddress]) + buff)
        
    def readRegisters(self, regAddress, numBytes=1):
        buff = self._send_receive(bytearray([0x01, regAddress]) + bytearray(numBytes))
        return buff
    
    def sendCommand(self, commandCode):
        self._send_receive(bytearray([0x80, commandCode]))
        
    def writeLinearFifo(self, buff):
        self._send_receive(bytearray([0x00, 0xFF]) + buff)
        
    def readLinearFifo(self, numBytes=1):
        return self._send_receive(bytearray([0x01, 0xFF]) + bytearray(numBytes))