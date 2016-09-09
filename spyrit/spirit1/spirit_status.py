import spirit_regs
import time

STATE_STANDBY = 0x40
STATE_SLEEP = 0x36
STATE_READY = 0x03
STATE_PM_SETUP = 0x3D
STATE_XO_SETTLING = 0x23
STATE_SYNTH_SETUP = 0x53
STATE_PROTOCOL = 0x1F
STATE_SYNTH_CALIBRATION = 0x4F
STATE_LOCK = 0x0F
STATE_RX = 0x33
STATE_TX = 0x5F

class Status:
    def __init__(self, spi):
        self.spi = spi
        self.refreshStatus()
    
    def refreshStatus(self):
        statusBuff = self.spi.readRegisters(spirit_regs.MC_STATE1_BASE, 2)
        self.parseStatus(statusBuff)
        
    def parseStatus(self, statusBuff):
        self.XO_On = statusBuff[1] & 0x01
        self.state = statusBuff[1] >> 1
        self.errorLock = statusBuff[0]  & 0x01
        self.rxFifoEmpty = statusBuff[0] & 0x02
        self.txFifoFull = statusBuff[0] & 0x04
        self.antSelect = statusBuff[0] & 0x08
        
    def getXO(self):
        return self.XO_On
    
    def getState(self):
        return self.state
    
    def getErrorLock(self):
        return self.errorLock
    
    def getRxFifoEmpty(self):
        return self.rxFifoEmpty
    
    def getTxFifoFull(self):
        return self.txFifoFull
    
    def getAntSelect(self):
        return self.antSelect
        
    def waitForState(self, state, wTime=1):
        timeLeft = wTime
        sTime = time.time()
        while timeLeft >= 0:
            timeLeft = timeLeft + sTime - time.time()
            self.refreshStatus()
            if self.state == state:
                return True
        return False