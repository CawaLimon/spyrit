import spirit_regs

CMD_TX = spirit_regs.COMMAND_TX
CMD_RX = spirit_regs.COMMAND_RX
CMD_READY = spirit_regs.COMMAND_READY
CMD_STANDBY = spirit_regs.COMMAND_STANDBY
CMD_SLEEP = spirit_regs.COMMAND_SLEEP
CMD_LOCKRX = spirit_regs.COMMAND_LOCKRX
CMD_LOCKTX = spirit_regs.COMMAND_LOCKTX
CMD_SABORT = spirit_regs.COMMAND_SABORT
CMD_LDC_RELOAD = spirit_regs.COMMAND_LDC_RELOAD
CMD_SEQUENCE_UPDATE = spirit_regs.COMMAND_SEQUENCE_UPDATE
CMD_AES_ENC = spirit_regs.COMMAND_AES_ENC
CMD_AES_KEY = spirit_regs.COMMAND_AES_KEY
CMD_AES_DEC = spirit_regs.COMMAND_AES_DEC
CMD_AES_KEY_DEC = spirit_regs.COMMAND_AES_KEY_DEC
CMD_IQC_INIT_LOAD = spirit_regs.COMMAND_IQC_INIT_LOAD
CMD_SRES = spirit_regs.COMMAND_SRES
CMD_FLUSHRXFIFO = spirit_regs.COMMAND_FLUSHRXFIFO
CMD_FLUSHTXFIFO = spirit_regs.COMMAND_FLUSHTXFIFO

class Command:
    def __init__(self, spi):
        self.spi = spi
    
    def strobeRx(self):
        self.spi.commandStrobes(CMD_RX)
        
    def strobeTx(self):
        self.spi.commandStrobes(CMD_TX)
        
    def strobeReady(self):
        self.spi.commandStrobes(CMD_READY)
        
    def strobeStandby(self):
        self.spi.commandStrobes(CMD_STANDBY)
        
    def strobeSleep(self):
        self.spi.commandStrobes(CMD_SLEEP)
        
    def strobeLockRx(self):
        self.spi.commandStrobes(CMD_LOCKRX)
        
    def strobeLockTx(self):
        self.spi.commandStrobes(CMD_LOCKTX)
        
    def strobeSabort(self):
        self.spi.commandStrobes(CMD_SABORT)
        
    def strobeLdcReload(self):
        self.spi.commandStrobes(CMD_LDC_RELOAD)
        
    def strobeSequenceUpdates(self):
        self.spi.commandStrobes(CMD_SEQUENCE_UPDATE)
        
    def strobeAesEnc(self):
        self.spi.commandStrobes(CMD_AES_ENC)
        
    def strobeAesKey(self):
        self.spi.commandStrobes(CMD_AES_KEY)
        
    def strobeAesDec(self):
        self.spi.commandStrobes(CMD_AES_DEC)
        
    def strobeAesKeyDec(self):
        self.spi.commandStrobes(CMD_AES_KEY_DEC)
        
    def strobeIqcInitLoad(self):
        self.spi.commandStrobes(CMD_IQC_INIT_LOAD)
        
    def strobeSres(self):
        self.spi.commandStrobes(CMD_SRES)
        
    def strobeFlushRxFifo(self):
        self.spi.commandStrobes(CMD_FLUSHRXFIFO)
        
    def strobeFlushTxFifo(self):
        self.spi.commandStrobes(CMD_FLUSHTXFIFO)
        
    def strobeCommand(self, xCommandCode):
        self.spi.commandStrobes(xCommandCode)