
ANA_FUNC_CONF1_BASE = 0x00 ##!< ANA_FUNC_CONF1 Address R#W ##

ANA_FUNC_CONF1_NUM_PIPES_MASK  = 0xE0 ##!< Mask for number of enabled pipes##

ANA_FUNC_CONF1_GMCONF_MASK = 0x1C ##!< Mask of the GmConf field of ANA_FUNC_CONF1 register R#W ##

GM_13_2 = 0x00 ##!< Transconducatance Gm at startup 13.2 mS ##
GM_18_2 = 0x04 ##!< Transconducatance Gm at startup 18.2 mS ##
GM_21_5 = 0x08 ##!< Transconducatance Gm at startup 21.5 mS ##
GM_25_6 = 0x0C ##!< Transconducatance Gm at startup 25.6 mS ##
GM_28_8 = 0x10 ##!< Transconducatance Gm at startup 28.8 mS ##
GM_33_9 = 0x14 ##!< Transconducatance Gm at startup 33.9 mS ##
GM_38_5 = 0x18 ##!< Transconducatance Gm at startup 38.5 mS ##
GM_43_0 = 0x1C ##!< Transconducatance Gm at startup 43.0 mS ##

ANA_FUNC_CONF1_SET_BLD_LVL_MASK = 0x03 ##!< Mask of the SET_BLD_LV field of ANA_FUNC_CONF1 register R#W ##

BLD_LVL_2_7 = 0x00 ##!< Sets the Battery Level Detector threshold to 2.7V ##
BLD_LVL_2_5 = 0x01 ##!< Sets the Battery Level Detector threshold to 2.5V ##
BLD_LVL_2_3 = 0x02 ##!< Sets the Battery Level Detector threshold to 2.3V ##
BLD_LVL_2_1 = 0x03 ##!< Sets the Battery Level Detector threshold to 2.1V ##


ANA_FUNC_CONF0_BASE = 0x01 ##!< ANA_FUNC_CONF0 Address R#W ##

SELECT_24_26_MHZ_MASK = 0x40 ##!< Configure the RCO if using 26 MHz or 24 MHz master clock#reference signal ##
AES_MASK = 0x20 ##!< AES engine on#off ##
EXT_REF_MASK = 0x10 ##!< Reference signal from XIN pin oscillator external or from XO circuit oscillator internal##
HIGH_POWER_MODE_MASK = 0x08 ##!< SET_SMPS_LEVEL word will be set to the value to PM_TEST register
# in RX state, while in TX state it will be fixed to 111
# which programs the SMPS output at max value, 1.8V ##
BROWN_OUT_MASK = 0x04 ##!< Accurate BrownOut detection on#off ##
BATTERY_LEVEL_MASK = 0x02 ##!< Battery level detector circuit on#off ##
TEMPERATURE_SENSOR_MASK  = 0x01 ##!< The Temperature Sensor available on GPIO0 on#off ##


ANT_SELECT_CONF_BASE = 0x27 ##!< Antenna diversity works only in static carrier sense mode ##
ANT_SELECT_CS_BLANKING_MASK  = 0x10 ##!< CS data blanking on#off ##
ANT_SELECT_CONF_AS_MASK  = 0x08 ##!< Antenna diversity on#off ##

DEVICE_INFO0_VERSION = 0xF1 ##!< Device version [7:0]; 0x55 in CUT1.0 ##


GPIO3_CONF_BASE = 0x02 ##!< GPIO_3 register address ##
GPIO2_CONF_BASE = 0x03 ##!< GPIO_3 register address ##
GPIO1_CONF_BASE = 0x04 ##!< GPIO_3 register address ##
GPIO0_CONF_BASE = 0x05 ##!< GPIO_3 register address ##

CONF_GPIO_IN_TX_Command = 0x00 ##!< TX command direct from PIN rising edge, width min =50ns ##
CONF_GPIO_IN_RX_Command = 0x08 ##!< RX command direct from PIN rising edge, width min =50ns##
CONF_GPIO_IN_TX_Data = 0x10 ##!< TX data input for direct modulation ##
CONF_GPIO_IN_WKUP_Ext = 0x18 ##!< Wake up from external input ##

CONF_GPIO_OUT_nIRQ = 0x00 ##!< nIRQ Interrupt Request, active low , default configuration after POR ##
CONF_GPIO_OUT_POR_Inv = 0x08 ##!< POR inverted active low ##
CONF_GPIO_OUT_WUT_Exp = 0x10 ##!< WakeUp Timer expiration: 1 when WUT has expired ##
CONF_GPIO_OUT_LBD = 0x18 ##!< Low battery detection: 1 when battery is below threshold setting ##
CONF_GPIO_OUT_TX_Data = 0x20 ##!< TX data internal clock output TX data are sampled on the rising edge of it ##
CONF_GPIO_OUT_TX_State = 0x28 ##!< TX state indication: 1 when Spirit1 is transiting in the TX state ##
CONF_GPIO_OUT_TX_FIFO_Almost_Empty = 0x30 ##!< TX FIFO Almost Empty Flag ##
CONF_GPIO_OUT_TX_FIFO_Amost_Full = 0x38 ##!< TX FIFO Almost Full Flag ##
CONF_GPIO_OUT_RX_Data = 0x40 ##!< RX data output ##
CONF_GPIO_OUT_RX_Clock = 0x48 ##!< RX clock output recovered from received data ##
CONF_GPIO_OUT_RX_State = 0x50 ##!< RX state indication: 1 when Spirit1 is transiting in the RX state ##
CONF_GPIO_OUT_RX_FIFO_Almost_Full = 0x58 ##!< RX FIFO Almost Full Flag ##
CONF_GPIO_OUT_RX_FIFO_Almost_Empty = 0x60 ##!< RX FIFO Almost Empty Flag ##
CONF_GPIO_OUT_Antenna_Switch = 0x68 ##!< Antenna switch used for antenna diversity ##
CONF_GPIO_OUT_Valid_Preamble = 0x70 ##!< Valid Preamble Detected Flag ##
CONF_GPIO_OUT_Sync_Detected = 0x78 ##!< Sync WordSync Word Detected Flag ##
CONF_GPIO_OUT_RSSI_Threshold = 0x80 ##!< CCA Assessment Flag ##
CONF_GPIO_OUT_MCU_Clock = 0x88 ##!< MCU Clock ##
CONF_GPIO_OUT_TX_RX_Mode = 0x90 ##!< TX or RX mode indicator to enable an external range extender ##
CONF_GPIO_OUT_VDD = 0x98 ##!< VDD to emulate an additional GPIO of the MCU, programmable by SPI ##
CONF_GPIO_OUT_GND = 0xA0 ##!< GND to emulate an additional GPIO of the MCU, programmable by SPI ##
CONF_GPIO_OUT_SMPS_Ext = 0xA8 ##!< External SMPS enable signal active high ##

CONF_GPIO_MODE_ANALOG = 0x00 ##!< Analog test BUS on GPIO; used only in test mode except for temperature sensor ##
CONF_GPIO_MODE_DIG_IN = 0x01 ##!< Digital Input on GPIO ##
CONF_GPIO_MODE_DIG_OUTL = 0x02 ##!< Digital Output on GPIO low current ##
CONF_GPIO_MODE_DIG_OUTH = 0x03 ##!< Digital Output on GPIO high current ##

MCU_CK_CONF_BASE = 0x06 ##!< MCU Clock Config register address ##

MCU_CK_ENABLE  = 0x80 ##!< MCU clock enable bit ##

MCU_CK_CONF_CLOCK_TAIL_0 = 0x00 ##!< 0 extra clock cycles provided to the MCU before switching to STANDBY state ##
MCU_CK_CONF_CLOCK_TAIL_64 = 0x20 ##!< 64extra clock cycles provided to the MCU before switching to STANDBY state ##
MCU_CK_CONF_CLOCK_TAIL_256 = 0x40 ##!< 256 extra clock cycles provided to the MCU before switching to STANDBY state ##
MCU_CK_CONF_CLOCK_TAIL_512 = 0x60 ##!< 512 extra clock cycles provided to the MCU before switching to STANDBY state ##
MCU_CK_CONF_XO_RATIO_1 = 0x00 ##!< XO Clock signal available on the GPIO divided by 1 ##
MCU_CK_CONF_XO_RATIO_2_3 = 0x02 ##!< XO Clock signal available on the GPIO divided by 2#3 ##
MCU_CK_CONF_XO_RATIO_1_2 = 0x04 ##!< XO Clock signal available on the GPIO divided by 1#2 ##
MCU_CK_CONF_XO_RATIO_1_3 = 0x06 ##!< XO Clock signal available on the GPIO divided by 1#3 ##
MCU_CK_CONF_XO_RATIO_1_4 = 0x08 ##!< XO Clock signal available on the GPIO divided by 1#4 ##
MCU_CK_CONF_XO_RATIO_1_6 = 0x0A ##!< XO Clock signal available on the GPIO divided by 1#6 ##
MCU_CK_CONF_XO_RATIO_1_8 = 0x0C ##!< XO Clock signal available on the GPIO divided by 1#8 ##
MCU_CK_CONF_XO_RATIO_1_12 = 0x0E ##!< XO Clock signal available on the GPIO divided by 1#12##
MCU_CK_CONF_XO_RATIO_1_16 = 0x10 ##!< XO Clock signal available on the GPIO divided by 1#16##
MCU_CK_CONF_XO_RATIO_1_24 = 0x12 ##!< XO Clock signal available on the GPIO divided by 1#24##
MCU_CK_CONF_XO_RATIO_1_36 = 0x14 ##!< XO Clock signal available on the GPIO divided by 1#36##
MCU_CK_CONF_XO_RATIO_1_48 = 0x16 ##!< XO Clock signal available on the GPIO divided by 1#48##
MCU_CK_CONF_XO_RATIO_1_64 = 0x18 ##!< XO Clock signal available on the GPIO divided by 1#64##
MCU_CK_CONF_XO_RATIO_1_96 = 0x1A ##!< XO Clock signal available on the GPIO divided by 1#96##
MCU_CK_CONF_XO_RATIO_1_128 = 0x1C ##!< XO Clock signal available on the GPIO divided by 1#128 ##
MCU_CK_CONF_XO_RATIO_1_192 = 0x1E ##!< XO Clock signal available on the GPIO divided by 1#196 ##
MCU_CK_CONF_RCO_RATIO_1 = 0x00 ##!< RCO Clock signal available on the GPIO divided by 1##
MCU_CK_CONF_RCO_RATIO_1_128 = 0x01 ##!< RCO Clock signal available on the GPIO divided by 1#128##


SYNT3_BASE = 0x08 ##!< [4:0] > SYNT[25:21], highest 5 bits of the PLL programmable divider ##

WCP_CONF_WCP_378UA = 0x00 ##!< Charge pump current nominal value  = 378uA [VCO 46444708]&[VCO 51615232] ##
WCP_CONF_WCP_369UA = 0x01 ##!< Charge pump current nominal value  = 369uA [VCO 47084772]&[VCO 52325303] ##
WCP_CONF_WCP_359UA = 0x02 ##!< Charge pump current nominal value  = 359uA [VCO 47724836]&[VCO 53035375] ##
WCP_CONF_WCP_350UA = 0x03 ##!< Charge pump current nominal value  = 350uA [VCO 48364902]&[VCO 53755448] ##
WCP_CONF_WCP_340UA = 0x04 ##!< Charge pump current nominal value  = 340uA [VCO 49024966]&[VCO 54485519] ##
WCP_CONF_WCP_331UA = 0x05 ##!< Charge pump current nominal value  = 331uA [VCO 49665030]&[VCO 55195592] ##
WCP_CONF_WCP_321UA = 0x06 ##!< Charge pump current nominal value  = 321uA [VCO 50305095]&[VCO 55925563] ##
WCP_CONF_WCP_312UA = 0x07 ##!< Charge pump current nominal value  = 312uA [VCO 50955160]&[VCO 55635736] ##

SYNT2_BASE = 0x09 ##!< SYNT[20:13], intermediate bits of the PLL programmable divider ##

SYNT1_BASE = 0x0A ##!< SYNT[12:5], intermediate bits of the PLL programmable divider ##

SYNT0_BASE = 0x0B ##!< [7:3] > SYNT[4:0], lowest bits of the PLL programmable divider ##

SYNT0_BS_6 = 0x01 ##!< Synthesizer band select outofloop divide factor of the synthesizer =6779956MHz ##
SYNT0_BS_8 = 0x02 ##!< Synthesizer band select outofloop divide factor of the synthesizer =8387470MHz##
SYNT0_BS_12 = 0x03 ##!< Synthesizer band select outofloop divide factor of the synthesizer =12 387470MHz##
SYNT0_BS_16 = 0x04 ##!< Synthesizer band select outofloop divide factor of the synthesizer =16 300348MHz##
SYNT0_BS_32 = 0x05 ##!< Synthesizer band select outofloop divide factor of the synthesizer =32 150174MHz##


CHSPACE_BASE = 0x0C ##!< Channel spacing. From ~0.8KHz to ~200KHz in fXO#2^15Hz 793Hz for 26MHz XO steps ##


IF_OFFSET_DIG_BASE = 0x0D ##!< Intermediate frequency fIF =fXO#IF_OFFSET_ANA+64#12#2^10 =fCLK#IF_OFFSET_DIG+64#12#2^10 Hz ##

IF_OFFSET_ANA_BASE = 0x07 ##!< Intermediate frequency fIF =fXO#IF_OFFSET_ANA+64#12#2^10 =fCLK#IF_OFFSET_DIG+64#12#2^10 Hz ##

FC_OFFSET1_BASE = 0x0E ##!< [3:0] > [11:8] Carrier offset upper part ##

FC_OFFSET0_BASE = 0x0F ##!< [7:0] > [7:0] Carrier offset lower part. This value is a 12bit 2s complement integer

PA_POWER8_BASE = 0x10 ##!< PA Power level for 8th slot of PA ramping or ASK modulation ##
PA_POWER7_BASE = 0x11 ##!< PA Power level for 7th slot of PA ramping or ASK modulation ##
PA_POWER6_BASE = 0x12 ##!< PA Power level for 6th slot of PA ramping or ASK modulation ##
PA_POWER5_BASE = 0x13 ##!< PA Power level for 5th slot of PA ramping or ASK modulation ##
PA_POWER4_BASE = 0x14 ##!< PA Power level for 4th slot of PA ramping or ASK modulation ##
PA_POWER3_BASE = 0x15 ##!< PA Power level for 3rd slot of PA ramping or ASK modulation ##
PA_POWER2_BASE = 0x16 ##!< PA Power level for 2nd slot of PA ramping or ASK modulation ##
PA_POWER1_BASE = 0x17 ##!< PA Power level for 1st slot of PA ramping or ASK modulation ##

PA_POWER0_BASE = 0x18 ##!< PA ramping settings and additional load capacitor banks used
# for PA optimization in different sub bands##
PA_POWER0_CWC_MASK = 0x20 ##!< Output stage additional load capacitors bank ##
PA_POWER0_CWC_0 = 0x00 ##!< No additional PA load capacitor ##
PA_POWER0_CWC_1_2P = 0x40 ##!< 1.2pF additional PA load capacitor ##
PA_POWER0_CWC_2_4P = 0x80 ##!< 2.4pF additional PA load capacitor ##
PA_POWER0_CWC_3_6P = 0xC0 ##!< 3.6pF additional PA load capacitor ##
PA_POWER0_PA_RAMP_MASK = 0x20 ##!< The PA power ramping ##
PA_POWER0_PA_RAMP_STEP_WIDTH_MASK  = 0x20 ##!< The step width ##
PA_POWER0_PA_RAMP_STEP_WIDTH_TB_8 = 0x00 ##!< PA ramping time step  = 1#8 Bit period##
PA_POWER0_PA_RAMP_STEP_WIDTH_TB_4 = 0x08 ##!< PA ramping time step  = 2#8 Bit period##
PA_POWER0_PA_RAMP_STEP_WIDTH_3TB_8 = 0x10 ##!< PA ramping time step  = 3#8 Bit period##
PA_POWER0_PA_RAMP_STEP_WIDTH_TB_2 = 0x18 ##!< PA ramping time step  = 4#8 Bit period##
PA_POWER0_PA_LEVEL_MAX_INDEX = 0x20 ##!< Final level for power ramping ##
PA_POWER0_PA_LEVEL_MAX_INDEX_0 = 0x00 ##!< ##
PA_POWER0_PA_LEVEL_MAX_INDEX_1 = 0x01 ##!<Fixes the MAX PA LEVEL in PA ramping or ASK modulation ##
PA_POWER0_PA_LEVEL_MAX_INDEX_2 = 0x02 ##!< ##
PA_POWER0_PA_LEVEL_MAX_INDEX_3 = 0x03 ##!< _________ ##
PA_POWER0_PA_LEVEL_MAX_INDEX_4 = 0x04 ##!< PA_LVL2 _| <| ##
PA_POWER0_PA_LEVEL_MAX_INDEX_5 = 0x05 ##!< _|| ##
PA_POWER0_PA_LEVEL_MAX_INDEX_6 = 0x06 ##!< PA_LVL1 _|| ##
PA_POWER0_PA_LEVEL_MAX_INDEX_7 = 0x07 ##!< PA_LVL0 _| MAX_INDEX ##

MOD1_BASE = 0x1A ##!< The Mantissa of the specified data rate ##

MOD0_BASE = 0x1B ##!< Modulation Settings, Exponent of the specified data rate, CW mode##

MOD0_MOD_TYPE_2_FSK = 0x00 ##!< Modulation type 2FSK MSK if the frequency deviation is identical to a quarter of the data rate ##
MOD0_MOD_TYPE_GFSK = 0x10 ##!< Modulation type GFSK GMSK if the frequency deviation is identical to a quarter of the data rate ##
MOD0_MOD_TYPE_ASK = 0x20 ##!< Modulation type ASK OOK the PA is switched off for symbol "0" ##
MOD0_MOD_TYPE_MSK = 0x00 ##!< Modulation type MSK the frequency deviation must be identical to a quarter of the data rate ##
MOD0_MOD_TYPE_GMSK = 0x10 ##!< Modulation type GMSK the frequency deviation must be identical to a quarter of the data rate ##
MOD0_BT_SEL_BT_MASK  = 0x00 ##!< Select the BT  = 1 or BT  = 0.5 valid only for GFSK or GMSK modulation##
MOD0_CW = 0x80 ##!< Set the Continous Wave no modulation transmit mode ##

FDEV0_BASE = 0x1C ##!< Sets the Mantissa and exponent of frequency deviation frequency separation#2
# and PLL or DLL alogrithm from clock recovery in RX digital demod##
FDEV0_CLOCK_REG_ALGO_SEL_MASK = 0x08 ##!< Can be DLL or PLL algorithm for clock recovery in RX digital demod see CLOCKREC reg ##
FDEV0_CLOCK_REG_ALGO_SEL_PLL = 0x00 ##!< Sets PLL alogrithm for clock recovery in RX digital demod see CLOCKREC reg ##
FDEV0_CLOCK_REG_ALGO_SEL_DLL = 0x08 ##!< Sets DLL alogrithm for clock recovery in RX digital demod see CLOCKREC reg ##

CHFLT_BASE = 0x1D ##!< RX Channel Filter Bandwidth ##

CHFLT_800_1 = 0x00 ##!< RX Channel Filter Bandwidth  = 800.1 kHz ##
CHFLT_795_1 = 0x10 ##!< RX Channel Filter Bandwidth  = 795.1 kHz ##
CHFLT_768_4 = 0x20 ##!< RX Channel Filter Bandwidth  = 768.4 kHz ##
CHFLT_736_8 = 0x30 ##!< RX Channel Filter Bandwidth  = 736.8 kHz ##
CHFLT_705_1 = 0x40 ##!< RX Channel Filter Bandwidth  = 705.1 kHz ##
CHFLT_670_9 = 0x50 ##!< RX Channel Filter Bandwidth  = 670.9 kHz ##
CHFLT_642_3 = 0x60 ##!< RX Channel Filter Bandwidth  = 642.3 kHz ##
CHFLT_586_7 = 0x70 ##!< RX Channel Filter Bandwidth  = 586.7 kHz ##
CHFLT_541_4 = 0x80 ##!< RX Channel Filter Bandwidth  = 541.4 kHz ##
CHFLT_450_9 = 0x01 ##!< RX Channel Filter Bandwidth  = 450.9 kHz ##
CHFLT_425_9 = 0x11 ##!< RX Channel Filter Bandwidth  = 425.9 kHz ##
CHFLT_403_2 = 0x21 ##!< RX Channel Filter Bandwidth  = 403.2 kHz ##
CHFLT_380_8 = 0x31 ##!< RX Channel Filter Bandwidth  = 380.8 kHz ##
CHFLT_362_1 = 0x41 ##!< RX Channel Filter Bandwidth  = 362.1 kHz ##
CHFLT_341_7 = 0x51 ##!< RX Channel Filter Bandwidth  = 341.7 kHz ##
CHFLT_325_4 = 0x61 ##!< RX Channel Filter Bandwidth  = 325.4 kHz ##
CHFLT_294_5 = 0x71 ##!< RX Channel Filter Bandwidth  = 294.5 kHz ##
CHFLT_270_3 = 0x81 ##!< RX Channel Filter Bandwidth  = 270.3 kHz ##
CHFLT_224_7 = 0x02 ##!< RX Channel Filter Bandwidth  = 224.7 kHz ##
CHFLT_212_4 = 0x12 ##!< RX Channel Filter Bandwidth  = 212.4 kHz ##
CHFLT_201_1 = 0x22 ##!< RX Channel Filter Bandwidth  = 201.1 kHz ##
CHFLT_190 = 0x32 ##!< RX Channel Filter Bandwidth  = 190.0 kHz ##
CHFLT_180_7 = 0x42 ##!< RX Channel Filter Bandwidth  = 180.7 kHz ##
CHFLT_170_6 = 0x52 ##!< RX Channel Filter Bandwidth  = 170.6 kHz ##
CHFLT_162_4 = 0x62 ##!< RX Channel Filter Bandwidth  = 162.4 kHz ##
CHFLT_147_1 = 0x72 ##!< RX Channel Filter Bandwidth  = 147.1 kHz ##
CHFLT_135 = 0x82 ##!< RX Channel Filter Bandwidth  = 135.0 kHz ##
CHFLT_112_3 = 0x03 ##!< RX Channel Filter Bandwidth  = 112.3 kHz ##
CHFLT_106_2 = 0x13 ##!< RX Channel Filter Bandwidth  = 106.2 kHz ##
CHFLT_100_5 = 0x23 ##!< RX Channel Filter Bandwidth  = 100.5 kHz ##
CHFLT_95 = 0x33 ##!< RX Channel Filter Bandwidth  = 95.0 kHz ##
CHFLT_90_3 = 0x43 ##!< RX Channel Filter Bandwidth  = 90.3 kHz ##
CHFLT_85_3 = 0x53 ##!< RX Channel Filter Bandwidth  = 85.3 kHz ##
CHFLT_81_2 = 0x63 ##!< RX Channel Filter Bandwidth  = 81.2 kHz ##
CHFLT_73_5 = 0x73 ##!< RX Channel Filter Bandwidth  = 73.5 kHz ##
CHFLT_67_5 = 0x83 ##!< RX Channel Filter Bandwidth  = 67.5 kHz ##
CHFLT_56_1 = 0x04 ##!< RX Channel Filter Bandwidth  = 56.1 kHz ##
CHFLT_53 = 0x14 ##!< RX Channel Filter Bandwidth  = 53.0 kHz ##
CHFLT_50_2 = 0x24 ##!< RX Channel Filter Bandwidth  = 50.2 kHz ##
CHFLT_47_4 = 0x34 ##!< RX Channel Filter Bandwidth  = 47.4 kHz ##
CHFLT_45_1 = 0x44 ##!< RX Channel Filter Bandwidth  = 45.1 kHz ##
CHFLT_42_6 = 0x54 ##!< RX Channel Filter Bandwidth  = 42.6 kHz ##
CHFLT_40_6 = 0x64 ##!< RX Channel Filter Bandwidth  = 40.6 kHz ##
CHFLT_36_7 = 0x74 ##!< RX Channel Filter Bandwidth  = 36.7 kHz ##
CHFLT_33_7 = 0x84 ##!< RX Channel Filter Bandwidth  = 33.7 kHz ##
CHFLT_28 = 0x05 ##!< RX Channel Filter Bandwidth  = 28.0 kHz ##
CHFLT_26_5 = 0x15 ##!< RX Channel Filter Bandwidth  = 26.5 kHz ##
CHFLT_25_1 = 0x25 ##!< RX Channel Filter Bandwidth  = 25.1 kHz ##
CHFLT_23_7 = 0x35 ##!< RX Channel Filter Bandwidth  = 23.7 kHz ##
CHFLT_22_6 = 0x45 ##!< RX Channel Filter Bandwidth  = 22.6 kHz ##
CHFLT_21_3 = 0x55 ##!< RX Channel Filter Bandwidth  = 21.3 kHz ##
CHFLT_20_3 = 0x65 ##!< RX Channel Filter Bandwidth  = 20.3 kHz ##
CHFLT_18_4 = 0x75 ##!< RX Channel Filter Bandwidth  = 18.4 kHz ##
CHFLT_16_9 = 0x85 ##!< RX Channel Filter Bandwidth  = 16.9 kHz ##
CHFLT_14 = 0x06 ##!< RX Channel Filter Bandwidth  = 14.0 kHz ##
CHFLT_13_3 = 0x16 ##!< RX Channel Filter Bandwidth  = 13.3 kHz ##
CHFLT_12_6 = 0x26 ##!< RX Channel Filter Bandwidth  = 12.6 kHz ##
CHFLT_11_9 = 0x36 ##!< RX Channel Filter Bandwidth  = 11.9 kHz ##
CHFLT_11_3 = 0x46 ##!< RX Channel Filter Bandwidth  = 11.3 kHz ##
CHFLT_10_6 = 0x56 ##!< RX Channel Filter Bandwidth  = 10.6 kHz ##
CHFLT_10_1 = 0x66 ##!< RX Channel Filter Bandwidth  = 10.1 kHz ##
CHFLT_9_2 = 0x76 ##!< RX Channel Filter Bandwidth  = 9.2 kHz ##
CHFLT_8_4 = 0x86 ##!< RX Channel Filter Bandwidth  = 8.4 kHz ##
CHFLT_7 = 0x07 ##!< RX Channel Filter Bandwidth  = 7.0 kHz ##
CHFLT_6_6 = 0x17 ##!< RX Channel Filter Bandwidth  = 6.6 kHz ##
CHFLT_6_3 = 0x27 ##!< RX Channel Filter Bandwidth  = 6.3 kHz ##
CHFLT_5_9 = 0x37 ##!< RX Channel Filter Bandwidth  = 5.9 kHz ##
CHFLT_5_6 = 0x47 ##!< RX Channel Filter Bandwidth  = 5.6 kHz ##
CHFLT_5_3 = 0x57 ##!< RX Channel Filter Bandwidth  = 5.3 kHz ##
CHFLT_5_1 = 0x67 ##!< RX Channel Filter Bandwidth  = 5.1 kHz ##
CHFLT_4_6 = 0x77 ##!< RX Channel Filter Bandwidth  = 4.6 kHz ##
CHFLT_4_2 = 0x87 ##!< RX Channel Filter Bandwidth  = 4.2 kHz ##
CHFLT_3_5 = 0x08 ##!< RX Channel Filter Bandwidth  = 3.5 kHz ##
CHFLT_3_3 = 0x18 ##!< RX Channel Filter Bandwidth  = 3.3 kHz ##
CHFLT_3_1 = 0x28 ##!< RX Channel Filter Bandwidth  = 3.1 kHz ##
CHFLT_3 = 0x38 ##!< RX Channel Filter Bandwidth  = 3.0 kHz ##
CHFLT_2_8 = 0x48 ##!< RX Channel Filter Bandwidth  = 2.8 kHz ##
CHFLT_2_7 = 0x58 ##!< RX Channel Filter Bandwidth  = 2.7 kHz ##
CHFLT_2_5 = 0x68 ##!< RX Channel Filter Bandwidth  = 2.5 kHz ##
CHFLT_2_3 = 0x78 ##!< RX Channel Filter Bandwidth  = 2.3 kHz ##
CHFLT_2_1 = 0x88 ##!< RX Channel Filter Bandwidth  = 2.1 kHz ##
CHFLT_1_8 = 0x09 ##!< RX Channel Filter Bandwidth  = 1.8 kHz ##
CHFLT_1_7 = 0x19 ##!< RX Channel Filter Bandwidth  = 1.7 kHz ##
CHFLT_1_6 = 0x29 ##!< RX Channel Filter Bandwidth  = 1.6 kHz ##
CHFLT_1_5 = 0x39 ##!< RX Channel Filter Bandwidth  = 1.5 kHz ##
CHFLT_1_4 = 0x49 ##!< RX Channel Filter Bandwidth  = 1.4 kHz ##
CHFLT_1_3a = 0x59 ##!< RX Channel Filter Bandwidth  = 1.3 kHz ##
CHFLT_1_3 = 0x69 ##!< RX Channel Filter Bandwidth  = 1.3 kHz ##
CHFLT_1_2 = 0x79 ##!< RX Channel Filter Bandwidth  = 1.2 kHz ##
CHFLT_1_1 = 0x89 ##!< RX Channel Filter Bandwidth  = 1.1 kHz ##

##
AFC2_BASE = 0x1E ##!< Automatic frequency compensation algorithm parameters FSK#GFSK#MSK##

AFC2_AFC_FREEZE_ON_SYNC_MASK = 0x80 ##!< The frequency correction value is frozen when SYNC word is detected ##
AFC2_AFC_MASK = 0x40 ##!< Mask of Automatic Frequency Correction ##
AFC2_AFC_MODE_MASK = 0x20 ##!< Automatic Frequency Correction can be in Main MODE or Auxiliary MODE##
AFC2_AFC_MODE_SLICER = 0x00 ##!< Automatic Frequency Correction Main MODE ##
AFC2_AFC_MODE_MIXER = 0x20 ##!< Automatic Frequency Correction Auxiliary MODE ##


AFC1_BASE = 0x1F ##!< Length of the AFC fast period ##
AFC0_BASE = 0x20 ##!< AFC loop gain in fast and slow modes 2's log ##

CLOCKREC_BASE = 0x23 ##!< Gain of clock recovery loop  Postfilter length 08 symbols, 116 symbols ##

AGCCTRL2_BASE = 0x24 ##!< AGC freeze strategy, AGC attenuationstrategy, AGC measure time ##

AGCCTRL2_FREEZE_ON_STEADY_MASK = 0x40 ##!< The attenuation settings will be frozen as soon as signal level
# is betweeen min and max treshold see AGCCTRL1 ##
AGCCTRL2_FREEZE_ON_SYNC_MASK = 0x20 ##!< The attenuation settings will be frozen as soon sync word is detected ##
AGCCTRL2_START_MAX_ATTENUATION_MASK = 0x10 ##!< The AGC algorithm can start with MAX attenuation or MIN attenuation ##

AGCCTRL1_BASE = 0x25 ##!< Sets low and high threshold for AGC ##

AGCCTRL0_BASE = 0x26 ##!< Enables AGC, set AGC algo between linear#binary mode, set hold time
# to account signal propagation through RX chain ##
AGCCTRL0_AGC_MASK = 0x80 ##!< AGC on#off ##
AGCCTRL0_AGC_MODE_MASK = 0x40 ##!< AGC search correct attenuation in binary mode or sequential mode ##
AGCCTRL0_AGC_MODE_LINEAR = 0x00 ##!< AGC search correct attenuation in sequential mode recommended ##
AGCCTRL0_AGC_MODE_BINARY = 0x40 ##!< AGC search correct attenuation in binary mode ##

CHNUM_BASE = 0x6C ##!< Channel number. This value is multiplied by the channel

AFC_CORR_BASE = 0xC4 ##!< AFC word of the received packet ##

PCKTCTRL4_BASE = 0x30 ##!< lenghts of address and control field ##

PCKTCTRL4_ADDRESS_LEN_MASK = 0x18
PCKTCTRL4_CONTROL_LEN_MASK = 0x07

PCKTCTRL3_BASE = 0x31 ##!< packet format, RX mode, lenght of length field ##

PCKTCTRL3_PCKT_FRMT_BASIC = 0x00 ##!< Basic Packet Format ##
PCKTCTRL3_PCKT_FRMT_MBUS = 0x80 ##!< Wireless MBUS Packet Format ##
PCKTCTRL3_PCKT_FRMT_STACK = 0xC0 ##!< STack Packet Format ##

PCKTCTRL3_RX_MODE_NORMAL = 0x00 ##!< Normal RX Mode ##
PCKTCTRL3_RX_MODE_DIRECT_FIFO = 0x10 ##!< RX Direct Mode; data available through FIFO ##
PCKTCTRL3_RX_MODE_DIRECT_GPIO = 0x20 ##!< RX Direct Mode; data available through selected GPIO ##

PCKTCTRL3_PKT_FRMT_MASK  = 0xC0
PCKTCTRL3_RX_MODE_MASK = 0x30
PCKTCTRL3_LEN_WID_MASK = 0x0F

PCKTCTRL2_BASE = 0x32 ##!< length of preamble and sync fields in bytes, fix or variable packet length ##

PCKTCTRL2_FIX_VAR_LEN_MASK = 0x01 ##!< Enable#disable the length mode ##
PCKTCTRL2_PREAMBLE_LENGTH_MASK = 0xF8
PCKTCTRL2_SYNC_LENGTH_MASK = 0x06

PCKTCTRL1_BASE = 0x33 ##!< CRC type, whitening enable, TX mode ##

PCKTCTRL1_FEC_MASK = 0x01 ##!< Enable#disable the Forward Error Correction ##
PCKTCTRL1_TX_SOURCE_MASK = 0x0C ##!< TX source mode ##
PCKTCTRL1_CRC_MODE_MASK  = 0xE0 ##!< CRC type ##
PCKTCTRL1_WHIT_MASK  = 0x10 ##!< Enable#disable the Whitening ##

PCKTLEN1_BASE = 0x34 ##!< lenght of packet in bytes upper field ##

PCKTLEN0_BASE = 0x35 ##!< lenght of packet in bytes lower field [PCKTLEN =PCKTLEN1x256+PCKTLEN0]##

SYNC4_BASE = 0x36 ##!< Sync word 4 ##
SYNC3_BASE = 0x37 ##!< Sync word 3 ##
SYNC2_BASE = 0x38 ##!< Sync word 2 ##
SYNC1_BASE = 0x39 ##!< Sync word 1 ##

MBUS_PRMBL_BASE = 0x3B ##!< MBUS preamble lenght in 01 bit pairs ##

MBUS_PSTMBL_BASE = 0x3C ##!< MBUS postamble length in 01 bit pairs ##

MBUS_CTRL_BASE = 0x3D ##!< MBUS submodes S1, S2 short#long header, T1, T2, R2 ##

MBUS_CTRL_MBUS_SUBMODE_S1_S2L = 0x00 ##!< MBUS submodes S1 & S2L, header lenght min 279, sync 0x7696, Manchester ##
MBUS_CTRL_MBUS_SUBMODE_S2_S1M_T2_OTHER = 0x02 ##!< MBUS submodes S2, S1m, T2 only other to meter short header, header lenght min 15, sync 0x7696, Manchester ##
MBUS_CTRL_MBUS_SUBMODE_T1_T2_METER = 0x06 ##!< MBUS submodes T1, T2 only meter to other, header lenght min 19, sync 0x3D, 3 out of 6 ##
MBUS_CTRL_MBUS_SUBMODE_R2 = 0x0A ##!< MBUS submode R2, header lenght min 39, sync 0x7696, Manchester ##

PCKT_FLT_GOALS_CONTROL0_MASK_BASE = 0x42 ##!< Packet control field #3 mask, all 0s > no filtering ##

PCKT_FLT_GOALS_CONTROL1_MASK_BASE = 0x43 ##!< Packet control field #2 mask, all 0s > no filtering ##

PCKT_FLT_GOALS_CONTROL2_MASK_BASE = 0x44 ##!< Packet control field #1 mask, all 0s > no filtering ##

PCKT_FLT_GOALS_CONTROL3_MASK_BASE = 0x45 ##!< Packet control field #0 mask, all 0s > no filtering ##

###
# @}
##

### @defgroup PCKT_FLT_GOALS_CONTROLx_FIELD_Registers
# @{
##

###
#\brief PCKT_FLT_GOALS_CONTROLx_FIELDregisters
#\code
# Default value: 0x00
# Read Write
# 7:0CONTROLx_FIELD[7:0]: Control field byte x to be used as reference
#
# \endcode
##
PCKT_FLT_GOALS_CONTROL0_FIELD_BASE = 0x46 ##!< Control field byte #3 ##

PCKT_FLT_GOALS_CONTROL1_FIELD_BASE = 0x47 ##!< Control field byte #2 ##

PCKT_FLT_GOALS_CONTROL2_FIELD_BASE = 0x48 ##!< Control field byte #1 ##

PCKT_FLT_GOALS_CONTROL3_FIELD_BASE = 0x49 ##!< Control field byte #0 ##

###
# @}
##

### @defgroup PCKT_FLT_GOALS_SOURCE_MASK_Register
# @{
##

###
#\brief PCKT_FLT_GOALS_SOURCE_MASKregister
#\code
# Default value: 0x00
# Read Write
# 7:0RX_SOURCE_MASK[7:0]: For received packet only: all 0s  no filtering
#
# \endcode
##
PCKT_FLT_GOALS_SOURCE_MASK_BASE = 0x4A ##!< Source address mask, valid in RX mode ##

###
# @}
##

### @defgroup PCKT_FLT_GOALS_SOURCE_ADDR_Register
# @{
##
###
#\brief PCKT_FLT_GOALS_SOURCE_ADDRregister
#\code
# Default value: 0x00
# Read Write
# 7:0RX_SOURCE_ADDR[7:0]:RX packet source # TX packet destination fields
#
# \endcode
##
PCKT_FLT_GOALS_SOURCE_ADDR_BASE = 0x4B ##!< Source address ##

###
# @}
##

### @defgroup PCKT_FLT_GOALS_BROADCAST_Register
# @{
##

###
#\brief PCKT_FLT_GOALS_BROADCASTregister
#\code
# Default value: 0x00
# Read Write
# 7:0BROADCAST[7:0]:Address shared for broadcast communication link
#
# \endcode
##
PCKT_FLT_GOALS_BROADCAST_BASE = 0x4C ##!< Address shared for broadcast communication links ##

###
# @}
##

### @defgroup PCKT_FLT_GOALS_MULTICAST_Register
# @{
##

###
#\brief PCKT_FLT_GOALS_MULTICASTregister
#\code
# Default value: 0x00
# Read Write
# 7:0MULTICAST[7:0]:Address shared for multicast communication links
#
# \endcode
##
PCKT_FLT_GOALS_MULTICAST_BASE = 0x4D ##!< Address shared for multicast communication links ##

###
# @}
##

### @defgroup PCKT_FLT_GOALS_TX_SOURCE_ADDR_Register
# @{
##

###
#\brief PCKT_FLT_GOALS_TX_SOURCE_ADDRregister
#\code
# Default value: 0x00
# Read Write
# 7:0TX_SOURCE_ADDR[7:0]:TX packet source # RX packet destination fields
#
# \endcode
##
PCKT_FLT_GOALS_TX_ADDR_BASE = 0x4E ##!< Address of the destination also device own address ##

###
# @}
##

### @defgroup PCKT_FLT_OPTIONS_Register
# @{
##

###
#\brief PCKT_FLT_OPTIONSregister
#\code
# Default value: 0x70
# Read Write
# 7 Reserved.
#
# 6 RX_TIMEOUT_AND_OR_SELECT[0]:1  OR logical function applied to CS#SQI#PQI
# values masked by 7:5 bits in PROTOCOL register
# 5 CONTROL_FILTERING[0]: 1  RX packet accepted if its control fields matches
# with masked CONTROLx_FIELD registers.
# 4 SOURCE_FILTERING[0]:1  RX packet accepted if its source field
# matches w# masked RX_SOURCE_ADDR register.
# 3 DEST_VS_ SOURCE _ADDR[0]: 1  RX packet accepted if its destination
# address matches with TX_SOURCE_ADDR reg.
# 2 DEST_VS_MULTICAST_ADDR[0]:1  RX packet accepted if its destination
# address matches with MULTICAST register
# 1 DEST_VS_BROADCAST_ADDR[0]:1  RX packet accepted if its destination
# address matches with BROADCAST register.
# 0 CRC_CHECK[0]: 1  packet discarded if CRC not valid.
#
# \endcode
##
PCKT_FLT_OPTIONS_BASE = 0x4F ##!< Options relative to packet filtering ##

PCKT_FLT_OPTIONS_CRC_CHECK_MASK  = 0x01 ##!< Enable#disable of CRC check: packet is discarded if CRC is not valid [RX] ##
PCKT_FLT_OPTIONS_DEST_VS_TX_ADDR_MASK = 0x08 ##!< Packet discarded if destination address differs from TX_ADDR register [RX] ##
PCKT_FLT_OPTIONS_DEST_VS_MULTICAST_ADDR_MASK = 0x04 ##!< Packet discarded if destination address differs from MULTICAST register [RX] ##
PCKT_FLT_OPTIONS_DEST_VS_BROADCAST_ADDR_MASK = 0x02 ##!< Packet discarded if destination address differs from MULTICAST register [RX] ##
PCKT_FLT_OPTIONS_SOURCE_FILTERING_MASK = 0x10 ##!< Packet discarded if source address masked by the SOURCE_MASK register
# differs from SOURCE_ADDR register [RX] ##
PCKT_FLT_OPTIONS_CONTROL_FILTERING_MASK = 0x20 ##!< Packet discarded if the xbyte x =14 control fieldmasked by the CONTROLx_MASK register
# differs from CONTROLx_FIELD register [RX] ##
PCKT_FLT_OPTIONS_RX_TIMEOUT_AND_OR_SELECT = 0x40 ##!< Logical function applied to CS#SQI#PQI values masked by [7:5] bits in PROTOCOL[2]
# register ##

###
# @}
##

### @defgroup TX_CTRL_FIELD_Registers
# @{
##

###
#\brief TX_CTRL_FIELDxregisters
#\code
# Default value: 0x00
# Read Write
# 7:0 TX_CTRLx[7:0]: Control field value to be used in TX packet as byte n.x
# \endcode
##
TX_CTRL_FIELD3_BASE = 0x68 ##!< Control field value to be used in TX packet as byte n.3 ##

TX_CTRL_FIELD2_BASE = 0x69 ##!< Control field value to be used in TX packet as byte n.2 ##

TX_CTRL_FIELD1_BASE = 0x6A ##!< Control field value to be used in TX packet as byte n.1 ##

TX_CTRL_FIELD0_BASE = 0x6B ##!< Control field value to be used in TX packet as byte n.0 ##

###
# @}
##


### @defgroup TX_PCKT_INFO_Register
# @{
##

###
#\brief TX_PCKT_INFOregisters
#\code
# Default value: 0x00
# Read
#
# 7:6 Not used.
#
# 5:4 TX_SEQ_NUM: Current TX packet sequence number
#
# 0 N_RETX[3:0]:Number of retransmissions done on the
#last TX packet
# \endcode
##
TX_PCKT_INFO_BASE = 0xC2 ##!< Current TX packet sequence number [5:4];
# Number of retransmissions done on the last TX packet [3:0]##
###
# @}
##

### @defgroup RX_PCKT_INFO_Register
# @{
##

###
#\brief RX_PCKT_INFOregisters
#\code
# Default value: 0x00
# Read
#
# 7:3 Not used.
#
# 2 NACK_RX: NACK field of the received packet
#
# 1:0 RX_SEQ_NUM[1:0]:Sequence number of the received packet
# \endcode
##
RX_PCKT_INFO_BASE = 0xC3 ##!< NO_ACK field of the received packet [2];
# sequence number of the received packet [1:0]##

TX_PCKT_INFO_NACK_RX = 0x04 ##!< NACK field of the received packet ##

###
# @}
##

### @defgroup RX_PCKT_LEN1
# @{
##

###
#\brief RX_PCKT_LEN1registers
#\code
# Default value: 0x00
# Read
#
# 7:0 RX_PCKT_LEN1[7:0]:Length number of bytes of the received packet: RX_PCKT_LEN =RX_PCKT_LEN1  256 + RX_PCKT_LEN0
# This value is packet_length#256
# \endcode
##
RX_PCKT_LEN1_BASE = 0xC9 ##!< Length number ofbytes of the received packet: ##

###
# @}
##

### @defgroup RX_PCKT_LEN0
# @{
##

###
#\brief RX_PCKT_LEN0registers
#\code
# Default value: 0x00
# Read
#
# 7:0 RX_PCKT_LEN0[7:0]:Length number of bytes of the received packet: RX_PCKT_LEN =RX_PCKT_LEN1  256 + RX_PCKT_LEN0
# This value is packet_length%256
# \endcode
##
RX_PCKT_LEN0_BASE = 0xCA ##!< RX_PCKT_LEN =RX_PCKT_LEN1  256 + RX_PCKT_LEN0 ##

###
# @}
##


### @defgroup CRC_FIELD_Register
# @{
##

###
#\brief CRC_FIELD[2:0]registers
#\code
# Default value: 0x00
# Read
#
# 7:0 CRC_FIELDx[7:0]:upperx =2, middlex =1 and lowerx =0 part of the crc field of the received packet
#\endcode
##
CRC_FIELD2_BASE = 0xCB ##!< CRC2 field of the received packet ##

CRC_FIELD1_BASE = 0xCC ##!< CRC1 field of the received packet ##

CRC_FIELD0_BASE = 0xCD ##!< CRC0 field of the received packet ##

###
# @}
##

### @defgroup RX_CTRL_FIELD_Register
# @{
##

###
#\brief RX_CTRL_FIELD[3:0]registers
#\code
# Default value: 0x00
# Read
#
# 7:0 RX_CTRL_FIELDx[7:0]:upperx =3, middlex =2, middlex =1 and lowerx =0 part of the control field of the received packet
# \endcode
##
RX_CTRL_FIELD0_BASE = 0xCE ##!< CRTL3 Control field of the received packet ##

RX_CTRL_FIELD1_BASE = 0xCF ##!< CRTL2 Control field of the received packet ##

RX_CTRL_FIELD2_BASE = 0xD0 ##!< CRTL1 Control field of the received packet ##

RX_CTRL_FIELD3_BASE = 0xD1 ##!< CRTL0 Control field of the received packet ##

###
# @}
##

### @defgroup RX_ADDR_FIELD_Register
# @{
##

###
#\brief RX_ADDR_FIELD[1:0]registers
#\code
# Default value: 0x00
# Read
#
# 7:0 RX_ADDR_FIELDx[7:0]:sourcex =1 and destinationx =0 address field of the received packet
# \endcode
##
RX_ADDR_FIELD1_BASE = 0xD2 ##!< ADDR1 Address field of the received packet ##

RX_ADDR_FIELD0_BASE = 0xD3 ##!< ADDR0 Address field of the received packet ##

###
# @}
##

###
# @}
##


### @defgroup Protocol_Registers
# @{
##

### @defgroup PROTOCOL2_Register
# @{
##

###
#\brief PROTOCOL2register
#\code
# Default value: 0x06
# Read Write
# 7 CS_TIMEOUT_MASK:1  CS value contributes to timeout disabling
#
# 6 SQI_TIMEOUT_MASK: 1  SQI value contributes to timeout disabling
#
# 5 PQI_TIMEOUT_MASK: 1  PQI value contributes to timeout disabling
#
# 4:3TX_SEQ_NUM_RELOAD[1:0]:TX sequence number to be used when counting reset is required using the related command.
#
# 2 RCO_CALIBRATION[0]: 1  Enables the automatic RCO calibration
#
# 1 VCO_CALIBRATION[0]: 1  Enables the automatic VCO calibration
#
# 0 LDCR_MODE[0]: 1  LDCR mode enabled
#
# \endcode
##
PROTOCOL2_BASE = 0x50 ##!< Protocol2 regisetr address ##

PROTOCOL2_LDC_MODE_MASK = 0x01 ##!< Enable#disable Low duty Cycle mode ##
PROTOCOL2_VCO_CALIBRATION_MASK = 0x02 ##!< Enable#disable VCO automatic calibration ##
PROTOCOL2_RCO_CALIBRATION_MASK = 0x04 ##!< Enable#disable RCO automatic calibration ##
PROTOCOL2_PQI_TIMEOUT_MASK = 0x20 ##!< PQI value contributes to timeout disabling ##
PROTOCOL2_SQI_TIMEOUT_MASK = 0x40 ##!< SQI value contributes to timeout disabling ##
PROTOCOL2_CS_TIMEOUT_MASK = 0x80 ##!< CS value contributes to timeout disabling ##

###
# @}
##

### @defgroup PROTOCOL1_Register
# @{
##

###
#\brief PROTOCOL1register
#\code
# Default value: 0x00
# Read Write
# 7 LDCR_RELOAD_ON_SYNC:1  LDCR timer will be reloaded with the value stored in the LDCR_RELOAD registers
#
# 6 PIGGYBACKING: 1  PIGGYBACKING enabled
#
# 5:4 Reserved.
#
# 3 SEED_RELOAD[0]: 1  Reload the backoff random generator
#seed using the value written in the
#BU_COUNTER_SEED_MSByte # LSByte registers
#
# 2 CSMA_ON [0]:1  CSMA channel access mode enabled
#
# 1 CSMA_PERS_ON[0]:1  CSMA persistent no backoff enabled
#
# 0 AUTO_PCKT_FLT[0]: 1  automatic packet filtering mode enabled
#
# \endcode
##
PROTOCOL1_BASE = 0x51 ##!< Protocol1 regisetr address ##

PROTOCOL1_AUTO_PCKT_FLT_MASK = 0x01 ##!< Enable#disable automatic packet filtering mode ##
PROTOCOL1_CSMA_PERS_ON_MASK = 0x02 ##!< Enable#disable CSMA persistent no backoff##
PROTOCOL1_CSMA_ON_MASK = 0x04 ##!< Enable#disable CSMA channel access mode ##
PROTOCOL1_SEED_RELOAD_MASK = 0x08 ##!< Reloads the seed of the PN generator for CSMA procedure ##
PROTOCOL1_PIGGYBACKING_MASK = 0x40 ##!< Enable#disable Piggybacking ##
PROTOCOL1_LDC_RELOAD_ON_SYNC_MASK = 0x80 ##!< LDC timer will be reloaded with the value stored in the LDC_RELOAD registers ##

###
# @}
##

### @defgroup PROTOCOL0_Register
# @{
##

###
#\brief PROTOCOL0register
#\code
# Default value: 0x08
# Read Write
# 7:4 NMAX_RETX[3:0]: Max number of reTX.0  retransmission is not performed
#
# 3 NACK_TX[0]: 1  field NO_ACK =1 on transmitted packet
#
# 2 AUTO_ACK[0]:1  automatic ack after RX
#
# 1 PERS_RX[0]: 1  persistent reception enabled
#
# 0 PERS_TX[0]: 1  persistent transmission enabled
#
# \endcode
##
PROTOCOL0_BASE = 0x52 ##!< Persistent RX#TX, autoack, Max number of retransmissions ##

PROTOCOL0_PERS_TX_MASK = 0x01 ##!< Enables persistent transmission ##
PROTOCOL0_PERS_RX_MASK = 0x02 ##!< Enables persistent reception ##
PROTOCOL0_AUTO_ACK_MASK = 0x04 ##!< Enables auto acknowlegment ##
PROTOCOL0_NACK_TX_MASK = 0x08 ##!< Writes field NO_ACK =1 on transmitted packet ##
PROTOCOL0_NMAX_RETX_MASK = 0xF0 ##!< Retransmission mask ##

###
# @}
##

### @defgroup TIMERS5_Register
# @{
##

###
#\brief TIMERS5register
#\code
# Default value: 0x00
# Read Write
# 7:0 RX_TIMEOUT_PRESCALER[7:0] : RX operation timeout: prescaler value
# \endcode
##
TIMERS5_RX_TIMEOUT_PRESCALER_BASE = 0x53 ##!< RX operation timeout: prescaler value ##

###
# @}
##

### @defgroup TIMERS4_Register
# @{
##

###
#\brief TIMERS4register
#\code
# Default value: 0x00
# Read Write
# 7:0 RX_TIMEOUT_COUNTER[7:0] : RX operation timeout: counter value
# \endcode
##
TIMERS4_RX_TIMEOUT_COUNTER_BASE = 0x54 ##!< RX operation timeout: counter value ##

###
# @}
##

### @defgroup TIMERS3_Register
# @{
##

###
#\brief TIMERS3register
#\code
# Default value: 0x00
# Read Write
# 7:0 LDCR_PRESCALER[7:0] : LDC Mode: Prescaler part of the wakeup value
# \endcode
##
TIMERS3_LDC_PRESCALER_BASE = 0x55 ##!< LDC Mode: Prescaler of the wakeup timer ##

###
# @}
##

### @defgroup TIMERS2_Register
# @{
##

###
#\brief TIMERS2register
#\code
# Default value: 0x00
# Read Write
# 7:0 LDCR_COUNTER[7:0] :LDC Mode: counter part of the wakeup value
# \endcode
##
TIMERS2_LDC_COUNTER_BASE = 0x56 ##!< LDC Mode: counter of the wakeup timer ##

###
# @}
##

### @defgroup TIMERS1_Register
# @{
##

###
#\brief TIMERS1register
#\code
# Default value: 0x00
# Read Write
# 7:0 LDCR_RELOAD_PRESCALER[7:0] : LDC Mode: Prescaler part of the reload value
# \endcode
##
TIMERS1_LDC_RELOAD_PRESCALER_BASE = 0x57 ##!< LDC Mode: Prescaler part of the reload value ##

###
# @}
##

### @defgroup TIMERS0_Register
# @{
##

###
#\brief TIMERS0register
#\code
# Default value: 0x00
# Read Write
# 7:0 LDCR_RELOAD_COUNTER[7:0] : LDC Mode: Counter part of the reload value
# \endcode
##
TIMERS0_LDC_RELOAD_COUNTER_BASE = 0x58 ##!< LDC Mode: Counter part of the reload value ##

###
# @}
##


### @defgroup CSMA_CONFIG3_Register
# @{
##

###
#\brief CSMA_CONFIG3registers
#\code
# Default value: 0xFF
# Read Write
# 7:0 BU_COUNTER_SEED_MSByte: Seed of the random number generator used to apply the BEB Binary Exponential Backoff algorithm MSB
# \endcode
##
CSMA_CONFIG3_BASE = 0x64 ##!< CSMA#CA: Seed of the random number generator used to apply the BEB Binary Exponential Backoff algorithm MSB ##

###
# @}
##

### @defgroup CSMA_CONFIG2_Register
# @{
##

###
#\brief CSMA_CONFIG2registers
#\code
# Default value: 0x00
# Read Write
# 7:0 BU_COUNTER_SEED_LSByte: Seed of the random number generator used to apply the BEB Binary Exponential Backoff algorithm LSB
# \endcode
##
CSMA_CONFIG2_BASE = 0x65 ##!< CSMA#CA: Seed of the random number generator used to apply the BEB Binary Exponential Backoff algorithm LSB ##

###
# @}
##

### @defgroup CSMA_CONFIG1_Register
# @{
##

###
#\brief CSMA_CONFIG1registers
#\code
# Default value: 0x04
# Read Write
# 7:2 BU_PRESCALER[5:0]: Used to program the backoff unit BU
#
# 1:0 CCA_PERIOD[1:0]: Used to program the Tcca time 64 # 128 #256 # 512  Tbit.
# \endcode
##
CSMA_CONFIG1_BASE = 0x66 ##!< CSMA#CA: Prescaler of the backoff time unit BU; CCA period ##

CSMA_CCA_PERIOD_64TBIT = 0x00 ##!< CSMA#CA: Sets CCA period to 64#TBIT ##
CSMA_CCA_PERIOD_128TBIT = 0x01 ##!< CSMA#CA: Sets CCA period to 128#TBIT ##
CSMA_CCA_PERIOD_256TBIT = 0x02 ##!< CSMA#CA: Sets CCA period to 256#TBIT ##
CSMA_CCA_PERIOD_512TBIT = 0x03 ##!< CSMA#CA: Sets CCA period to 512#TBIT ##

###
# @}
##

### @defgroup CSMA_CONFIG0_Register
# @{
##

###
#\brief CSMA_CONFIG0registers
#\code
# Default value: 0x00
# Read Write
# 7:4 CCA_LENGTH[3:0]: Used to program the Tlisten time
#
# 3 Reserved.
#
# 2:0 NBACKOFF_MAX[2:0]: Max number of backoff cycles.
# \endcode
##
CSMA_CONFIG0_BASE = 0x67 ##!< CSMA#CA: CCA lenght; Max number of backoff cycles ##

###
# @}
##

###
# @}
##


### @defgroup Link_Quality_Registers
# @{
##

### @defgroup QI_Register
# @{
##

###
#\brief QI register
#\code
# Read Write
# Default value: 0x02
#
# 7:6 SQI_TH[1:0]: SQI threshold according to the formula: 8#SYNC_LEN  2#SQI_TH
#
# 5:2 PQI_TH[3:0]: PQI threshold according to the formula: 4#PQI_THR
#
#
# 1 SQI_EN[0]:SQI enable
# 1  Enable
# 0  Disable
#
# 0 PQI_EN[0]: PQI enable
# 1  Enable
# 0  Disable
# \endcode
##
QI_BASE = 0x3A ##!< QI register ##

QI_PQI_MASK = 0x01 ##!< PQI enable#disable##
QI_SQI_MASK = 0x02 ##!< SQI enable#disable##

###
# @}
##

### @defgroup LINK_QUALIF2
# @{
##

###
#\brief LINK_QUALIF2registers
#\code
# Default value: 0x00
# Read
#
# 7:0 PQI[7:0]: PQI value of the received packet
# \endcode
##
LINK_QUALIF2_BASE = 0xC5 ##!< PQI value of the received packet ##

###
# @}
##

### @defgroup LINK_QUALIF1
# @{
##

###
#\brief LINK_QUALIF1registers
#\code
# Default value: 0x00
# Read
#
# 7 CS:Carrier Sense indication
#
# 6:0 SQI[6:0]: SQI value of the received packet
# \endcode
##
LINK_QUALIF1_BASE = 0xC6 ##!< Carrier sense indication [7]; SQI value of the received packet ##

LINK_QUALIF1_CS = 0x80 ##!< Carrier sense indication [7] ##

###
# @}
##

### @defgroup LINK_QUALIF0
# @{
##

###
#\brief LINK_QUALIF0registers
#\code
# Default value: 0x00
# Read
#
# 7:4 LQI [3:0]:LQI value of the received packet
#
# 3:0 AGC_WORD[3:0]: AGC word of the received packet
# \endcode
##
LINK_QUALIF0_BASE = 0xC7 ##!< LQI value of the received packet [7:4]; AGC word of the received packet [3:0] ##

###
# @}
##

### @defgroup RSSI_LEVEL
# @{
##

###
#\brief RSSI_LEVELregisters
#\code
# Default value: 0x00
# Read
#
# 7:0 RSSI_LEVEL[7:0]:RSSI level of the received packet
# \endcode
##
RSSI_LEVEL_BASE = 0xC8 ##!< RSSI level of the received packet ##

###
# @}
##

### @defgroup RSSI_FLT_Register
# @{
##

###
#\brief RSSI register
#\code
# Read Write
# Default value: 0xF3
# 7:4RSSI_FLT[3:0]: Gain of the RSSI filter
#
# 3:2CS_MODE[1:0]: AFC loop gain in slow mode 2's log
#
#CS_MODE1 |CS_MODE0 | CS Mode
# 
# 0 | 0 |Static CS
# 0 | 1 |Dynamic CS with 6dB dynamic threshold
# 1 | 0 |Dynamic CS with 12dB dynamic threshold
# 1 | 1 |Dynamic CS with 18dB dynamic threshold
#
# 1:0 OOK_PEAK_DECAY[1:0]: Peak decay control for OOK: 3 slow decay; 0 fast decay
#
# \endcode
##
RSSI_FLT_BASE = 0x21 ##!< Gain of the RSSI filter; lower value is fast but inaccurate,
# higher value is slow and more accurate ##
RSSI_FLT_CS_MODE_MASK = 0x0C ##!< Carrier sense mode mask ##
RSSI_FLT_CS_MODE_STATIC = 0x00 ##!< Carrier sense mode;static carrier sensing ##
RSSI_FLT_CS_MODE_DYNAMIC_6 = 0x04 ##!< Carrier sense mode;dynamic carrier sensing with 6dB threshold ##
RSSI_FLT_CS_MODE_DYNAMIC_12 = 0x08 ##!< Carrier sense mode;dynamic carrier sensing with 12dB threshold ##
RSSI_FLT_CS_MODE_DYNAMIC_18 = 0x0C ##!< Carrier sense mode;dynamic carrier sensing with 18dB threshold ##
RSSI_FLT_OOK_PEAK_DECAY_MASK = 0x03 ##!< Peak decay control for OOK mask ##
RSSI_FLT_OOK_PEAK_DECAY_FAST = 0x00 ##!< Peak decay control for OOK: fast decay ##
RSSI_FLT_OOK_PEAK_DECAY_MEDIUM_FAST = 0x01 ##!< Peak decay control for OOK: medium_fast decay ##
RSSI_FLT_OOK_PEAK_DECAY_MEDIUM_SLOW = 0x02 ##!< Peak decay control for OOK: medium_fast decay ##
RSSI_FLT_OOK_PEAK_DECAY_SLOW = 0x03 ##!< Peak decay control for OOK: slow decay ##

###
# @}
##

### @defgroup RSSI_TH_Register
# @{
##

###
#\brief RSSI_TH register
#\code
# Read Write
# Default value: 0x24
#
# 7:0 RSSI_THRESHOLD [7:0]:Signal detect threshold in 0.5dB.120dBm corresponds to 20
# \endcode
##
RSSI_TH_BASE = 0x22 ##!< Signal detect threshold in 0.5dB stp. 20 correspond to 120 dBm ##

###
# @}
##

###
# @}
##


### @defgroup FIFO_Registers
# @{
##

### @defgroup FIFO_CONFIG3_Register
# @{
##

###
#\brief FIFO_CONFIG3registers
#\code
# Default value: 0x30
# Read Write
# 7Reserved.
#
# 6:0rxafthr [6:0]: FIFO Almost Full threshold for rx fifo.
#
# \endcode
##
FIFO_CONFIG3_RXAFTHR_BASE = 0x3E ##!< FIFO Almost Full threshold for rx fifo [6:0] ##

###
# @}
##

### @defgroup FIFO_CONFIG2_Register
# @{
##

###
#\brief FIFO_CONFIG2registers
#\code
# Default value: 0x30
# Read Write
# 7Reserved.
#
# 6:0rxaethr [6:0]: FIFO Almost Empty threshold for rx fifo.
#
# \endcode
##
FIFO_CONFIG2_RXAETHR_BASE = 0x3F ##!< FIFO Almost Empty threshold for rx fifo [6:0] ##

###
# @}
##

### @defgroup FIFO_CONFIG1_Register
# @{
##

###
#\brief FIFO_CONFIG1registers
#\code
# Default value: 0x30
# Read Write
# 7Reserved.
#
# 6:0txafthr [6:0]: FIFO Almost Full threshold for tx fifo.
#
# \endcode
##
FIFO_CONFIG1_TXAFTHR_BASE = 0x40 ##!< FIFO Almost Full threshold for tx fifo [6:0] ##

###
# @}
##

### @defgroup FIFO_CONFIG0_Register
# @{
##

###
#\brief FIFO_CONFIG0registers
#\code
# Default value: 0x30
# Read Write
# 7Reserved.
#
# 6:0txaethr [6:0]: FIFO Almost Empty threshold for tx fifo.
#
# \endcode
##
FIFO_CONFIG0_TXAETHR_BASE = 0x41 ##!< FIFO Almost Empty threshold for tx fifo [6:0] ##

###
# @}
##

### @defgroup LINEAR_FIFO_STATUS1_Register
# @{
##

###
#\brief LINEAR_FIFO_STATUS1registers
#\code
# Default value: 0x00
# Read
#
# 7 Reserved.
#
# 6:0 elem_txfifo[6:0]: Number of elements in the linear TXFIFO < =96
# \endcode
##
LINEAR_FIFO_STATUS1_BASE = 0xE6 ##!< Number of elements in the linear TX FIFO [6:0] < =96 ##

###
# @}
##

### @defgroup LINEAR_FIFO_STATUS0_Register
# @{
##

###
#\brief LINEAR_FIFO_STATUS0registers
#\code
# Default value: 0x00
# Read
#
# 7 Reserved.
#
# 6:0 elem_rxfifo[6:0]: Number of elements in the linear RXFIFO < =96
# \endcode
##
LINEAR_FIFO_STATUS0_BASE = 0xE7 ##!< Number of elements in the linear RX FIFO [6:0] < =96 ##

###
# @}
##


###
# @}
##


### @defgroup Calibration_Registers
# @{
##

### @defgroup RCO_VCO_CALIBR_IN2_Register
# @{
##

###
#\brief RCO_VCO_CALIBR_IN2registers
#\code
# Default value: 0x70
# Read Write
# 7:4 RWT_IN[3:0]: RaWThermometric word value for the RCO [7:4]
#
# 3:0 RFB_IN[4:1]: ResistorFineBit word value for the RCO first 4 bits
# \endcode
##
RCO_VCO_CALIBR_IN2_BASE = 0x6D ##!< RaWThermometric word value for the RCO [7:4]; ResistorFineBit word value for the RCO [3:0] ##

###
# @}
##

### @defgroup RCO_VCO_CALIBR_IN1_Register
# @{
##

###
#\brief RCO_VCO_CALIBR_IN1registers
#\code
# Default value: 0x48
# Read Write
#
# 7 RFB_IN[0]: ResistorFineBit word value for the RCO LSb
#
# 6:0 VCO_CALIBR_TX[6:0]:Word value for the VCO to be used in TX mode
# \endcode
##
RCO_VCO_CALIBR_IN1_BASE = 0x6E ##!< ResistorFineBit word value for the RCO [7]; Word value for the VCO to be used in TX mode[6:0]##

###
# @}
##

### @defgroup RCO_VCO_CALIBR_IN0_Register
# @{
##

###
#\brief RCO_VCO_CALIBR_IN0registers
#\code
# Default value: 0x48
# Read Write
#
# 7 Reserved.
#
# 6:0 VCO_CALIBR_RX[6:0]:Word value for the VCO to be used in RX mode
# \endcode
##
RCO_VCO_CALIBR_IN0_BASE = 0x6F ##!< Word value for the VCO to be used in RX mode [6:0] ##

###
# @}
##

### @defgroup RCO_VCO_CALIBR_OUT1_Register
# @{
##

###
#\brief RCO_VCO_CALIBR_OUT1registers
#\code
# Default value: 0x00
# Read
#
# 7:4 RWT_OUT[3:0]:RWT word from internal RCO calibrator
#
# 3:0 RFB_OUT[4:1]: RFB word from internal RCO calibrator upper part
# \endcode
##
RCO_VCO_CALIBR_OUT1_BASE = 0xE4 ##!< RaWThermometric RWT word from internal RCO calibrator [7];
# ResistorFineBit RFB word from internal RCO oscillator [6:0] ##
###
# @}
##

### @defgroup RCO_VCO_CALIBR_OUT0_Register
# @{
##

###
#\brief RCO_VCO_CALIBR_OUT0registers
#\code
# Default value: 0x00
# Read
#
# 7 RFB_OUT[0]:RFB word from internal RCO calibrator last bit LSB
#
# 6:0 VCO_CALIBR_DATA[6:0]: Output word from internal VCO calibrator
# \endcode
##
RCO_VCO_CALIBR_OUT0_BASE = 0xE5 ##!< ResistorFineBit RFB word from internal RCO oscillator [0];
# Output word from internal calibrator [6:0]; ##
###
# @}
##

###
# @}
##


### @defgroup AES_Registers
# @{
##

### @defgroup AES_KEY_IN_Register
# @{
##

###
#\brief AES_KEY_INxregisters
#\code
# Default value: 0x00
# Read Write
#
# 7:0 AES_KEY_INx[7:0]:AES engine key input total  128 bits
# \endcode
##
AES_KEY_IN_15_BASE = 0x70 ##!< AES engine key input 15 ##

AES_KEY_IN_14_BASE = 0x71 ##!< AES engine key input 14 ##

AES_KEY_IN_13_BASE = 0x72 ##!< AES engine key input 13 ##

AES_KEY_IN_12_BASE = 0x73 ##!< AES engine key input 12 ##

AES_KEY_IN_11_BASE = 0x74 ##!< AES engine key input 11 ##

AES_KEY_IN_10_BASE = 0x75 ##!< AES engine key input 10 ##

AES_KEY_IN_9_BASE = 0x76 ##!< AES engine key input 9 ##

AES_KEY_IN_8_BASE = 0x77 ##!< AES engine key input 8 ##

AES_KEY_IN_7_BASE = 0x78 ##!< AES engine key input 7 ##

AES_KEY_IN_6_BASE = 0x79 ##!< AES engine key input 6 ##

AES_KEY_IN_5_BASE = 0x7A ##!< AES engine key input 5 ##

AES_KEY_IN_4_BASE = 0x7B ##!< AES engine key input 4 ##

AES_KEY_IN_3_BASE = 0x7C ##!< AES engine key input 3 ##

AES_KEY_IN_2_BASE = 0x7D ##!< AES engine key input 2 ##

AES_KEY_IN_1_BASE = 0x7E ##!< AES engine key input 1 ##

AES_KEY_IN_0_BASE = 0x7F ##!< AES engine key input 0 ##

###
# @}
##

### @defgroup AES_DATA_IN_Register
# @{
##

###
#\brief AES_DATA_INxregisters
#\code
# Default value: 0x00
# Read Write
#
# 7:0 AES_DATA_INx[7:0]:AES engine data input total  128 bits
# \endcode
##
AES_DATA_IN_15_BASE = 0x80 ##!< AES engine data input 15
# Take care: Address is in reverse order respect data numbering; eg.: 0x81 > AES_data14[7:0] ##
AES_DATA_IN_14_BASE = 0x81 ##!< AES engine data input 14 ##

AES_DATA_IN_13_BASE = 0x82 ##!< AES engine data input 13 ##

AES_DATA_IN_12_BASE = 0x83 ##!< AES engine data input 12 ##

AES_DATA_IN_11_BASE = 0x84 ##!< AES engine data input 11 ##

AES_DATA_IN_10_BASE = 0x85 ##!< AES engine data input 10 ##

AES_DATA_IN_9_BASE = 0x86 ##!< AES engine data input 9 ##

AES_DATA_IN_8_BASE = 0x87 ##!< AES engine data input 8 ##

AES_DATA_IN_7_BASE = 0x88 ##!< AES engine data input 7 ##

AES_DATA_IN_6_BASE = 0x89 ##!< AES engine data input 6 ##

AES_DATA_IN_5_BASE = 0x8A ##!< AES engine data input 5 ##

AES_DATA_IN_4_BASE = 0x8B ##!< AES engine data input 4 ##

AES_DATA_IN_3_BASE = 0x8C ##!< AES engine data input 3 ##

AES_DATA_IN_2_BASE = 0x8D ##!< AES engine data input 2 ##

AES_DATA_IN_1_BASE = 0x8E ##!< AES engine data input 1 ##

AES_DATA_IN_0_BASE = 0x8F ##!< AES engine data input 0 ##

###
# @}
##

### @defgroup AES_DATA_OUT_Register
# @{
##

###
#\brief AES_DATA_OUT[15:0]registers
#\code
# Default value: 0x00
# Read
#
# 7:0 AES_DATA_OUTx[7:0]:AES engine data output 128 bits
# \endcode
##
AES_DATA_OUT_15_BASE = 0xD4 ##!< AES engine data output 15 ##

AES_DATA_OUT_14_BASE = 0xD5 ##!< AES engine data output 14 ##

AES_DATA_OUT_13_BASE = 0xD6 ##!< AES engine data output 13 ##

AES_DATA_OUT_12_BASE = 0xD7 ##!< AES engine data output 12 ##

AES_DATA_OUT_11_BASE = 0xD8 ##!< AES engine data output 11 ##

AES_DATA_OUT_10_BASE = 0xD9 ##!< AES engine data output 10 ##

AES_DATA_OUT_9_BASE = 0xDA ##!< AES engine data output 9 ##

AES_DATA_OUT_8_BASE = 0xDB ##!< AES engine data output 8 ##

AES_DATA_OUT_7_BASE = 0xDC ##!< AES engine data output 7 ##

AES_DATA_OUT_6_BASE = 0xDD ##!< AES engine data output 6 ##

AES_DATA_OUT_5_BASE = 0xDE ##!< AES engine data output 5 ##

AES_DATA_OUT_4_BASE = 0xDF ##!< AES engine data output 4 ##

AES_DATA_OUT_3_BASE = 0xE0 ##!< AES engine data output 3 ##

AES_DATA_OUT_2_BASE = 0xE1 ##!< AES engine data output 2 ##

AES_DATA_OUT_1_BASE = 0xE2 ##!< AES engine data output 1 ##

AES_DATA_OUT_0_BASE = 0xE3 ##!< AES engine data output 0 ##

###
# @}
##

###
# @}
##

### @defgroup IRQ_Registers
# @{
##

### @defgroup IRQ_MASK0_Register
# @{
##

###
#\brief IRQ_MASK0registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_MASK0:IRQ mask, if the correspondent bit is set and IRQ can be generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#0 | RX data ready
#1 | RX data discarded upon filtering
#2 | TX data sent
#3 | Max reTX reached
#4 | CRC error
#5 | TX FIFO underflow#overflow error
#6 | RX FIFO underflow#overflow error
#7 | TX FIFO almost full
#\endcode
##


IRQ_MASK0_BASE = 0x93 ##!< IRQ_MASK is split into 4 registers##

IRQ_MASK0_RX_DATA_READY = 0x01 ##!< IRQ: RX data ready ##
IRQ_MASK0_RX_DATA_DISC = 0x02 ##!< IRQ: RX data discarded upon filtering ##
IRQ_MASK0_TX_DATA_SENT = 0x04 ##!< IRQ: TX data sent ##
IRQ_MASK0_MAX_RE_TX_REACH = 0x08 ##!< IRQ: Max reTX reached ##
IRQ_MASK0_CRC_ERROR = 0x10 ##!< IRQ: CRC error ##
IRQ_MASK0_TX_FIFO_ERROR = 0x20 ##!< IRQ: TX FIFO underflow#overflow error ##
IRQ_MASK0_RX_FIFO_ERROR = 0x40 ##!< IRQ: RX FIFO underflow#overflow error ##
IRQ_MASK0_TX_FIFO_ALMOST_FULL = 0x80 ##!< IRQ: TX FIFO almost full ##

###
# @}
##

### @defgroup IRQ_MASK1_Register
# @{
##

###
#\brief IRQ_MASK1registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_MASK1:IRQ mask, if the correspondent bit is set and IRQ can be generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#8 | TX FIFO almost empty
#9 | RX FIFO almost full
#10| RX FIFO almost empty
#11| Max number of backoff during CCA
#12| Valid preamble detected
#13| Sync word detected
#14| RSSI above threshold Carrier Sense
#15| Wakeup timeout in LDCR mode13
# \endcode
##

IRQ_MASK1_BASE = 0x92 ##!< IRQ_MASK is split into 4 registers##

IRQ_MASK1_TX_FIFO_ALMOST_EMPTY = 0x01 ##!< IRQ: TX FIFO almost empty ##
IRQ_MASK1_RX_FIFO_ALMOST_FULL = 0x02 ##!< IRQ: RX FIFO almost full ##
IRQ_MASK1_RX_FIFO_ALMOST_EMPTY = 0x04 ##!< IRQ: RX FIFO almost empty##
IRQ_MASK1_MAX_BO_CCA_REACH = 0x08 ##!< IRQ: Max number of backoff during CCA ##
IRQ_MASK1_VALID_PREAMBLE = 0x10 ##!< IRQ: Valid preamble detected ##
IRQ_MASK1_VALID_SYNC = 0x20 ##!< IRQ: Sync word detected ##
IRQ_MASK1_RSSI_ABOVE_TH = 0x40 ##!< IRQ: RSSI above threshold ##
IRQ_MASK1_WKUP_TOUT_LDC = 0x80 ##!< IRQ: Wakeup timeout in LDC mode ##

###
# @}
##

### @defgroup IRQ_MASK2_Register
# @{
##

###
#\brief IRQ_MASK2registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_MASK2:IRQ mask, if the correspondent bit is set and IRQ can be generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#16| READY state in steady condition14
#17| STANDBY state switching in progress
#18| Low battery level
#19| PowerOn reset
#20| BrownOut event
#21| LOCK state in steady condition
#22| PM startup timer expiration
#23| XO settling timeout
# \endcode
##
IRQ_MASK2_BASE = 0x91 ##!< IRQ_MASK is split into 4 registers##

IRQ_MASK2_READY = 0x01 ##!< IRQ: READY state ##
IRQ_MASK2_STANDBY_DELAYED = 0x02 ##!< IRQ: STANDBY state after MCU_CK_CONF_CLOCK_TAIL_X clock cycles ##
IRQ_MASK2_LOW_BATT_LVL = 0x04 ##!< IRQ: Battery level below threshold##
IRQ_MASK2_POR = 0x08 ##!< IRQ: Power On Reset ##
IRQ_MASK2_BOR = 0x10 ##!< IRQ: Brown out event both accurate and inaccurate##
IRQ_MASK2_LOCK = 0x20 ##!< IRQ: LOCK state ##
IRQ_MASK2_PM_COUNT_EXPIRED = 0x40 ##!< IRQ: only for debug; Power Management startup timer expiration see reg PM_START_COUNTER, 0xB5 ##
IRQ_MASK2_XO_COUNT_EXPIRED = 0x80 ##!< IRQ: only for debug; Crystal oscillator settling time counter expired ##

###
# @}
##

### @defgroup IRQ_MASK3_Register
# @{
##

###
#\brief IRQ_MASK3registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_MASK3:IRQ mask, if the correspondent bit is set and IRQ can be generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#24| SYNTH locking timeout
#25| SYNTH calibration startup time
#26| SYNTH calibration timeout
#27| TX circuitry startup time
#28| RX circuitry startup time
#29| RX operation timeout
#30| Others AES Endof Operation
#31| Reserved
# \endcode
##
IRQ_MASK3_BASE = 0x90 ##!< IRQ_MASK is split into 4 registers##

IRQ_MASK3_SYNTH_LOCK_TIMEOUT = 0x01 ##!< IRQ: only for debug; LOCK state timeout ##
IRQ_MASK3_SYNTH_LOCK_STARTUP = 0x02 ##!< IRQ: only for debug; see CALIBR_START_COUNTER ##
IRQ_MASK3_SYNTH_CAL_TIMEOUT = 0x04 ##!< IRQ: only for debug; SYNTH calibration timeout ##
IRQ_MASK3_TX_START_TIME = 0x08 ##!< IRQ: only for debug; TX circuitry startup time; see TX_START_COUNTER ##
IRQ_MASK3_RX_START_TIME = 0x10 ##!< IRQ: only for debug; RX circuitry startup time; see TX_START_COUNTER ##
IRQ_MASK3_RX_TIMEOUT = 0x20 ##!< IRQ: RX operation timeout ##
IRQ_MASK3_AES_END = 0x40 ##!< IRQ: AES End of operation ##

###
# @}
##


### @defgroup IRQ_STATUS0_Register
# @{
##

###
#\brief IRQ_STATUS0registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_STATUS0:IRQ status, if the correspondent bit is set and IRQ has been generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#0 | RX data ready
#1 | RX data discarded upon filtering
#2 | TX data sent
#3 | Max reTX reached
#4 | CRC error
#5 | TX FIFO underflow#overflow error
#6 | RX FIFO underflow#overflow error
#7 | TX FIFO almost full
# \endcode
##

IRQ_STATUS0_BASE = 0xFD ##!< IRQ EventsRR, split into 4 registers ##

IRQ_STATUS0_SYNTH_LOCK_TIMEOUT = 0x01 ##!< IRQ: LOCK state timeout ##
IRQ_STATUS0_SYNTH_LOCK_STARTUP = 0x02 ##!< IRQ: only for debug; see CALIBR_START_COUNTER ##
IRQ_STATUS0_SYNTH_CAL_TIMEOUT = 0x04 ##!< IRQ: SYNTH locking timeout ##
IRQ_STATUS0_TX_START_TIME = 0x08 ##!< IRQ: only for debug; TX circuitry startup time; see TX_START_COUNTER ##
IRQ_STATUS0_RX_START_TIME = 0x10 ##!< IRQ: only for debug; RX circuitry startup time; see TX_START_COUNTER ##
IRQ_STATUS0_RX_TIMEOUT = 0x20 ##!< IRQ: RX operation timeout expiration ##
IRQ_STATUS0_AES_END = 0x40 ##!< IRQ: AES End of operation ##

###
# @}
##

### @defgroup IRQ_STATUS1_Register
# @{
##

###
#\brief IRQ_STATUS1registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_STATUS1:IRQ status, if the correspondent bit is set and IRQ has been generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#8 | TX FIFO almost empty
#9 | RX FIFO almost full
#10| RX FIFO almost empty
#11| Max number of backoff during CCA
#12| Valid preamble detected
#13| Sync word detected
#14| RSSI above threshold Carrier Sense
#15| Wakeup timeout in LDCR mode13
# \endcode
##

IRQ_STATUS1_BASE = 0xFC ##!< IRQ EventsRR, split into 4 registers ##

IRQ_STATUS1_READY = 0x01 ##!< IRQ: READY state in steady condition##
IRQ_STATUS1_STANDBY_DELAYED = 0x02 ##!< IRQ: STANDBY state after MCU_CK_CONF_CLOCK_TAIL_X clock cycles ##
IRQ_STATUS1_LOW_BATT_LVL = 0x04 ##!< IRQ: Battery level below threshold##
IRQ_STATUS1_POR = 0x08 ##!< IRQ: Power On Reset ##
IRQ_STATUS1_BOR = 0x10 ##!< IRQ: Brown out event both accurate and inaccurate##
IRQ_STATUS1_LOCK = 0x20 ##!< IRQ: LOCK state in steady condition ##
IRQ_STATUS1_PM_COUNT_EXPIRED = 0x40 ##!< IRQ: Power Management startup timer expiration see reg PM_START_COUNTER, 0xB5 ##
IRQ_STATUS1_XO_COUNT_EXPIRED = 0x80 ##!< IRQ: Crystal oscillator settling time counter expired ##

###
# @}
##

### @defgroup IRQ_STATUS2_Register
# @{
##

###
#\brief IRQ_STATUS2registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_STATUS2:IRQ status, if the correspondent bit is set and IRQ has been generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#16| READY state in steady condition14
#17| STANDBY state switching in progress
#18| Low battery level
#19| PowerOn reset
#20| BrownOut event
#21| LOCK state in steady condition
#22| PM startup timer expiration
#23| XO settling timeout
# \endcode
##

IRQ_STATUS2_BASE = 0xFB ##!< IRQ EventsRR, split into 4 registers ##

IRQ_STATUS2_TX_FIFO_ALMOST_EMPTY = 0x01 ##!< IRQ: TX FIFO almost empty ##
IRQ_STATUS2_RX_FIFO_ALMOST_FULL = 0x02 ##!< IRQ: RX FIFO almost full ##
IRQ_STATUS2_RX_FIFO_ALMOST_EMPTY = 0x04 ##!< IRQ: RX FIFO almost empty ##
IRQ_STATUS2_MAX_BO_CCA_REACH = 0x08 ##!< IRQ: Max number of backoff during CCA ##
IRQ_STATUS2_VALID_PREAMBLE = 0x10 ##!< IRQ: Valid preamble detected ##
IRQ_STATUS2_VALID_SYNC = 0x20 ##!< IRQ: Sync word detected ##
IRQ_STATUS2_RSSI_ABOVE_TH = 0x40 ##!< IRQ: RSSI above threshold ##
IRQ_STATUS2_WKUP_TOUT_LDC = 0x80 ##!< IRQ: Wakeup timeout in LDC mode ##

###
# @}
##

### @defgroup IRQ_STATUS3_Register
# @{
##

###
#\brief IRQ_STATUS3registers
#\code
# Default value: 0x00
# Read Write
#
# 7:0 INT_STATUS3:IRQ status, if the correspondent bit is set and IRQ has been generated according to the next table
#
#Bit | Events Group Interrupt Event
# 
#24| SYNTH locking timeout
#25| SYNTH calibration startup time
#26| SYNTH calibration timeout
#27| TX circuitry startup time
#28| RX circuitry startup time
#29| RX operation timeout
#30| Others AES Endof Operation
#31| Reserved
#\endcode
##
IRQ_STATUS3_BASE = 0xFA ##!< IRQ EventsRR, split into 4 registers ##

IRQ_STATUS3_RX_DATA_READY = 0x01 ##!< IRQ: RX data ready ##
IRQ_STATUS3_RX_DATA_DISC = 0x02 ##!< IRQ: RX data discarded upon filtering ##
IRQ_STATUS3_TX_DATA_SENT = 0x04 ##!< IRQ: TX data sent ##
IRQ_STATUS3_MAX_RE_TX_REACH = 0x08 ##!< IRQ: Max reTX reached ##
IRQ_STATUS3_CRC_ERROR = 0x10 ##!< IRQ: CRC error ##
IRQ_STATUS3_TX_FIFO_ERROR = 0x20 ##!< IRQ: TX FIFO underflow#overflow error ##
IRQ_STATUS3_RX_FIFO_ERROR = 0x40 ##!< IRQ: RX FIFO underflow#overflow error ##
IRQ_STATUS3_TX_FIFO_ALMOST_FULL = 0x80 ##!< IRQ: TX FIFO almost full ##

###
# @}
##

###
# @}
##


### @defgroup MC_STATE_Registers
# @{
##

### @defgroup MC_STATE1_Register
# @{
##

###
#\brief MC_STATE1registers
#\code
# Default value: 0x50
# Read
#
# 7:4 Reserved.
#
# 3 ANT_SELECT:Currently selected antenna
#
# 2 TX_FIFO_Full: 1  TX FIFO is full
#
# 1 RX_FIFO_Empty:1  RX FIFO is empty
#
# 0 ERROR_LOCK: 1  RCO calibrator error
# \endcode
##
MC_STATE1_BASE = 0xC0 ##!< MC_STATE1 register address see the SpiritStatus struct ##


###
# @}
##


### @defgroup MC_STATE0_Register
# @{
##

###
#\brief MC_STATE0registers
#\code
# Default value: 0x00
# Read
#
# 7:1 STATE[6:0]: Current MC state.
#
#REGISTER VALUE | STATE
# 
#0x40 | STANDBY
#0x36 | SLEEP
#0x03 | READY
#0x3B | PM setup
#0x23 | XO settling
#0x53 | SYNTH setup
#0x1F | PROTOCOL
#0x4F | SYNTH calibration
#0x0F | LOCK
#0x33 | RX
#0x5F | TX
#
# 0 XO_ON: 1  XO is operating
# \endcode
##
MC_STATE0_BASE = 0xC1 ##!< MC_STATE0 register address. In this version ALL existing states have been inserted
# and are still to be verified ##
###
# @}
##

###
# @}
##

### @defgroup EngineeringTest_Registers
# @{
##

SYNTH_CONFIG1_BASE = 0x9E ##!< Synthesizier registers: M, A, K data sync on positive#negative clock edges [4],
# Enable Linearization of the charge pump [3], split time 1.75#3.45ns [2], VCO calibration window 16,32,64,128 clock cycles [1:0]##
SYNTH_CONFIG0_BASE = 0x9E ##!< Enable DSM randomizer [7], Window width 1.27.5ns Downup of lock detector##
VCOTH_BASE = 0xA0 ##!< Controls the threshold frequency between VCO low and VCO high [7:0]
# VCOth frequency =2#fXO#96+VCO_TH#16, fmin =4992 MHz, fmax =5820 MHz##
PM_CONFIG2_BASE = 0xA4 ##!< Enables high current buffer on Temperature sensor, sets SMPS options ##
PM_CONFIG1_BASE = 0xA5 ##!< Set SMPS options ##
PM_CONFIG0_BASE = 0xA6 ##!< Set SMPS options ##
VCO_CONFIG_BASE = 0xA1 ##!< Set VCO current [5:2]part and [1:0] part ##
XO_CONFIG_BASE = 0xA7 ##!< Clock management options from XO to digital part ##

XO_RCO_TEST_BASE = 0xB4 ##!< Test of XO and RCO ##

###
# @}
##


### @addtogroup Commands
# @{
##

COMMAND_TX = 0x60 ##!< Start to transmit; valid only from READY ##
COMMAND_RX = 0x61 ##!< Start to receive; valid only from READY ##
COMMAND_READY = 0x62 ##!< Go to READY; valid only from STANDBY or SLEEP or LOCK ##
COMMAND_STANDBY = 0x63 ##!< Go to STANDBY; valid only from READY ##
COMMAND_SLEEP = 0x64 ##!< Go to SLEEP; valid only from READY ##
COMMAND_LOCKRX = 0x65 ##!< Go to LOCK state by using the RX configuration of the synth; valid only from READY ##
COMMAND_LOCKTX = 0x66 ##!< Go to LOCK state by using the TX configuration of the synth; valid only from READY ##
COMMAND_SABORT = 0x67 ##!< Force exit form TX or RX states and go to READY state; valid only from TX or RX ##
COMMAND_LDC_RELOAD = 0x68 ##!< LDC Mode: Reload the LDC timer with the value stored in theLDC_PRESCALER # COUNTER
# registers; valid from all states##
COMMAND_SEQUENCE_UPDATE = 0x69 ##!< Autoretransmission: Reload the Packet sequence counter with the value stored in the PROTOCOL[2] register
# valid from all states ##
COMMAND_AES_ENC = 0x6A ##!< AES: Start the encryption routine; valid from all states; valid from all states ##
COMMAND_AES_KEY = 0x6B ##!< AES: Start the procedure to compute the key for the decryption; valid from all states ##
COMMAND_AES_DEC = 0x6C ##!< AES: Start the decryption routine using the current key; valid from all states ##
COMMAND_AES_KEY_DEC = 0x6D ##!< AES: Compute the key and start the decryption; valid from all states ##
COMMAND_IQC_INIT_LOAD = 0x6E ##!< Load the IQC word in IQC_CORRECT_OUT [2:0] from IQC_CORRECT_IN[2:0] registers; it is
# used to let the IQ correction parameters for image rejection evolve from packet to packet instead of restarting at each packet; valid from all states TBC ##
COMMAND_SRES = 0x70 ##!< Reset of all digital part, except SPI registers ##
COMMAND_FLUSHRXFIFO = 0x71 ##!< Clean the RX FIFO; valid from all states ##
COMMAND_FLUSHTXFIFO = 0x72 ##!< Clean the TX FIFO; valid from all states ##

###
# @}
##

###
# @}
##

#ifdef __cplusplus
# }
#endif

#endif

#################### C COPYRIGHT 2012 STMicroelectronics #####END OF FILE#####

# Contact GitHub API Training Shop Blog About 


