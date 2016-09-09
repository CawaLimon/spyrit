import spirit_regs

CALIB_TIME_7_33_US_24MHZ,\
CALIB_TIME_14_67_US_24MHZ,\
CALIB_TIME_29_33_US_24MHZ,\
CALIB_TIME_58_67_US_24MHZ = range(4)

CALIB_TIME_6_77_US_26MHZ,\
CALIB_TIME_13_54_US_26MHZ,\
CALIB_TIME_27_08_US_26MHZ,\
CALIB_TIME_54_15_US_26MHZ = range(4)

VCO_L, VCO_H = range(2)

class Calibration:
    def __init__(self, spi):
        self.spi = spi
        
    def enableRco(self, xNewState):
        tempRegValue = self.spi.readRegisters(spirit_regs.PROTOCOL2_BASE)
        
        if xNewState:
            tempRegValue[0] |= spirit_regs.PROTOCOL2_RCO_CALIBRATION_MASK
        else:
            tempRegValue[0] &= ~spirit_regs.PROTOCOL2_RCO_CALIBRATION_MASK
            
        self.spi.writeRegisters(spirit_regs.PROTOCOL2_BASE, tempRegValue)
        
    def enableVco(self, xNewState):
        tempRegValue = self.spi.readRegisters(spirit_regs.PROTOCOL2_BASE)
        
        if xNewState:
            tempRegValue[0] |= spirit_regs.PROTOCOL2_VCO_CALIBRATION_MASK
        else:
            tempRegValue[0] &= ~spirit_regs.PROTOCOL2_VCO_CALIBRATION_MASK
            
        self.spi.writeRegisters(spirit_regs.PROTOCOL2_BASE, tempRegValue)
    
    def setRcoCalWords(self, cRwt, cRfb):
        tempRegValue = bytearray(2)
        
        tempRegValue[0] = (cRwt << 4) | (cRfb >> 1)
        
        tempRegValue[1] = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_IN1_BASE)[0]
        
        tempRegValue[1] = (tempRegValue[1]&0x7F) | (cRfb<<7)
        
        self.spi.writeRegisters(spirit_regs.RCO_VCO_CALIBR_IN2_BASE, tempRegValue)
        
    def getRcoCalWords(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_OUT1_BASE, 2)
        
        pcRwt = tempRegValue[0] >> 4
        pcRfb = (tempRegValue[0] & 0x0F) <<1 |(tempRegValue[1]>>7)
        return pcRwt, pcRfb
    
    def getVcoCalData(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_OUT0_BASE)
        
        return tempRegValue[0]&0x7F
    
    def setVcoCalDataTx(self, cVcoCalData):
        tempRegValue = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_IN1_BASE)
        
        tempRegValue[0] &= 0x80
        tempRegValue[0] |= cVcoCalData
        
        self.spi.writeRegisters(spirit_regs.RCO_VCO_CALIBR_IN1_BASE, tempRegValue)
        
    def getVcoCalDataTx(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_IN1_BASE)
        
        return tempRegValue[0]&0x7F
    
    def setVcoCalDataRx(self, cVcoCalData):
        tempRegValue = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_IN0_BASE)
        
        tempRegValue[0] &= 0x80
        tempRegValue[0] |= cVcoCalData
        
        self.spi.writeRegisters(spirit_regs.RCO_VCO_CALIBR_IN0_BASE, tempRegValue)
    
    def getVcoCalDataRx(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.RCO_VCO_CALIBR_IN0_BASE)
        
        return tempRegValue[0]&0x7F
    
    def setVcoWindow(self, xRefWord):
        tempRegValue = self.spi.readRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
        
        tempRegValue[0] &= 0xFC
        tempRegValue[0] |= xRefWord
        
        self.spi.writeRegisters(spirit_regs.SYNTH_CONFIG1_BASE, tempRegValue)
    
    def getVcoWindow(self):
        tempRegValue1 = self.spi.readRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
        tempRegValue2 = self.spi.readRegsiters(spirit_regs.ANA_FUNC_CONF0_BASE)
        
        tempRegValue1[0] &= 0x03
        tempRegValue2[0] = ((tempRegValue2[0]&0x40)>>6)
        
        if tempRegValue2[0]:
            if tempRegValue1[0] == 0:
                refWord = CALIB_TIME_6_77_US_26MHZ
            elif tempRegValue1[0] == 1:
                refWord = CALIB_TIME_13_54_US_26MHZ
            elif tempRegValue1[0] == 2:
                refWord = CALIB_TIME_27_08_US_26MHZ
            else:
                refWord = CALIB_TIME_54_15_US_26MHZ
        else:
            if tempRegValue1[0] == 0:
                refWord = CALIB_TIME_7_33_US_24MHZ
            elif tempRegValue1[0] == 1:
                refWord = CALIB_TIME_14_67_US_24MHZ
            elif tempRegValue1[0] == 2:
                refWord = CALIB_TIME_29_33_US_24MHZ
            else:
                refWord = CALIB_TIME_58_67_US_24MHZ
                
        return refWord
    
    def selectVco(self, xVco):
        tempRegValue = self.spi.readRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
        
        tempRegValue[0] &= 0xF9
        
        if xVco == VCO_H:
            tempRegValue[0] |= 0x02
        else:
            tempRegValue[0] |= 0x04
        
        self.spi.writeRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
    
    def getVcoSelection(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
        
        if tempRegValue == 0x01:
            return VCO_H
        else:
            return VCO_L
    
    