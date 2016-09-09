

class AES:
    def __init__(self, spirit):
        """
        @param spirit: SPIRIT1 object
        """
        self.spirit = spirit
        self.enable()
        
    def _cmdEncrypt(self):
        """Start the encryption routine
        """
        buff = bytearray([COMMAND_BYTE, 0x6A])
        self.spirit.SPIobj.send_recv(buff)
        
    def _cmdKey(self):
        """Start the procedure to compute the key
        for decryption
        """
        buff = bytearray([COMMAND_BYTE, 0x6B])
        self.spirit.SPIobj.send_recv(buff)
        
    def _cmdDecrypt(self):
        """Start decryption using current key
        """
        buff = bytearray([COMMAND_BYTE, 0x6C])
        self.spirit.SPIobj.send_recv(buff)
        
    def _cmdKeyDecrypt(self):
        """Compute the key and start
        decryption
        """
        buff = bytearray([COMMAND_BYTE, 0x6D])
        self.spirit.SPIobj.send_recv(buff)
        
    def enable(self):
        """enables AES within the config registers
        """
        reg = self.spirit.getRegister("ANA_FUNC_CONF[0]")
        val = reg.read()
        newval = setBitPos(val, 5, 1)
        reg.write(newval)
        
    def disable(self):
        """disables AES within the config registers
        """
        reg = self.spirit.getRegister("ANA_FUNC_CONF[0]")
        val = reg.read()
        newval = setBitPos(val, 5, 0)
        reg.write(newval)
        
    def encryptData(self, data, encryptionKey):
        """Encryption using a given encryption key.
        @param data: string to be encoded, must be 16 bytes or less
        @param encryptionKey: 128 bit string
        @return decryptedData: data parameter encrypted with given encryption key
        """
        dataEncoded = bytearray(data)
        if len(dataEncoded) < 16:
            dataEncoded = bytearray([0 for _ in range(16 - len(dataEncoded))]) + dataEncoded
        elif len(dataEncoded) > 16:
            raise TypeError("data too big, must be 16 bytes max")
        
        self.spirit.writeRegister("AES_KEY_IN[15]", bytearray(encryptionKey))
        self.spirit.writeRegister("AES_DATA_IN[15]", dataEncoded)
        
        print(self.spirit.readRegister("AES_KEY_IN[15]", 16))
        print(self.spirit.readRegister("AES_DATA_IN[15]", 16))
        
        pyb.enable_irq()
        self._cmdEncrypt()
#         pyb.wfi()
#         pyb.disable_irq()
        return self.spirit.readRegister("AES_DATA_OUT[15]", 16)#.decode("UTF-8")
    
    def getDecryptionKey(self, encryptionKey):
        """Decryption key derivation starting from an encryption key.
        @param encryptionKey: 128 bit string
        @return decryptionKey: decryption key corresponding to given encryption key
        """
        self.spirit.writeRegister("AES_DATA_IN[15]", bytearray(encryptionKey))
        pyb.enable_irq()
        self._cmdKey()
#         pyb.wfi()
#         pyb.disable_irq()
        return self.spirit.readRegister("AES_DATA_OUT[15]", 16)#.decode("UTF-8")
    
    def decryptData(self, data, decryptionKey):
        """Data decryption using a decryption key.
        @param data: string to be decrypted, must be 16 bytes or less
        @param decryptionKey: 128 bit decryption key
        @return decrypted Data
        """
        dataEncoded = bytearray(data)
        while len(dataEncoded) < 16:
            dataEncoded.insert(0, 0x00)
        if len(dataEncoded) > 16:
            raise TypeError
        
        self.spirit.writeRegister("AES_KEY_IN[15]", bytearray(decryptionKey))
        self.spirit.writeRegister("AES_DATA_IN[15]", dataEncoded)
        pyb.enable_irq()
        self._cmdDecrypt()
#         pyb.wfi()
#         pyb.disable_irq()
        return self.spirit.readRegister("AES_DATA_OUT[15]", 16)#.decode("UTF-8")
    
    def decryptDataKey(self, data, encryptionKey):
        """Data decryption using a decryption key derived from an encryption key.
        @param data: string to be decrypted, must be 16 bytes or less
        @param encryptionKey: 128 bit encryption key
        @return decrypted Data
        """
        dataEncoded = bytearray(data)
        while len(dataEncoded) < 16:
            dataEncoded.insert(0, 0x00)
        if len(dataEncoded) > 16:
            raise TypeError
        
        self.spirit.writeRegister("AES_KEY_IN[15]", bytearray(encryptionKey))
        self.spirit.writeRegister("AES_DATA_IN[15]", dataEncoded)
        pyb.enable_irq()
        self._cmdKeyDecrypt()
#         pyb.wfi()
#         pyb.disable_irq()
        return self.spirit.readRegister("AES_DATA_OUT[15]", 16)#.decode("UTF-8")
