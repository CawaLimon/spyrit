CUT_MAX_NO = 3
CUT_2_1v3 = 0x0103
CUT_2_1v4 = 0x0104
CUT_3_0 = 0x0130

RANGE_EXT_NONE,\
RANGE_EXT_SKYWORKS = range(2)

COMMUNICATION_STATE_TX,\
COMMUNICATION_STATE_RX = range(2)

from spirit_radio import B_HALF_FACTOR
from spirit_radio import BAND_REG_VALUE

N_SAMPLES = 20
SETTLING_PERIODS = 4
A = 0.4

class Management:
    
    def __init__(self,
                 spi,
                 gpio,
                 spiritVersion=None,
                 rangeExtType=None,
                 xtalFrequency=None,
                 bandSelect=None):
        self.spi = spi
        self.gpio = gpio
        
        self.spiritVersion = spiritVersion
        self.rangeExtType = rangeExtType
        self.xtalFrequency = xtalFrequency
        self.bandSelect = bandSelect
        
        self.tim3Ch4CompareModeRaised = 0
        
#     def _enableTCX0(self):
#         #SOME GPIO BULLSHIT
#         self.spi.writeRegisters(0x01, bytearray([0xD0]))
        
    def setXtalFrequency(self, xtalFrequency):
        self.xtalFrequency = xtalFrequency
    
    def setVersion(self, version):
        self.spiritVersion = version
        
#     def computeXtalFrequency(self):
#         if self.rangeExtType == RANGE_EXT_SKYWORKS:
#             self._enableTCX0()
#         
#         #set spiritclock on gpio0
#         
#         #configure clock freq to be divided by 192
        
    def computeSpiritVersion(self):
        pass
    
    def identificationRFBoard(self):
        pass
    
    def computeBand(self):
        pass
    
    def getRangeExtender(self):
        pass
    
    def getXtalFrequency(self):
        pass
    
    def waVcoCalibration(self):
        pass
    
    def waRcoCalibration(self):
        pass
    
    def waRxStartupInit(self):
        pass
    
    def waRxStartup(self):
        pass
    
    def waCmdStrobeTx(self):
        pass
    
    def waCmdStrobeRx(self):
        pass
    
    def waTRxFcMem(self, nDesiredFreq):
        pass
    
    def rangeExtInit(self):
        pass
    
    def tim3IRQHandler(self):
        pass