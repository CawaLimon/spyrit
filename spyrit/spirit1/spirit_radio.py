import spirit_regs
import spirit_status
import spirit_calibration

from math import log2

XTAL_FLAG_24_MHz = 0x00
XTAL_FLAG_26_MHz = 0x01
    
HIGH_BAND = 0x00
MIDDLE_BAND = 0x01
LOW_BAND = 0x02
VERY_LOW_BAND = 0x03
        
FSK = 0x00
GFSK_BT05 = 0x50
GFSK_BT1 = 0x10
ASK_OOK = 0x20
MSK = 0x30
    
LOAD_0_PF = 0x00
LOAD_1_2_PF = 0x40
LOAD_2_4_PF = 0x80
LOAD_3_6_PF = 0xC0
    
AFC_SLICER_CORRECTION = 0x00
AFC_2ND_IF_CORRECTION = 0x10
    
CLK_REC_PLL = 0x00
CLK_REC_DLL = 0x08
    
PSTFLT_LENGTH_8 = 0x00
PSTFLT_LENGTH_16 = 0x10
    
FAST_DECAY = 0x00
MEDIUM_FAST_DECAY = 0x01
MEDIUM_SLOW_DECAY = 0x02
SLOW_DECAY = 0x03
        
FBASE_DIVIDER = 262144
HIGH_BAND_FACTOR = 6
MIDDLE_BAND_FACTOR = 12
LOW_BAND_FACTOR = 16
VERY_LOW_BAND_FACTOR = 32

HIGH_BAND_LOWER_LIMIT = 779000000
HIGH_BAND_UPPER_LIMIT = 956500000
MIDDLE_BAND_LOWER_LIMIT = 387000000
MIDDLE_BAND_UPPER_LIMIT = 470000000
LOW_BAND_LOWER_LIMIT = 300000000
LOW_BAND_UPPER_LIMIT = 348000000
VERY_LOW_BAND_LOWER_LIMIT = 150000000
VERY_LOW_BAND_UPPER_LIMIT = 174000000

F_OFFSET_DIVIDER = 262144
PPM_FACTOR = 1e6

CHSPACE_DIVIDER = 32768

DATARATE_DIVIDER = 268435456
DATARATE_EXPONENT_UPPER_LIMIT = 15
MINIMUM_DATARATE = 100
MAXIMUM_DATARATE = 500000

FDEV_DIVIDER = 262144
F_DEV_MANTISSA_UPPER_LIMIT = 7
F_DEV_EXPONENT_UPPER_LIMIT = 9

BW_EXPONENT_UPPER_LIMIT = 9
BW_MANTISSA_UPPER_LIMIT = 8

PA_LOWER_LIMIT_DBM = -32.0
PA_UPPER_LIMIT_DBM = 11.227
PA_COEFFICIENT_DBM = 0.4678

#available VCO frequencies
VCO_FREQS = [4644, 4708, 4772, 4836, 4902, 4966, 5030, 5095, \
    5161, 5232, 5303, 5375, 5448, 5519, 5592, 5663]

BANDWIDTH26M = [8001, 7951, 7684, 7368, 7051, 6709, 6423, 5867, 5414, \
    4509, 4259, 4032, 3808, 3621, 3417, 3254, 2945, 2703, \
      2247, 2124, 2011, 1900, 1807, 1706, 1624, 1471, 1350, \
        1123, 1062, 1005,  950,  903,  853,  812,  735,  675, \
          561,  530,  502,  474,  451,  426,  406,  367,  337, \
            280,  265,  251,  237,  226,  213,  203,  184,  169, \
              140,  133,  126,  119,  113,  106,  101,   92,   84, \
                70,   66,   63,   59,   56,   53,   51,   46,   42, \
                  35,   33,   31,   30,   28,   27,   25,   23,   21, \
                    18, 17, 16, 15, 14, 13, 13, 12, 11]

B_HALF_FACTOR = [HIGH_BAND_FACTOR/2, MIDDLE_BAND_FACTOR/2, LOW_BAND_FACTOR/2, VERY_LOW_BAND_FACTOR/2]

BAND_REG_VALUE = [spirit_regs.SYNT0_BS_6, spirit_regs.SYNT0_BS_12, spirit_regs.SYNT0_BS_16, spirit_regs.SYNT0_BS_32]

class Radio:
    def __init__(self, 
                 spirit,
                 lXtalFrequency,
                 nXtalOffsetPpm,
                 lFrequencyBase,
                 fChannelSpace,
                 cChannelNumber,
                 xModulationSelect,
                 fDatarate,
                 fFreqDev,
                 lBandwidth):
        
        self.spirit = spirit
        self.version = self.spirit.general.getSpiritVersion()
        
        #Workaround for Vtune?
        self.spirit.spi.writeRegisters(0x9F, bytearray([0xA0]))
        
        #Calculates the offset respect to RF frequency and according to xtal_ppm param
        fOffsetTmp = nXtalOffsetPpm * lFrequencyBase / PPM_FACTOR
        
#         cDivider = bytearray(1)
#         self.spirit.spi.readRegisters(spirit_regs.XO_RCO_TEST, 1, cDivider)
#         cDivider = (cDivider[0] >> 3) & 0x1
#         if cDivider == 0:
#             cDivider = 2
            
        self.lXtalFrequency = lXtalFrequency
        self.nXtalOffsetPpm = nXtalOffsetPpm
        self.lFrequencyBase = lFrequencyBase
        self.fChannelSpace = fChannelSpace
        self.cChannelNumber = cChannelNumber
        self.xModulationSelect = xModulationSelect
        self.fDatarate = fDatarate
        self.fFreqDev = fFreqDev
        self.lBandwidth = lBandwidth
        
        #Disable the digital, ADC, smps REFERENCE CLOCK DIVIDER IF FxO>24mhZ OR Fxo < 26 mhz
        self.spirit.command.strobeStandby()
        self.spirit.status.waitForState(spirit_status.STATE_STANDBY)
        
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.XO_RCO_TEST_BASE)
        if self.lXtalFrequency < 48000000:
            tempRegValue[0] |= 0x08
        else:
            tempRegValue[0] &= 0xF7
        
        self.spirit.spi.writeRegisters(spirit_regs.XO_RCO_TEST_BASE, tempRegValue)
        
        self.spirit.command.strobeReady()
        self.spirit.status.waitForState(spirit_status.STATE_READY)
        
        #Calculate the FC_OFFSET param and cast as signed int
        fOffset = (fOffsetTmp * FDEV_DIVIDER) / self.lXtalFrequency
        fOffset = fOffset if fOffset >= 0 else fOffset + 4096
        
        #Calculates the channel space factor
        fChannelSpaceFactor = self.fChannelSpace / (float(self.lXtalFrequency) / CHSPACE_DIVIDER)
        cChannelSpaceFactor = round(fChannelSpaceFactor)
        
        #Calculate the channel center freq
        fC = float(self.lFrequencyBase) + fOffset + ((float(cChannelSpaceFactor * self.lXtalFrequency) / CHSPACE_DIVIDER) * self.cChannelNumber)
        
        self.spirit.management.WaTRxFcMem(fC) #no idea
        #Calculates the mantissas and exponents for these values
        drM, drE = self.searchDatarateME(self.fDatarate)
        fDevM, fDevE = self.searchFreqDevME(self.fFreqDev)
        bwM, bwE = self.searchChannelBwME(self.lBandwidth)
        
        if self.lXtalFrequency == 24000000:
            ifOffsetAna = 0xB6
            ifOffsetDig = 0xB6
        elif self.lXtalFrequency == 25000000:
            ifOffsetAna = 0xAC
            ifOffsetDig = 0xAC
        elif self.lXtalFrequency == 26000000:
            ifOffsetAna = 0xA3
            ifOffsetDig = 0xA3
        elif self.lXtalFrequency == 48000000:
            ifOffsetAna = 0x3B
            ifOffsetDig = 0xB6
        elif self.lXtalFrequency == 50000000:
            ifOffsetAna = 0x36
            ifOffsetDig = 0xA3
        else:
            ifOffsetAna = 0x31
            ifOffsetDig = 0xA3
            
        self.spirit.spi.writeRegisters(spirit_regs.IF_OFFSET_DIG_BASE, bytearray([ifOffsetDig]))
        self.spirit.spi.writeRegisters(spirit_regs.IF_OFFSET_ANA_BASE, bytearray([ifOffsetAna]))
        
        fcOffsetArray = bytearray(2)
        fcOffsetArray[0] = fOffset & 0x0F00
        fcOffsetArray[1] = fOffset & 0xFF
        self.spirit.spi.writeRegisters(spirit_regs.FC_OFFSET1_BASE, fcOffsetArray)
        
        self.setXtalFlag(self.lXtalFrequency)
        digConfigArray = bytearray(4)
        digConfigArray[0] = drM
        digConfigArray[1] = self.xModulationSelect | drE
        digConfigArray[2] = (fDevE << 4) | fDevM
        digConfigArray[3] = (bwM << 4) | bwE
        self.spirit.spi.writeRegisters(spirit_regs.MOD1_BASE, digConfigArray)
        
        self.spirit.spi.writeRegisters(spirit_regs.CHNUM_BASE, bytearray([cChannelNumber]))
        
        self.setFrequencyBase(self.lFrequencyBase)
        
    def getInfo(self):
        anaRadioRegArray = self.spirit.spi.readRegisters(spirit_regs.SYNT3_BASE, 8)
        digRadioRegArray = self.spirit.spi.readRegisters(spirit_regs.MOD1_BASE, 4)
        
        
    
    def setXtalFlag(self, flag):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.ANA_FUNC_CONF0_BASE, 1)
        if flag == XTAL_FLAG_26_MHz:
            tempRegValue[0] |= spirit_regs.SELECT_24_26_MHZ_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.SELECT_24_26_MHZ_MASK)
        
        self.spirit.spi.writeRegisters(spirit_regs.ANA_FUNC_CONF0_BASE, tempRegValue)
    
    def getXtalFlag(self):
        tempRegValue = self.spirit.readRegisters(spirit_regs.ANA_FUNC_CONF0_BASE)
        return (tempRegValue[0] & spirit_regs.SELECT_24_26_MHZ_MASK) >> 6
    
    def searchWCP(self, lFc):
        #search operating band
        if HIGH_BAND_LOWER_LIMIT <= lFc <= HIGH_BAND_UPPER_LIMIT:
            bFactor = HIGH_BAND_FACTOR
        elif MIDDLE_BAND_LOWER_LIMIT <= lFc <= MIDDLE_BAND_UPPER_LIMIT:
            bFactor = MIDDLE_BAND_FACTOR
        elif LOW_BAND_LOWER_LIMIT <= lFc <= LOW_BAND_UPPER_LIMIT:
            bFactor = LOW_BAND_FACTOR
        elif VERY_LOW_BAND_LOWER_LIMIT <= lFc <= VERY_LOW_BAND_UPPER_LIMIT:
            bFactor = VERY_LOW_BAND_FACTOR
        else:
            raise TypeError("Invalid Center Frequency")
            
        #calculates the vco frequency FCOFreq = Fc*B
        vcofreq = lFc/1e6
        vcofreq *= bFactor
        
        for i in range(len(VCO_FREQS) - 1):
            if VCO_FREQS[i] <= vcofreq < VCO_FREQS[i+1]:
                return i%8
    
    def setSynthWord(self, lSynthWord):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.SYNT0_BASE)
        #mask the band select field
        tempRegValue &= 0x07
        
        tempArray = bytearray(4)
        tempArray[0] = (lSynthWord>>21)&(0x0000001F)
        tempArray[1] = (lSynthWord>>13)&(0x000000FF)
        tempArray[2] = (lSynthWord>>5)&(0x000000FF)
        tempArray[3] = ((lSynthWord&0x0000001F)<<3) | tempRegValue
        
        self.spirit.spi.writeRegisters(spirit_regs.SYNT3_BASE, tempArray)
    
    def getSynthWord(self):
        regArray = self.spirit.spi.readRegisters(spirit_regs.SYNT3_BASE, 4)
        word3 = (regArray[0] & 0x1F) << 21
        word2 = regArray[1] << 13
        word1 = regArray[2] << 5
        word0 = regArray[0] >> 3
        return word0 + word1 + word2 + word3
    
    def setBand(self, xBand):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.SYNT0_BASE)
        tempRegValue &= 0xF8
        if xBand == HIGH_BAND:
            bandRegValue = spirit_regs.SYNT0_BS_6
        elif xBand == MIDDLE_BAND:
            bandRegValue = spirit_regs.SYNT0_BS_12
        elif xBand == LOW_BAND:
            bandRegValue = spirit_regs.SYNT0_BS_16
        elif xBand == VERY_LOW_BAND:
            bandRegValue = spirit_regs.SYNT0_BS_32
        else:
            raise TypeError("Invalid band")
        tempRegValue |= bandRegValue
        
        self.spirit.spi.writeRegisters(spirit_regs.SYNT0_BASE, tempRegValue)
    
    def getBand(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.SYNT0_BASE)
        
        if tempRegValue & 0x07 == spirit_regs.SYNT0_BS_6:
            return HIGH_BAND
        elif tempRegValue & 0x07 == spirit_regs.SYNT0_BS_12:
            return MIDDLE_BAND
        elif tempRegValue & 0x07 == spirit_regs.SYNT0_BS_16:
            return LOW_BAND
        else:
            return VERY_LOW_BAND
    
    def setChannel(self, cChannel):
        self.spirit.spi.writeRegisters(spirit_regs.CHNUM_BASE, bytearray([cChannel]))
    
    def getChannel(self):
        return self.spirit.spi.readRegisters(spirit_regs.CHNUM_BASE)[0]
    
    def setChannelSpace(self, fChannelSpace):
        fChannelSpaceFactor = fChannelSpace/(self.lXtalFrequency/CHSPACE_DIVIDER)
        cChannelSpaceFactor = round(fChannelSpaceFactor)
        
        self.spirit.spi.writeRegisters(spirit_regs.CHSPACE_BASE, bytearray([cChannelSpaceFactor]))
    
    def getChannelSpace(self):
        channelSpaceFactor = self.spirit.spi.readRegisters(spirit_regs.CHSPACE_BASE)[0]
        return float(channelSpaceFactor)*(self.lXtalFrequency/CHSPACE_DIVIDER)
    
    def setFrequencyOffsetPpm(self, nXtalPpm):
        synthWord = self.getSynthWord()
        band = self.getBand()
        fBase = float(synthWord)*(float(self.lXtalFrequency)/FBASE_DIVIDER*(1.0/B_HALF_FACTOR[band]))
        fOffsetTmp = nXtalPpm*(fBase/PPM_FACTOR)
        xtalOffsetFactor = (float(fOffsetTmp)/float(self.lXtalFrequency)/FBASE_DIVIDER)
        
        tempArray = bytearray(2)
        tempArray[0] = (xtalOffsetFactor>>8) & 0x0F
        tempArray[1] = xtalOffsetFactor & 0xFF
        
        self.spirit.spi.writeRegisters(spirit_regs.FC_OFFSET1_BASE, tempArray)
    
    def setFrequencyOffset(self, lFOffset):
        offset = (float(lFOffset)/(float(self.lXtalFrequency)/FBASE_DIVIDER))
        
        tempArray = bytearray(2)
        tempArray[0] = (offset >> 8) & 0x0F
        tempArray[1] = offset & 0xFF
        
        self.spirit.spi.writeRegisters(spirit_regs.FC_OFFSET1_BASE, tempArray)
    
    def getFrequencyOffset(self):
        tempArray = self.spirit.spi.readRegisters(spirit_regs.FC_OFFSET1_BASE, 2)
        
        xtalOffTemp = (tempArray[0]<<8) + tempArray[1]
        if xtalOffTemp & 0x0800:
            xtalOffTemp |= 0xF000
        else:
            xtalOffTemp &= 0x0FFF    
        
        return float(xtalOffTemp) * (float(self.lXtalFrequency)/FBASE_DIVIDER)
    
    def setFrequencyBase(self, lFBase):
        if HIGH_BAND_LOWER_LIMIT <= lFBase <= HIGH_BAND_UPPER_LIMIT:
            band = HIGH_BAND
        elif MIDDLE_BAND_LOWER_LIMIT <= lFBase <= MIDDLE_BAND_UPPER_LIMIT:
            band = MIDDLE_BAND
        elif LOW_BAND_LOWER_LIMIT <= lFBase <= LOW_BAND_UPPER_LIMIT:
            band = LOW_BAND
        elif VERY_LOW_BAND_LOWER_LIMIT <= lFBase <= VERY_LOW_BAND_UPPER_LIMIT:
            band = VERY_LOW_BAND
        
        fOffset = self.getFrequencyOffset()
        fChannelSpace = self.getChannelSpace()
        cChannelNum = self.getChannel()
        
        fC = float(lFBase) + float(fOffset) + fChannelSpace*cChannelNum
        
        cRefDiv = self.getRefDiv() + 1
        if band == VERY_LOW_BAND:
            if fC < 161281250:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_L)
            else:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_H)
        elif band == LOW_BAND:
            if fC < 322562500:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_L)
            else:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_H)
        elif band == MIDDLE_BAND:
            if fC < 430083334:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_L)
            else:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_H)
        elif band == HIGH_BAND:
            if fC < 860166667:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_L)
            else:
                self.spirit.calibration.selectVco(spirit_calibration.VCO_H)
        
        synthWord = float(lFBase)*B_HALF_FACTOR[band]*((float(FBASE_DIVIDER*cRefDiv/self.lXtalFrequency)))
        
        wcp = self.searchWCP(fC)
        
        anaRadioRegArray = bytearray(4)
        anaRadioRegArray[0] = ((synthWord>>21)&(0x0000001F))|(wcp<<5)
        anaRadioRegArray[1] = (synthWord>>13)&(0x0000000F)
        anaRadioRegArray[2] = (synthWord>>5)&(0x000000FF)
        anaRadioRegArray[3] = ((synthWord&0x0000001F)<<3)|BAND_REG_VALUE[band]
        
        self.spirit.spi.writeRegisters(spirit_regs.SYNT3_BASE, anaRadioRegArray)
        
    def getFrequencyBase(self):
        synthWord = self.getSynthWord()
        band = self.getBand()
        
        cRefDiv = self.getRefDiv() + 1
        
        return (float(synthWord)*(float(self.lXtalFrequency)/FBASE_DIVIDER)/float(B_HALF_FACTOR[band]/cRefDiv))
    
    def getCenterFrequency(self):
        fBase = self.getFrequencyBase()
        offset = self.getFrequencyOffset()
        channelSpace = self.getChannelSpace()
        channel = self.getChannel()
        
        return fBase + offset + channelSpace*channel
    
    def searchDatarateME(self, fDatarate):
        """
        @brief Returns the mantissa and exponent, whose value is used in the datarate
        formula will give the datarate value closer to the given datarate.
        @param fDatarate datarate expressed in bps, between 100 and 500000
        @retval pcM, pcE mantissa and exponent
        """
        cDivider = 1 - ((self.spirit.spi.readRegisters(spirit_regs.XO_RCO_TEST_BASE)[0]>>3)&0x1)
#         cDivider = cDivider if cDivider != 0 else 2
        for i in range(DATARATE_EXPONENT_UPPER_LIMIT, -1, -1):
            if fDatarate >= (self.lXtalFrequency>>(20-i+cDivider)):
                pcE = i
                break
        else:
            pcE = 0
        
        pcM = (float(DATARATE_DIVIDER/(self.lXtalFrequency>>cDivider))*fDatarate*1.0/float(1<<pcE))-256
        pcM = round(pcM)
        return pcM, pcE
    
    def searchFreqDevME(self, fFDev):
        for i in range(F_DEV_EXPONENT_UPPER_LIMIT, -1, -1):
            if fFDev >= (self.lXtalFrequency>>(16-i)):
                pcE = i
                break
        else:
            pcE = 0
            
        fMantissaTmp = 2 * (float(FDEV_DIVIDER)/self.lXtalFrequency)*fFDev*(1.0/float(1<<pcE))-8
        pcM = round(fMantissaTmp)
        
        return pcM, pcE
    
    def searchChannelBwME(self, lBandwidth):
        cDivider = ((self.spirit.spi.readRegisters(spirit_regs.XO_RCO_TEST_BASE)[0]>>3)&0x1)
        
        for i in range(len(BANDWIDTH26M)-1):
            if BANDWIDTH26M[i] >= lBandwidth/(1e2*self.lXtalFrequency/26e6/cDivider) > BANDWIDTH26M[i+1]:
                index = i
                break
        else:
            index = 0
        
        pcE = int(index/9)
        pcM = index%9
        return pcM, pcE
    
    def setDatarate(self, fDatarate):
        drM, drE = self.searchDatarateME(fDatarate)
        
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.MOD1_BASE, 2)
        tempRegValue[0] = drM
        tempRegValue[1] &= 0xF0
        tempRegValue[1] |= drE
        
        self.spirit.spi.writeRegisters(spirit_regs.MOD1_BASE, tempRegValue)
    
    def getDatarate(self):
        tempRegValue = self.spirit.readRegisters(spirit_regs.MOD1_BASE, 2)
        
        cDivider = self.spirit.spi.readRegisters(spirit_regs.XO_RCO_TEST_BASE)[0]
        cDivider = cDivider if cDivider != 0 else 2
        
        return float(float((self.lXtalFrequency/cDivider)/DATARATE_DIVIDER)*float(256+tempRegValue[0])*float(pow(2, tempRegValue[1]&0x0F)))
    
    def setFrequencyDev(self, lFDev):
        fDevM, fDevE = self.searchFreqDevME(lFDev)
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.FDEV0_BASE)
        
        tempRegValue[0] &= 0x08
        tempRegValue[0] |= ((fDevE<<4)|(fDevM))
    
        self.spirit.spi.writeRegisters(spirit_regs.FDEV0_BASE, tempRegValue)
        
    def getFrequencyDev(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.FDEV0_BASE)
        fDevM = tempRegValue[0]&0x07
        fDevE = (tempRegValue[0]&0xF0)>>4
        
        return float((float(self.lXtalFrequency/FDEV_DIVIDER)*float(8+fDevM)*\
                      float(pow(2,fDevE))))
    
    def setChannelBW(self, lBandwidth):
        bwM, bwE = self.searchChannelBwME(lBandwidth)
        tempRegValue = bytearray([(bwM<<4)|(bwE)])
        self.spirit.spi.writeRegisters(spirit_regs.CHFLT_BASE, tempRegValue)
    
    def getChannelBW(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CHFLT_BASE)
        bwM = (tempRegValue[0]&0xF0)>>4
        bwE = tempRegValue[0]&0x0F
        
        return round(100.0*BANDWIDTH26M[bwM+(bwE*9)]*self.lXtalFrequency/26e6)
    
    def setModulation(self, xModulation):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.MOD0_BASE)
        
        tempRegValue[0] &= 0x8F
        tempRegValue |= xModulation
        
        self.spirit.spi.writeRegisters(spirit_regs.MOD0_BASE, tempRegValue)
    
    def getModulation(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.MOD0_BASE)
        
        return tempRegValue[0]&0x70
    
    def setCWTransmitMode(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.MOD0_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.MOD0_CW
        else:
            tempRegValue[0] &= (~spirit_regs.MOD0_CW)
        
        self.spirit.spi.writeRegisters(spirit_regs.MOD0_BASE, tempRegValue)
    
    def setOokPeakDecay(self, xOokDecay):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.RSSI_FLT_BASE)
        
        tempRegValue[0] &= 0xFC
        tempRegValue[0] |= xOokDecay
        
        self.spirit.spi.writeRegisters(spirit_regs.RSSI_FLT_BASE, tempRegValue)
    
    def getOokPeakDecay(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.RSSI_FLT_BASE)
        return tempRegValue[0]&0x03
    
    def setPATabledBm(self, cPALevelMaxIndex, cWidth, xCLoad, pfPAtabledBm):
        palevel = [0] * cPALevelMaxIndex
        for i in range(cPALevelMaxIndex):
            paLevelValue = int(float(PA_UPPER_LIMIT_DBM = pfPAtabledBm)/PA_COEFFICIENT_DBM+1)
            paLevelValue = paLevelValue if paLevelValue <= 90 else 90
            palevel[cPALevelMaxIndex-i] = paLevelValue
        
        palevel.append(xCLoad|(cWidth-1)<<3|cPALevelMaxIndex)
        
        address = spirit_regs.PA_POWER8_BASE+7-cPALevelMaxIndex
        
        self.spirit.spi.writeRegisters(address, cPALevelMaxIndex, bytearray(palevel))
    
    def getPATabledBm(self, pcPALevelMaxIndex, pfPAtabledBm):
        # @TODO: finish this func
#         pslevelvect = self.spirit.spi.readRegisters(spirit_regs.PA_POWER8_BASE, 9)
#         
#         for i in range(7, -1, -1):
#             pfPA
        pass
    
    def setPATable(self, cPALevelMaxIndex, cWidth, xCLoad, pcPAtable):
        palevel = [0] * cPALevelMaxIndex
        # @TODO: finish this func
        pass
        
    
    def getPATable(self, pcPALevelMaxIndex, pcPAtable):
        pass
    
    def setPALeveldBm(self, cIndex, fPowerdBm):
        paLevelValue = float(PA_UPPER_LIMIT_DBM-fPowerdBm)/PA_COEFFICIENT_DBM+1
        paLevelValue = paLevelValue if paLevelValue <= 90 else 90
        
        address = spirit_regs.PA_POWER8_BASE+7-cIndex
        
        self.spirit.spi.writeRegisters(address, bytearray([paLevelValue]))
    
    def getPALeveldBm(self, cIndex):
        address = spirit_regs.PA_POWER8_BASE+7-cIndex
        
        paLevelValue = self.spirit.spi.readRegisters(address)[0]
        return float(PA_UPPER_LIMIT_DBM - (paLevelValue-1)*PA_COEFFICIENT_DBM)
    
    def setPALevel(self, cIndex, cPower):
        address = spirit_regs.PA_POWER8_BASE+7-cIndex
        
        self.spirit.spi.writeRegisters(address, bytearray([cPower]))
    
    def getPALevel(self, cIndex):
        address = spirit_regs.PA_POWER8_BASE+7-cIndex
        tempRegValue = self.spirit.spi.readRegisters(address)
        return tempRegValue[0]
    
    def setPACwc(self, xCLoad):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        
        tempRegValue[0] &= 0x3F
        tempRegValue[0] |= xCLoad
        
        self.spirit.spi.writeRegisters(spirit_regs.PA_POWER0_BASE, tempRegValue)
        
    def getPACwc(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        return tempRegValue[0]&0xC0
    
    def setPALevelMaxIndex(self, cIndex):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        
        tempRegValue[0] &= 0xF8
        tempRegValue[0] |= cIndex
        
        self.spirit.spi.writeRegisters(spirit_regs.PA_POWER0_BASE, tempRegValue)
    
    def getPALevelMaxIndex(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        
        return tempRegValue[0]&0x07
        
    def setPAStepWidth(self, cWidth):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        
        tempRegValue[0] &= 0xE7
        tempRegValue[0] |= (cWidth-1)<<3
        
        self.spirit.spi.writeRegisters(spirit_regs.PA_POWER0_BASE, tempRegValue)
    
    def getPAStepWidth(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        tempRegValue[0] &= 0x18
        return tempRegValue[0]>>3
    
    def setPARamping(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.PA_POWER0_PA_RAMP_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.PA_POWER0_PA_RAMP_MASK)
        self.spirit.spi.writeRegisters(spirit_regs.PA_POWER0_BASE, tempRegValue)
    
    def getPARamping(self):
        tempRegValue = self.spirit.spi.readRegister(spirit_regs.PA_POWER0_BASE)
        return (tempRegValue[0]>>5)&0x01
    
    def disablePA(self):
        tempRegValue = bytearray([0x00, 0x00])
        
        tempRegValue[1] = self.spirit.spi.readRegisters(spirit_regs.PA_POWER0_BASE)[0]
        tempRegValue[1] &= 0xF8
        
        self.spirit.spi.writeRegisters(spirit_regs.PA_POWER1_BASE, tempRegValue)
    
    def setAFC(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC2_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.AFC2_AFC_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.AFC2_AFC_MASK)
            
        self.spirit.spi.writeRegisters(spirit_regs.AFC2_BASE, tempRegValue)
    
    def setAFCFreezeOnSync(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC2_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.AFC2_AFC_FREEZE_ON_SYNC_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.AFC2_AFC_FREEZE_ON_SYNC_MASK)
            
        self.spirit.spi.writeRegisters(spirit_regs.AFC2_BASE, tempRegValue)
    
    def setAFCMode(self, xMode):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC2_BASE)
        if xMode == spirit_regs.AFC2_AFC_MODE_MIXER:
            tempRegValue[0] |= spirit_regs.AFC2_AFC_MODE_MIXER
        else:
            tempRegValue[0] &= (~spirit_regs.AFC2_AFC_MODE_MIXER)
            
        self.spirit.spi.writeRegisters(spirit_regs.AFC2_BASE, tempRegValue)
    
    def getAFCMode(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC2_BASE)
        
        return tempRegValue[0]&0x20
    
    def setAFCPDLeakage(self, cLeakage):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC2_BASE)
        tempRegValue[0] &= 0xE0
        tempRegValue[0] |= cLeakage
        
        self.spirit.spi.writeRegisters(spirit_regs.AFC2_BASE, tempRegValue)
    
    def getAFCPDLeakage(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC2_BASE) 
        return tempRegValue[0] & 0x1F
    
    def setAFCFastPeriod(self, cLength):
        self.spirit.spi.writeRegisters(spirit_regs.AFC1_BASE, bytearray([cLength]))
    
    def getAFCFastPeriod(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC1_BASE)
        return tempRegValue[0]
    
    def setAFCFastGain(self, cGain):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC0_BASE)
        tempRegValue[0] &= 0x0F
        tempRegValue[0] |= cGain<<4
        
        self.spirit.spi.writeRegisters(spirit_regs.AFC0_BASE, tempRegValue)
        
    def getAFCFastGain(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC0_BASE)
        return (tempRegValue[0]&0xF0)>>4
    
    def setAFCSlowGain(self, cGain):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC0_BASE)
        tempRegValue[0] &= 0xF0
        tempRegValue[0] |= cGain
        
        self.spirit.spi.writeRegisters(spirit_regs.AFC0_BASE, tempRegValue)
    
    def getAFCSlowGain(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC0_BASE)
        
        return tempRegValue[0] & 0x0F
    
    def getAFCCorrectionReg(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AFC_CORR_BASE)
        return tempRegValue[0]
    
    def getAFCCorrectionHz(self):
        correction = self.getAFCCorrectionReg()
        return float(self.lXtalFrequency/(12*pow(2, 10))*2*correction)
    
    def autoSetFOffset(self):
        fCorrection = self.getAFCCorrectionHz()
        fOffset = self.getFrequencyOffset()
        
        fOffset += fCorrection
        
        self.setFrequencyOffset(fOffset)
    
    def enableAGC(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.AGCCTRL0_AGC_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.AGCCTRL0_AGC_MASK)
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL0_BASE, tempRegValue)
    
    def setAGCMode(self, xMode):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        if xMode == spirit_regs.AGCCTRL0_AGC_MODE_BINARY:
            tempRegValue[0] |= spirit_regs.AGCCTRL0_AGC_MODE_BINARY
        else:
            tempRegValue[0] &= (~spirit_regs.AGCCTRL0_AGC_MODE_BINARY)
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL0_BASE, tempRegValue)
    
    def getAGCMode(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        return tempRegValue[0]&0x40
    
    def enableAGCFreezeOnSteady(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.AGCCTRL2_FREEZE_ON_STEADY_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.AGCCTRL2_FREEZE_ON_STEADY_MASK)
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL2_BASE, tempRegValue)
    
    def enableAGCFreezeOnSync(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.AGCCTRL2_FREEZE_ON_SYNC_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.AGCCTRL2_FREEZE_ON_SYNC_MASK)
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL2_BASE, tempRegValue)
    
    def enableAGCStartMaxAttenuation(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)
        if xNewState:
            tempRegValue[0] |= spirit_regs.AGCCTRL2_START_MAX_ATTENUATION_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.AGCCTRL2_START_MAX_ATTENUATION_MASK)
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL2_BASE, tempRegValue)
    
    def setAGCMeasureTimeUs(self, cTime):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)
        
        measure = round(log2(float(cTime/1e6 * self.lXtalFrequency/12)))
        measure = measure if measure <= 15 else 15
        
        tempRegValue[0] &= 0xF0
        tempRegValue[0] |= measure
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL2_BASE, tempRegValue)
    
    def getAGCMeasureTimeUs(self):
        measure = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)[0]
        measure &= 0x0F
        
        return int((12.0/self.lXtalFrequency)*float(pow(2, measure)*1e6))
    
    def setAGCMeasureTime(self, cTime):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)
        
        tempRegValue[0] &= 0xF0
        tempRegValue[0] |= cTime
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL2_BASE, tempRegValue)
        
    def getAGCMeasureTime(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL2_BASE)
        return tempRegValue[0]&0x0F
    
    def setAGCHoldTimeUs(self, cTime):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        
        hold = round(float(cTime/1e6 * self.lXtalFrequency/12))
        hold = hold if hold >= 63 else 63
        
        tempRegValue[0] &= 0xC0
        tempRegValue[0] |= hold
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL0_BASE, tempRegValue)
    
    def getAGCHoldTimeUs(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        
        tempRegValue &= 0x3F
        return round((12.0/self.lXtalFrequency)*(tempRegValue[0]*1e6))
    
    def setAGCHoldTime(self, cTime):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        
        tempRegValue[0] &= 0xC0
        tempRegValue[0] |= cTime
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL0_BASE, tempRegValue)
        
    def getAGCHoldTime(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL0_BASE)
        return tempRegValue[0]&0x3F
    
    def setAGCHighThreshold(self, cHighThreshold):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL1_BASE)
        
        tempRegValue[0] &= 0x0F
        tempRegValue[0] |= cHighThreshold<<4
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL1_BASE, tempRegValue)
    
    def getAGCHighThreshold(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL1_BASE)
        return (tempRegValue[0]&0xF0)>>4
    
    def setAGCLowThreshold(self, cLowThreshold):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL1_BASE)
        
        tempRegValue[0] &= 0xF0
        tempRegValue[0] |= cLowThreshold
        
        self.spirit.spi.writeRegisters(spirit_regs.AGCCTRL1_BASE, tempRegValue)
    
    def getAGCLowThreshold(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.AGCCTRL1_BASE)
        
        return (tempRegValue[0] & 0x0F)
    
    def setClkRecMode(self, xMode):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.FDEV0_BASE)
        
        tempRegValue[0] &= 0xF7
        tempRegValue[0] |= int(xMode)
        
        self.spirit.spi.writeRegisters(spirit_regs.FDEV0_BASE, tempRegValue)
    
    def getClkRecMode(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.FDEV0_BASE)
        
        return tempRegValue[0] & 0x08
    
    def setClkRecPGain(self, cPGain):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CLOCKREC_BASE)
        
        tempRegValue[0] &= 0x1F
        tempRegValue[0] |= (cPGain<<5)
        
        self.spirit.spi.writeRegisters(spirit_regs.CLOCKREC_BASE, tempRegValue)
    
    def getClkRecPGain(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CLOCKREC_BASE)
        
        return (tempRegValue[0]&0xEF)>>5
    
    def setClkRecIGain(self, cIGain):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CLOCKREC_BASE)
        
        tempRegValue[0] &= 0xF0
        tempRegValue[0] |= cIGain
        
        self.spirit.spi.writeRegisters(spirit_regs.CLOCKREC_BASE, tempRegValue)
    
    def getClkRecIGain(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CLOCKREC_BASE)
        
        return (tempRegValue[0] & 0x0F)
    
    def setClkRecPstFltLength(self, xLength):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CLOCKREC_BASE)
        
        tempRegValue[0] & 0xEF
        tempRegValue[0] |= xLength
        
        self.spirit.spi.writeRegisters(spirit_regs.CLOCKREC_BASE, tempRegValue)
    
    def getClkRecPstFltLength(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.CLOCKREC_BASE)
        
        return tempRegValue[0]&0x10
    
    def enableCsBlanking(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.ANT_SELECT_CONF_BASE)
        
        if xNewState:
            tempRegValue[0] |= spirit_regs.ANT_SELECT_CS_BLANKING_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.ANT_SELECT_CS_BLANKING_MASK)
            
        self.spirit.spi.writeRegisters(spirit_regs.ANT_SELECT_CONF_BASE, tempRegValue)
    
    def enablePersistentRx(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.PROTOCOL0_BASE)
        
        if xNewState:
            tempRegValue[0] |= spirit_regs.PROTOCOL0_PERS_RX_MASK
        else:
            tempRegValue[0] &= (~spirit_regs.PROTOCOL0_PERS_RX_MASK)
            
        self.spirit.spi.writeRegisters(spirit_regs.PROTOCOL0_BASE, tempRegValue)
    
    def getXtalFrequency(self):
        return self.lXtalFrequency
    
    def setXtalFrequency(self, lXtalFrequency):
        self.lXtalFrequency = lXtalFrequency
    
    def setRefDiv(self, xNewState):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
        
        if xNewState:
            tempRegValue[0] |= 0x80
        else:
            tempRegValue[0] &= 0x7F
            
        self.spirit.spi.writeRegisters(spirit_regs.SYNTH_CONFIG1_BASE, tempRegValue)
    
    def getRefDiv(self):
        tempRegValue = self.spirit.spi.readRegisters(spirit_regs.SYNTH_CONFIG1_BASE)
        
        cRefDiv = ((tempRegValue[0]>>7)&0x1)
        return cRefDiv
