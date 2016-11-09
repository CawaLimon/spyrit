from PyQt4 import QtGui
from PyQt4 import QtCore

import sys
import collections

def lowestSet(int_type):
    low = (int_type & -int_type)
    lowBit = -1
    while (low):
        low >>= 1
        lowBit += 1
    return(lowBit)

def bitLenCount(int_type):
    length = 0
    count = 0
    while (int_type):
        count += (int_type & 1)
        length += 1
        int_type >>= 1
    return(length, count)

def testBit(int_type, offset):
    mask = 1 << offset
    return (int_type & mask)

class HexStandardItem(QtGui.QStandardItem):
    def setText(self, text):
        if text == self.text():
            self.setForeground(QtGui.QBrush(QtGui.QColor('black')))
        else:
            text = '0x%X' % int(str(text))
            if len(text) < 4:
                text = text[:2] + "0" + text[2]
            QtGui.QStandardItem.setText(self, text)
            self.setForeground(QtGui.QBrush(QtGui.QColor('red')))
            self.emitDataChanged()
        
    def text(self):
        text = QtGui.QStandardItem.text(self)
        return int(str(text), 16) if text != '' else ''

class Register:
    def __init__(self, name, address, default, fieldDict, parent=None):
        self.name = QtGui.QStandardItem(name)
        self.address = HexStandardItem()
        self.address.setText(address)
        self.address.setForeground(QtGui.QBrush(QtGui.QColor('black')))
        self.default = HexStandardItem()
        self.default.setText(default)
        self.default.setForeground(QtGui.QBrush(QtGui.QColor('black')))
        self.value = HexStandardItem()
        self.value.setText(default)
        self.value.setForeground(QtGui.QBrush(QtGui.QColor('black')))
        
        self.fields = []
        for key in fieldDict.keys():
            self.fields.append(RegisterField(key, fieldDict[key], self))
        self.fields = sorted(self.fields, key=lambda field: field.lsb)
        self.fields.reverse()
        for field in self.fields:
            self.address.appendRow(field.getRowItems())
            
        self.rowItems = []
        self.rowItems.append(self.address)
        self.rowItems.append(self.name)
        self.rowItems.append(self.value)
        self.rowItems.append(self.default)
        
    def getRowItems(self):
        return self.rowItems
    
    def getAddress(self):
        return self.address.data()
    
    def setValue(self, value):
        self.value.setText(value)
        for field in self.fields:
            field.updateValue()
        
class RegisterField:
    def __init__(self, name, bitRange, parent):
        self.parent = parent
        self.name = QtGui.QStandardItem(name)
        self.name.setEditable(False)
        self.mask = 0
        if type(bitRange) == list:
            count = bitRange[0]
            while count >= bitRange[1]:
                bitMask = 1 << count
                self.mask |= bitMask
                count -= 1
            self.lsb = bitRange[1]
            self.rangeLabel = QtGui.QStandardItem(":".join([str(i) for i in bitRange]))
        else:
            self.mask |= 1 << bitRange
            self.lsb = bitRange
            self.rangeLabel = QtGui.QStandardItem(str(bitRange))
        self.value = HexStandardItem()
        self.value.setText((self.parent.value.text()&self.mask) >> self.lsb)
        self.value.setForeground(QtGui.QBrush(QtGui.QColor('black')))
        self.default = HexStandardItem()
        self.default.setText((self.parent.default.text()&self.mask) >> self.lsb)
        self.default.setForeground(QtGui.QBrush(QtGui.QColor('black')))
            
        self.rowItems = []
        self.rowItems.append(self.rangeLabel)
        self.rowItems.append(self.name)
        self.rowItems.append(self.value)
        self.rowItems.append(self.default)
        
    def getRowItems(self):
        return self.rowItems
    
    def updateValue(self):
        self.value.setText((self.parent.value.text()&self.mask) >> self.lsb)
        
class RegisterModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(RegisterModel, self).__init__(parent)
        self.parent = parent
        self.registers = collections.OrderedDict()
        self.registers[0x00] = Register("ANA_FUNC_CONF[1]", 0x00, 0b00001100, {"Reserved":[7,5],
                                                                        "GM_CONF[2:0]":[4,2],
                                                                        "SET_BLD_LVL[1:0]":[1,0]})
        self.registers[0x01] = Register("ANA_FUNC_CONF[0]", 0x01, 0b11000000, {"Reserved ":7,
                                                                       "24_26_MHz_SELECT":6,
                                                                       "AES_ON":5,
                                                                       "EXT_REF":4,
                                                                       "Reserved":3,
                                                                       "BROWN_OUT":2,
                                                                       "BATTERY_LEVEL":1,
                                                                       "TS":0})
        
        self.registers[0x02] = Register("GPIO3_CONF", 0x02, 0b10100010, {"GPIO_SELECT[4:0]":[7,3],
                                                                         "Reserved":0,
                                                                         "GPIO_MODE[1:0]":[1,0]})
        self.registers[0x03] = Register("GPIO2_CONF", 0x03, 0b10100010, {"GPIO_SELECT[4:0]":[7,3],
                                                                         "Reserved":0,
                                                                         "GPIO_MODE[1:0]":[1,0]})
        self.registers[0x04] = Register("GPIO1_CONF", 0x04, 0b10100010, {"GPIO_SELECT[4:0]":[7,3],
                                                                         "Reserved":0,
                                                                         "GPIO_MODE[1:0]":[1,0]})
        self.registers[0x05] = Register("GPIO0_CONF", 0x05, 0b00001010, {"GPIO_SELECT[4:0]":[7,3],
                                                                         "Reserved":0,
                                                                         "GPIO_MODE[1:0]":[1,0]})
        self.registers[0x06] = Register("MCU_CK_CONF", 0x06, 0, {"EN_MCU_CLK":7,
                                                                 "CLOCK_TAIL[1:0]":[6,5],
                                                                 "XO_RATIO[3:0]":[4,1],
                                                                 "RCO_RATIO":0})
        self.registers[0x07] = Register("IF_OFFSET_ANA", 0x07, 0xA3, {"IF_OFFSET_ANA":[7,0]})
        self.registers[0x08] = Register("SYNT3", 0x08, 0x0C, {"WCP":[7,5],
                                                              "SYNT[25:21]":[4,0]})
        self.registers[0x09] = Register("SYNT2", 0x09, 0x84, {"SYNT[20:13]":[7,0]})
        self.registers[0x0A] = Register("SYNT1", 0x0A, 0xEC, {"SYNT[12:5]":[7,0]})
        self.registers[0x0B] = Register("SYNT0", 0x0B, 0x51, {"SYNT[4:0]":[7,3],
                                                              "BS":[2,0]})
        self.registers[0x0C] = Register("CH_SPACE", 0x0C, 0xFC, {"CH_SPACING[7:0]":[7,0]})
        self.registers[0x0D] = Register("IF_OFFSET_DIG", 0x0D, 0xA3, {"IF_OFFSET_DIG":[7,0]})
        self.registers[0x0E] = Register("FC_OFFSET[1]", 0x0E, 0, {"Reserved":[7,4],
                                                               "FC_OFFSET":[3,0]})
        self.registers[0x0F] = Register("FC_OFFEST[0]", 0x0F, 0, {"FC_OFFSET":[7,0]})
        self.registers[0x10] = Register("PA_POWER[8]", 0x10, 0x03, {"Reserved":7,
                                                                    "PA_LEVEL_7":[6,0]})
        self.registers[0x11] = Register("PA_POWER[7]", 0x11, 0x0E, {"Reserved":7,
                                                                    "PA_LEVEL_6":[6,0]})
        self.registers[0x12] = Register("PA_POWER[6]", 0x12, 0x1A, {"Reserved":7,
                                                                    "PA_LEVEL_5":[6,0]})
        self.registers[0x13] = Register("PA_POWER[5]", 0x13, 0x25, {"Reserved":7,
                                                                    "PA_LEVEL_4":[6,0]})
        self.registers[0x14] = Register("PA_POWER[4]", 0x14, 0x35, {"Reserved":7,
                                                                    "PA_LEVEL_3":[6,0]})
        self.registers[0x15] = Register("PA_POWER[3]", 0x15, 0x40, {"Reserved":7,
                                                                    "PA_LEVEL_2":[6,0]})
        self.registers[0x16] = Register("PA_POWER[2]", 0x16, 0x4E, {"Reserved":7,
                                                                    "PA_LEVEL_1":[6,0]})
        self.registers[0x17] = Register("PA_POWER[1]", 0x17, 0, {"Reserved":7,
                                                                 "PA_LEVEL_0":[6,0]})
        self.registers[0x18] = Register("PA_POWER[0]", 0x18, 0x07, {"CWC":[7,6],
                                                                    "PA_RAMP_ENABLE":5,
                                                                    "PA_RAMP_STEP_WIDTH":[4,3],
                                                                    "PA_LEVEL_MAX_INDEX":[2,0]})
        self.registers[0x1A] = Register("MOD1", 0x1A, 0x83, {"DATARATE_M[7:0]":[7,0]})
        self.registers[0x1B] = Register("MOD0", 0x1B, 0x1A, {"CW":7,
                                                             "BT_SEL":6,
                                                             "MOD_TYPE":[5,4],
                                                             "DATARATE_E":[3,0]})
        self.registers[0x1C] = Register("FDEV0", 0x1C, 0x45, {"FDEV_E":[7,4],
                                                              "CLOCK_REC_ALGO_SEL":3,
                                                              "FDEV_M":[2,0]})
        self.registers[0x1D] = Register("CHFLT", 0x1D, 0x23, {"CHFLT_M":[7,4],
                                                              "CHFLT_E":[3,0]})
        self.registers[0x1E] = Register("AFC2", 0x1E, 0x48, {"AFC_FREEZE_ON_SYNC":7,
                                                             "AFC_ENABLED":6,
                                                             "AFC_MODE":5,
                                                             "AFC_PD_LEAKAGE":[4,0]})
        self.registers[0x1F] = Register("AFC1", 0x1F, 0x18, {"AFC_FAST_PERIOD":[7,0]})
        self.registers[0x20] = Register("AFC0", 0x20, 0x25, {"AFC_FAST_GAIN_LOG2[3:0]":[7,4],
                                                             "AFC_SLOW_GAIN_LOG2[3:0]":[3,0]})
        self.registers[0x21] = Register("RSSI_FLT", 0x21, 0xE3, {"RSSI_FLT":[7,4],
                                                                 "CS_MODE":[3,2],
                                                                 "OOK_PEAK_DECAY":[1,0]})
        self.registers[0x22] = Register("RSSI_TH", 0x22, 0x24, {"RSSI_THRESHOLD":[7,0]})
        self.registers[0x23] = Register("CLOCKREC", 0x23, 0x58, {"CLOCK_REC_P_GAIN[2:0]":[7,5],
                                                                 "PSTFLT_LEN":4,
                                                                 "CLOCK_REC_I_GAIN[3:0]":[3,0]})
        self.registers[0x24] = Register("AGCCTRL2", 0x24, 0x22, {"Reserved":[7,4],
                                                                 "MEAS_TIME":[3,0]})
        self.registers[0x25] = Register("AGCCTRL1", 0x25, 0x65, {"THRESHOLD_HIGH[3:0]":[7,4],
                                                                 "THRESHOLD_LOW[3:0]":[3,0]})
        self.registers[0x26] = Register("AGCCTRL0", 0x26, 0x8A, {"AGC_ENABLE":7,
                                                                 "Reserved":[7,0]})
        self.registers[0x27] = Register("ANT_SELECT_CONF", 0x27, 0x05, {"Reserved":[7,5],
                                                                        "CS_BLANKING":4,
                                                                        "AS_ENABLE":3,
                                                                        "AS_MEAS_TIME":[2,0]})
        self.registers[0x30] = Register("PCKTCTRL4", 0x30, 0, {"Reserved":[7,5],
                                                               "ADDRESS_LEN":[4,3],
                                                               "CONTROL_LEN":[2,0]})
        self.registers[0x31] = Register("PCKTCTRL3", 0x31, 0x07, {"PCKT_FRMT":[7,6],
                                                                  "RX_MODE":[5,4],
                                                                  "LEN_WID":[3,0]})
        self.registers[0x32] = Register("PCKTCTRL2", 0x32, 0x1E, {"PREAMBLE_LENGTH":[7,3],
                                                                  "SYNC_LENGTH":[2,1],
                                                                  "FIX_VAR_LEN":0})
        self.registers[0x33] = Register("PCKTCTRL1", 0x33, 0x20, {"CRC_MODE":[7,5],
                                                                  "WHIT_EN":4,
                                                                  "TXSOURCE":[3,2],
                                                                  "Reserved":1,
                                                                  "FEC_EN":0})
        self.registers[0x34] = Register("PCKTLEN1", 0x34, 0, {"PCKTLEN1":[7,0]})
        self.registers[0x35] = Register("PCKTLEN0", 0x35, 0x14, {"PCKTLEN0":[7,0]})
        self.registers[0x36] = Register("SYNC4", 0x36, 0x88, {"SYNC4":[7,0]})
        self.registers[0x37] = Register("SYNC3", 0x37, 0x88, {"SYNC3":[7,0]})
        self.registers[0x38] = Register("SYNC2", 0x38, 0x88, {"SYNC2":[7,0]})
        self.registers[0x39] = Register("SYNC1", 0x39, 0x88, {"SYNC1":[7,0]})
        self.registers[0x3A] = Register("QI", 0x3A, 0x02, {"SQI_TH":[7,6],
                                                           "PQI_TH":[5,2],
                                                           "SQI_EN":1,
                                                           "PQI_EN":0})
        self.registers[0x3B] = Register("MBUS_PRMBL", 0x3B, 0x20, {"MBUS_PRMBL[7:0]":[7,0]})
        self.registers[0x3C] = Register("MBUS_PSTMBL", 0x3C, 0x20, {"MUBS_PSTMBL[7:0]":[7,0]})
        self.registers[0x3D] = Register("MBUS_CTRL", 0x3D, 0, {"Reserved":[7,4],
                                                               "MBUS_SUBMODE[2:0]":[3,1],
                                                               "Reserved ":0})
        self.registers[0x3E] = Register("FIFO_CONFIG[3]", 0x3E, 0x30, {"Reserved":7,
                                                                       "RXAFTHR[6:0]":[6,0]})
        self.registers[0x3F] = Register("FIFO_CONFIG[2]", 0x3F, 0x30, {"Reserved":7,
                                                                       "RXAETHR[6:0]":[6,0]})
        self.registers[0x40] = Register("FIFO_CONFIG[1]", 0x40, 0x30, {"Reserved":7,
                                                                       "TXAFTHR[6:0]":[6,0]})
        self.registers[0x41] = Register("FIFO_CONFIG[0]", 0x41, 0x30, {"Reserved":7,
                                                                       "TXAETHR[6:0]":[6,0]})
        self.registers[0x42] = Register("PCKT_FLT_GOALS[12]", 0x42, 0, {"CONTROL0_MASK":[7,0]})
        self.registers[0x43] = Register("PCKT_FLT_GOALS[11]", 0x43, 0, {"CONTROL1_MASK":[7,0]})
        self.registers[0x44] = Register("PCKT_FLT_GOALS[10]", 0x44, 0, {"CONTROL2_MASK":[7,0]})
        self.registers[0x45] = Register("PCKT_FLT_GOALS[9]", 0x45, 0, {"CONTROL3_MASK":[7,0]})
        self.registers[0x46] = Register("PCKT_FLT_GOALS[8]", 0x46, 0, {"CONTROL0_FIELD":[7,0]})
        self.registers[0x47] = Register("PCKT_FLT_GOALS[7]", 0x47, 0, {"CONTROL1_FIELD":[7,0]})
        self.registers[0x48] = Register("PCKT_FLT_GOALS[6]", 0x48, 0, {"CONTROL2_FIELD":[7,0]})
        self.registers[0x49] = Register("PCKT_FLT_GOALS[5]", 0x49, 0, {"CONTROL3_FIELD":[7,0]})
        self.registers[0x4A] = Register("PCKT_FLT_GOALS[4]", 0x4A, 0, {"RX_SOURCE_MASK":[7,0]})
        self.registers[0x4B] = Register("PCKT_FLT_GOALS[3]", 0x4B, 0, {"DESTINATION_ADDR":[7,0]})
        self.registers[0x4C] = Register("PCKT_FLT_GOALS[2]", 0x4C, 0, {"BROADCAST_ADDR":[7,0]})
        self.registers[0x4D] = Register("PCKT_FLT_GOALS[1]", 0x4D, 0, {"MULTICAST_ADDR":[7,0]})
        self.registers[0x4E] = Register("PCKT_FLT_GOALS[0]", 0x4E, 0, {"MY_ADDR":[7,0]})
        self.registers[0x4F] = Register("PCKT_FLT_OPTIONS", 0x4F, 0x70, {"Reserved":7,
                                                                         "RX_TIMEOUT_AND_OR_SELECT":6,
                                                                         "CONTROL_FILTERING":5,
                                                                         "SOURCE_FILTERING":4,
                                                                         "DEST_VS_SOURCE_ADDR":3,
                                                                         "DEST_VS_MULTICAST_ADDR":2,
                                                                         "DEST_VS_BROADCAST_ADDR":1,
                                                                         "CRC_CHECK":0})
        self.registers[0x50] = Register("PROTOCOL[2]", 0x50, 0x02, {"CS_TIMEOUT_MASK":7,
                                                                    "SQI_TIMEOUT_MASK":6,
                                                                    "PQI_TIMEOUT_MASK":5,
                                                                    "TX_SEQ_NUM_RELOAD":[4,3],
                                                                    "RCO_CALIBRATION":2,
                                                                    "VCO_CALIBRATION":1,
                                                                    "LDC_MODE":0})
        self.registers[0x51] = Register("PROTOCOL[1]", 0x51, 0, {"LDC_RELOAD_ON_SYNC":7,
                                                                 "PIGGYBACKING":6,
                                                                 "Reserved":[5,4],
                                                                 "SEED_RELOAD":3,
                                                                 "CSMA_ON":2,
                                                                 "CSMA_PERS_ON":2,
                                                                 "AUTO_PCKT_FLT":0})
        self.registers[0x52] = Register("PROTOCOL[0]", 0x52, 0x08, {"NMAX_RETX":[7,4],
                                                                    "NACK_TX":3,
                                                                    "AUTO_ACK":2,
                                                                    "PERS_RX":1,
                                                                    "PERS_TX":0})
        self.registers[0x53] = Register("TIMERS[5]", 0x53, 0x01, {"RX_TIMEOUT_PRESCALER":[7,0]})
        self.registers[0x54] = Register("TIMERS[4]", 0x54, 0, {"RX_TIMEOUT_COUNTER":[7,0]})
        self.registers[0x55] = Register("TIMERS[3]", 0x55, 1, {"LDC_PRESCALER":[7,0]})
        self.registers[0x56] = Register("TIMERS[2]", 0x56, 0, {"LDC_COUNTER":[7,0]})
        self.registers[0x57] = Register("TIMERS[1]", 0x57, 1, {"LDC_RELOAD_PRESCALER":[7,0]})
        self.registers[0x58] = Register("TIMERS[0]", 0x58, 0, {"LDC_RELOAD_COUNTER":[7,0]})
        self.registers[0x64] = Register("CSMA_CONFIG[3]", 0x64, 0xFF, {"BU_COUNTER_SEED_MSBYTE":[7,0]})
        self.registers[0x65] = Register("CSMA_CONFIG[2]", 0x65, 0, {"BU_COUNTER_SEED_LSBYTE":[7,0]})
        self.registers[0x66] = Register("CSMA_CONFIG[1]", 0x66, 0x04, {"BU_PRESCALER":[7,2],
                                                                       "CCA_PERIOD":[1,0]})
        self.registers[0x67] = Register("CSMA_CONFIG[0]", 0x67, 0, {"CCA_LENGTH":[7,4],
                                                                    "Reserved":3,
                                                                    "NBACKOFF_MAX":[2,0]})
        self.registers[0x68] = Register("TX_CTRL_FIELD[3]", 0x68, 0, {"TX_CTRL3":[7,0]})
        self.registers[0x69] = Register("TX_CTRL_FIELD[2]", 0x69, 0, {"TX_CTRL2":[7,0]})
        self.registers[0x6A] = Register("TX_CTRL_FIELD[1]", 0x6A, 0, {"TX_CTRL1":[7,0]})
        self.registers[0x6B] = Register("TX_CTRL_FIELD[0]", 0x6B, 0, {"TC_CTRl0":[7,0]})
        self.registers[0x6C] = Register("CHNUM", 0x6C, 0, {"CH_NUM[7:0]":[7,0]})
        self.registers[0x6D] = Register("RCO_VCO_CALIBR_IN[2]", 0x6D, 0x70, {"RWT_IN[3:0]":[7,4],
                                                                             "RFB_IN[4:1]":[3,0]})
        self.registers[0x6E] = Register("RCO_VCO_CALIBR_IN[1]", 0x6E, 0x48, {"RFB_IN[0]":7,
                                                                             "VCO_CALIBR_TX":[6,0]})
        self.registers[0x6F] = Register("RCO_VCO_CALIBR_IN[0]", 0x6F, 0x48, {"Reserved":7,
                                                                             "VCO_CALIBR_RX":[6,0]})
        self.registers[0x90] = Register("IRQ_MASK[3]", 0x90, 0, {"INT_MASK[31:24]":[7,0]})
        self.registers[0x91] = Register("IRQ_MASK[2]", 0x91, 0, {"INT_MASK[23:16]":[7,0]})
        self.registers[0x92] = Register("IRQ_MASK[1]", 0x92, 0, {"INT_MASK[15:8]":[7,0]})
        self.registers[0x93] = Register("IRQ_MASK[0]", 0x93, 0, {"INT_MASK[7:0]":[7,0]})
        self.registers[0x9E] = Register("SYNTH_CONFIG[1]", 0x9E, 0x5B, {"REFDIV":7,
                                                                        "Reserved":[6,3],
                                                                        "VCO_L_SEL":2,
                                                                        "VCO_H_SEL":1,
                                                                        "Reserved":0})
        self.registers[0x9F] = Register("SYNTH_CONFIG[0]", 0x9F, 0x20, {"SEL_TSPLIT":7,
                                                                        "Reserved":[6,0]})
        self.registers[0xA1] = Register("VCO_CONFIG", 0xA1, 0x11, {"Reserved":[7,6],
                                                                   "VCO_GEN_CURR":[5,0]})
        self.registers[0xA3] = Register("DEM_CONFIG", 0xA3, 0x37, {"Reserved":[7,2],
                                                                   "DEM_ORDER":1,
                                                                   "Reserved ":0})
        self.registers[0xA4] = Register("PM_CONFIG[2]", 0xA4, 0x0C, {"Reserved":7,
                                                                     "EN_TS_BUFFER":6,
                                                                     "DISABLE_SMPS":5,
                                                                     "Reserved ":4,
                                                                     "SET_SMPS_VTUNE":3,
                                                                     "SET_SMPS_PLLBW":2,
                                                                     "Reserved  ":[1,0]})
        self.registers[0xA5] = Register("PM_CONFIG[1]", 0xA5, 0x20, {"EN_RM":7,
                                                                     "KRM[14:8]":[6,0]})
        self.registers[0xA6] = Register("PM_CONFIG[0]", 0xA6, 0, {"KRM[7:0]":[7,0]})
        self.registers[0xA7] = Register("XO_RCO_CONFIG", 0xA7, 0xE1, {"Reserved":[7,4],
                                                                      "EXT_RCOSC":3,
                                                                      "Reserved ":[2,0]})
        self.registers[0xB4] = Register("XO_RCO_TEST", 0xB4, 0x21, {"Reserved":[7,4],
                                                                    "PD_CLKDIV":3,
                                                                    "Reserved ":[2,0]})
        self.registers[0xC0] = Register("MC_STATE[1]", 0xC0, 0x50, {"Reserved":[7,4],
                                                                    "ANT_SELECT":3,
                                                                    "TX_FIFO_FULL":2,
                                                                    "RX_FIFO_EMPTY":1,
                                                                    "ERROR_LOCK":0})
        self.registers[0xC1] = Register("MC_STATE[0]", 0xC1, 0, {"STATE[6:0]":[7,1],
                                                                 "XO_ON":0})
        self.registers[0xC2] = Register("TX_PCKT_INFO", 0xC2, 0, {"Reserved":[7,6],
                                                                  "TX_SEQ_NUM":[5,4],
                                                                  "N_RETX":[3,0]})
        self.registers[0xC3] = Register("RX_PCKT_INFO", 0xC3, 0, {"Reserved":[7,3],
                                                                  "NACK_RX":2,
                                                                  "RX_SEQ_NUM":[1,0]})
        self.registers[0xC4] = Register("AFC_CORR", 0xC4, 0, {"AFC_CORR[7:0]":[7,0]})
        self.registers[0xC5] = Register("LINK_QUALIF[2]", 0xC5, 0, {"PQI[7:0]":[7,0]})
        self.registers[0xC6] = Register("LINK_QUALIF[1]", 0xC6, 0, {"CS":7,
                                                                    "SQI[6:0]":[6,0]})
        self.registers[0xC7] = Register("LINK_QUALIF[0]", 0xC7, 0, {"Reserved":[7,4],
                                                                    "AGC_WORD":[3,0]})
        self.registers[0xC8] = Register("RSSI_LEVEL", 0xC8, 0, {"RSSI_LEVEL[7:0]":[7,0]})
        self.registers[0xC9] = Register("RX_PCKT_LEN[1]", 0xC9, 0, {"RX_PCKT_LEN1":[7,0]})
        self.registers[0xCA] = Register("RX_PCKT_LEN[0]", 0xCA, 0, {"RX_PCKT_LEN0":[7,0]})
        self.registers[0xCB] = Register("CRC_FIELD[2]", 0xCB, 0, {"CRC2":[7,0]})
        self.registers[0xCC] = Register("CRC_FIELD[1]", 0xCC, 0, {"CRC1":[7,0]})
        self.registers[0xCD] = Register("CRC_FIELD[0]", 0xCD, 0, {"CRC0":[7,0]})
        self.registers[0xCE] = Register("CTRL_FIELD[3]", 0xCD, 0, {"RX_CTRL0":[7,0]})
        self.registers[0xCF] = Register("CTRL_FIELD[2]", 0xCF, 0, {"RX_CTRL1":[7,0]})
        self.registers[0xD0] = Register("CTRL_FIELD[1]", 0xD0, 0, {"RX_CTRL2":[7,0]})
        self.registers[0xD1] = Register("CTRL_FIELD[0]", 0xD1, 0, {"RX_CTRL3":[7,0]})
        self.registers[0xD2] = Register("RX_ADDR_FIELD[1]", 0xD2, 0, {"ADDR1":[7,0]})
        self.registers[0xD3] = Register("RX_ADDR_FIELD[0]", 0xD3, 0, {"ADDR0":[7,0]})
        self.registers[0xE4] = Register("RCO_VCO_CALIBR_OUT[1]", 0xE4, 0, {"RWT_OUT[3:0]":[7,4],
                                                                           "RFB_OUT[4:1]":[3,0]})
        self.registers[0xE5] = Register("RCO_VCO_CALIBR_OUT[0]", 0xE5, 0, {"RFB_OUT[0]":7,
                                                                           "VCO_CALIBR_DATA":[6,0]})
        self.registers[0xE6] = Register("LINEAR_FIFO_STATUS[1]", 0xE6, 0, {"Reserved":7,
                                                                           "ELEM_TXFIFO":[6,0]})
        self.registers[0xE7] = Register("LINEAR_FIFO_STATUS[0]", 0xE7, 0, {"Reserved":7,
                                                                           "ELEM_RXFIFO":[6,0]})
        self.registers[0xF0] = Register("DEVICE_INFO[1]", 0xF0, 0x01, {"PARTNUM":[7,0]})
        self.registers[0xF1] = Register("DEVICE_INFO[0]", 0xF1, 0x30, {"VERSION":[7,0]})
        
        for item in self.registers.items():
            self.appendRow(item[1].getRowItems())
            
    def refreshAll(self):
        for key in self.registers.keys():
            self.parent.readRegisters(key)
            
    def updateRegister(self, address, valueList):
        for i in range(len(valueList)):
            self.registers[address+i].setValue(valueList[i])
        
class RegisterTable(QtGui.QTreeView):
    def __init__(self, model, parent=None):
        super(RegisterTable, self).__init__(parent)
        self.model = model
        self.setModel(self.model)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.setColumnWidth(1, 250)
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Value")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Default")
        
        self.expandAllButton = QtGui.QPushButton("Expand")
        self.collapseAllButton = QtGui.QPushButton("Collapse")
        self.expandAllButton.clicked.connect(lambda: self.setExpandAll(True))
        self.collapseAllButton.clicked.connect(lambda: self.setExpandAll(False))
        self.refreshAllButton = QtGui.QPushButton("Refresh")
        self.refreshAllButton.clicked.connect(self.model.refreshAll)
        
        self.widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(self.widget)
        bottom = QtGui.QHBoxLayout()
        bottom.addWidget(self.expandAllButton)
        bottom.addWidget(self.collapseAllButton)
        bottom.addStretch(1)
        bottom.addWidget(self.refreshAllButton)
        bottom.addStretch(1)
        layout.addWidget(self)
        layout.addLayout(bottom)
        
    def setExpandAll(self, expand):
        for i in range(self.model.rowCount()):
            self.setExpanded(self.model.index(i, 0), expand)
def main():
    app = QtGui.QApplication(sys.argv)
    window = RegisterTable()
    window.widget.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()