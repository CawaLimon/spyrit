import spirit_regs

#TIMEOUT STOP CONDITIONS
NO_TIMEOUT_STOP = 0x00
TIMEOUT_ALWAYS_STOPPED = 0x08
RSSI_ABOVE_THRESHOLD = 0x04
SQI_ABOVE_THRESHOLD = 0x02
PQI_ABOVE_THRESHOLD = 0x01
RSSI_AND_SQI_ABOVE_THRESHOLD = 0x06
SQI_AND_PQI_ABOVE_THRESHOLD = 0x03
ALL_ABOVE_THRESHOLD = 0x07
RSSI_OR_SQI_ABOVE_THRESHOLD = 0x0E
RSSI_OR_SQI_ABOVE_THRESHOLD = 0x0D
SQI_OR_PQI_ABOVE_THRESHOLD = 0x0B
ANY_ABOVE_THRESHOLD = 0x0F

RX_TCLK_24_MHz = 50.417
RX_TCLK_26_MHz = 46.538
WAKEUP_TCLK = 28.818

class Timer:
    def __init__(self, spi):
        self.spi = spi
        
    def enableLdcrMode(self, xNewState):
        tempRegValue = self.spi.readRegisters(spirit_regs.PROTOCOL2_BASE)
        
        if xNewState:
            tempRegValue[0] |= spirit_regs.PROTOCOL2_LDC_MODE_MASK
        else:
            tempRegValue[0] &= ~spirit_regs.PROTOCOL2_LDC_MODE_MASK
            
        self.spi.writeRegisters(spirit_regs.PROTOCOL2_BASE, tempRegValue)
        
    def enableLdcrAutoReload(self, xNewState):
        tempRegValue = self.spi.readRegisters(spirit_regs.PROTOCOL1_BASE)
        
        if xNewState:
            tempRegValue[0] |= spirit_regs.PROTOCOL1_LDC_RELOAD_ON_SYNC_MASK
        else:
            tempRegValue[0] &= ~spirit_regs.PROTOCOL1_LDC_RELOAD_ON_SYNC_MASK
            
        self.spi.writeRegisters(spirit_regs.PROTOCOL1_BASE, tempRegValue)
        
    def getLdcrAutoReload(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.PROTOCOL1_BASE)
        
        return tempRegValue[0]&0x80
    
    def setRxTimeout(self, cCounter, cPrescaler):
        tempRegValue = bytearray([cPrescaler, cCounter])
        self.spi.writeRegisters(spirit_regs.TIMERS5_RX_TIMEOUT_PRESCALER_BASE, tempRegValue)
        
    def setRxTimeoutMs(self, fDesiredMsec):
        
        tempRegValue = self.computeRxTimeoutValues(fDesiredMsec)
        
        self.spi.writeRegisters(spirit_regs.TIMERS5_RX_TIMEOUT_PRESCALER_BASE, tempRegValue)
        
    def setRxTimeoutCounter(self, cCounter):
        self.spi.writeRegisters(spirit_regs.TIMERS4_RX_TIMEOUT_COUNTER_BASE, bytearray([cCounter]))
        
    def setRxTimeoutPrescaler(self, cPrescaler):
        self.spi.writeRegisters(spirit_regs.TIMERS5_RX_TIMEOUT_PRESCALER_BASE, bytearray([cPrescaler]))
        
    def getRxTimeout(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.TIMERS5_RX_TIMEOUT_PRESCALER_BASE, 2)
        xtal = self.spi.readRegisters(spirit_regs.ANA_FUNC_CONF0_BASE)[0]
        
        pcPrescaler = tempRegValue[0]
        pcCounter = tempRegValue[0]
        
        if (xtal & 0x40) == spirit_regs.SELECT_24_26_MHZ_MASK:
            pfTimeoutMsec = (float(tempRegValue[0]+1)*tempRegValue[1]+1)*float(RX_TCLK_26_MHz/1000)
        else:
            pfTimeoutMsec = (float(tempRegValue[0]+1)*tempRegValue[1]+1)*float(RX_TCLK_24_MHz/1000)
            
        return pcPrescaler, pcCounter, pfTimeoutMsec
    
    def setWakeUpTimer(self, cCounter, cPrescaler):
        tempRegValue = bytearray([cPrescaler, cCounter])
        self.spi.writeRegisters(spirit_regs.TIMERS3_LDC_PRESCALER_BASE, tempRegValue)
        
    def setWakeUpTimerMs(self, fDesiredMsec):
        tempRegValue = self.computeWakeUpValues(fDesiredMsec)
        self.spi.writeRegisters(spirit_regs.TIMERS3_LDC_PRESCALER_BASE, tempRegValue)
        
    def setWakeUpTimerCounter(self, cCounter):
        self.spi.writeRegisters(spirit_regs.TIMERS2_LDC_COUNTER_BASE, bytearray([cCounter]))
        
    def setWakeUpTimerPrescaler(self, cPrescaler):
        self.spi.writeRegisters(spirit_regs.TIMERS3_LDC_PRESCALER_BASE, cPrescaler)
        
    def getWakeUpTimer(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.TIMERS3_LDC_PRESCALER_BASE, 2)
        
        pcPrescaler = tempRegValue[0]
        pcCounter = tempRegValue[1]
        pfWakeUpMsec = float((pcPrescaler+1)*(pcCounter+1))*float(WAKEUP_TCLK/1000)
        
        return pcPrescaler, pcCounter, pfWakeUpMsec
        
    def setWakeUpTimerReload(self, cCounter, cPrescaler):
        tempRegValue = bytearray([cPrescaler, cCounter])
        
        self.spi.writeRegisters(spirit_regs.TIMERS1_LDC_RELOAD_PRESCALER_BASE, tempRegValue)
        
    def setWakeUpTimerReloadMs(self, fDesiredMsec):
        tempRegValue = self.computeWakeUpValues(fDesiredMsec)
        
        self.spi.writeRegisters(spirit_regs.TIMERS1_LDC_RELOAD_PRESCALER_BASE, tempRegValue)
        
    def setWakeUpTimerReloadPrescaler(self, cPrescaler):
        self.spi.writeRegisters(spirit_regs.TIMERS1_LDC_RELOAD_PRESCALER_BASE, bytearray([cPrescaler]))
        
    def getWakeUpTimerReload(self):
        tempRegValue = self.spi.readRegisters(spirit_regs.TIMERS1_LDC_RELOAD_PRESCALER_BASE, 2)
        
        pcPrescaler = tempRegValue[0]
        pcCounter = tempRegValue[1]
        
        pfWakeUpReloadMsec = float((pcPrescaler+1)*(pcCounter+1))*float(WAKEUP_TCLK/1000)
        return pcPrescaler, pcCounter, pfWakeUpReloadMsec
    
    def computeWakeUpValues(self, fDesiredMsec):
        n = (fDesiredMsec*1000)/WAKEUP_TCLK
        err_min = n
        
        pcPrescaler, a0 = (n/0xFF)+1
        pcCounter, b0 = (n / pcPrescaler)
        pcPrescaler -= 1
        
        if fDesiredMsec > 1888.0:
            pcCounter = 0xFF
            pcPrescaler = 0xFF
            return bytearray([pcPrescaler, pcCounter])
            
        while True:
            pcCounter = ((n/(pcPrescaler+1))-1)
            err = ((int(pcPrescaler)+1)) * (int(pcCounter)+1) - int(n)
            if abs(err) > (pcPrescaler / 2):
                pcCounter += 1
                err = (int(pcPrescaler)+1) * (int(pcCounter)+1) - int(n)
            if abs(err) < abs(err_min):
                err_min = err
                a0 = pcPrescaler
                b0 = pcCounter
                if err == 0:
                    break
            if pcPrescaler == 0xFF:
                break
            pcPrescaler += 1
        
        pcPrescaler = a0
        pcCounter = b0
        
        return bytearray([pcPrescaler, pcCounter])
    
    def computeRxTimeoutValues(self, fDesiredMsec):
        xtal = self.spirit.readRegisters(spirit_regs.ANA_FUNC_CONF0_BASE)[0]
        
        if xtal & 0x40 == spirit_regs.SELECT_24_26_MHZ_MASK:
            if fDesiredMsec > 3026.0:
                pcCounter = 0xFF
                pcPrescaler = 0xFF
                return bytearray([pcPrescaler, pcCounter])
            n = int((fDesiredMsec*1000)/RX_TCLK_26_MHz)
        else:
            if fDesiredMsec > 3278.0:
                pcCounter = 0xFF
                pcPrescaler = 0xFF
                return bytearray([pcPrescaler, pcCounter])
            n = int((fDesiredMsec*1000)/RX_TCLK_24_MHz)
        
        err_min = n
        
        pcPrescaler, a0 = ((n-1)/0xFF) + 1
        pcCounter, b0 = (n/pcPrescaler)
        
        while True:
            pcCounter = n / pcPrescaler
            err = 1 + (int(pcPrescaler)+1) * int(pcCounter) - int(n)
            if abs(err) > pcPrescaler / 2:
                pcCounter += 1
                err = 1 + int(pcPrescaler + 1) * int(pcCounter) - int(n)
            if abs(err) < abs(err_min):
                err_min = err
                a0 = pcPrescaler
                b0 = pcCounter
                if err == 0:
                    break
            if pcPrescaler == 0xFF:
                break
            pcPrescaler += 1
        
        pcPrescaler = a0
        pcCounter = b0
        return bytearray([pcPrescaler, pcCounter])
    
    def setRxTimeoutStopCondition(self, xStopCondition):
        tempRegValue = self.spi.readRegisters(spirit_regs.PCKT_FLT_OPTIONS_BASE, 2)
        
        tempRegValue[0] &= 0xBF
        tempRegValue[1] |= ((xStopCondition & 0x08) << 3)
        
        tempRegValue[1] &= 0x1F
        tempRegValue[1] |= (xStopCondition << 5)
        
        self.spi.writeRegisters(spirit_regs.PCKT_FLT_OPTIONS_BASE, tempRegValue)
        
    def reloadStrobe(self):
        self.spi.commandStrobes(spirit_regs.COMMAND_LDC_RELOAD)
            