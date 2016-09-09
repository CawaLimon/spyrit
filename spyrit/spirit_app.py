import sys
import pyboard
import ast
import spirit_regs
import register_table

from PyQt4 import QtGui
from PyQt4 import QtCore

from widgets import functions
from widgets import labels

from spirit1 import spirit_status

ICON_PATH = "./assets/logosmall.png"

class SerialConnect(QtGui.QWidget):
    def __init__(self, notifyFunc=None, parent=None):
        super(SerialConnect, self).__init__(parent)
        self.registers = register_table.RegisterModel(self)
        self.callbackFunc = notifyFunc
        
        self.portsList = QtGui.QComboBox()
        self.portsList.addItems(functions.listSerialPorts())
        self.portsList.setMinimumWidth(300)
        
        self.toggleButton = QtGui.QPushButton('Open')
        self.toggleButton.clicked.connect(self.togglePort)
        
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.portsList)
        layout.addWidget(self.toggleButton)
        layout.addStretch(1)
        
    def togglePort(self):
        if self.toggleButton.text() == "Open":
            try:
                self.open(str(self.portsList.currentText()))
            except:
                QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                                   "Invalid Device",
                                   "Please choose another device.").exec_()
                return
            self.portsList.setEnabled(False)
            self.toggleButton.setText("Close")
            self.pyboard.exec_("import spirit1")
            self.pyboard.exec_("spir = spirit1.SPIRIT1(1)")
            for key in self.registers.registers:
                self.readRegisters(key)
        else:
            self.close()
            self.portsList.setEnabled(True)
            self.toggleButton.setText("Open")
            
    def open(self, port):
        self.pyboard = pyboard.Pyboard(port)
        self.pyboard.enter_raw_repl()
        
    def close(self):
        self.pyboard.exit_raw_repl()
        self.pyboard.close()
    
    def writeRegisters(self, regAddress, values):
        cmd = "print(spir.writeRegisters(%d, bytearray(%s)))" % (regAddress, values)
        f, _ = self.pyboard.exec_raw(cmd)
        f = ast.literal_eval(f)
        if self.callbackFunc:
            self.callbackFunc(f[:2])
        self.readRegisters(regAddress, len(values))
        return f
        
    def readRegisters(self, regAddress, numBytes=1):
        cmd = "print(spir.readRegisters(%d, numBytes=%d))" % (regAddress, numBytes)
        f, _ =  self.pyboard.exec_raw(cmd)
        f = ast.literal_eval(f)
        self.registers.updateRegister(regAddress, f[2:])
        if self.callbackFunc:
            self.callbackFunc(f[:2])
        return f
    
    def getRegisterModel(self):
        return self.registers
    
    def sendCommand(self, commandCode):
        self._send_receive(bytearray([0x80, commandCode]))
        
    def writeLinearFifo(self, buff):
        self._send_receive(bytearray([0x00, 0xFF]) + buff)
        
    def readLinearFifo(self, numBytes=1):
        return self._send_receive(bytearray([0x01, 0xFF]) + bytearray(numBytes))
    
    def setCallback(self, callbackFunc):
        self.callbackFunc = callbackFunc
        
class Status(QtGui.QWidget):
    def __init__(self, serial, parent=None):
        super(Status, self).__init__(parent)
        self.serial = serial
        #Status displays
        self.XO_On = labels.Switch()
        self.XO_On.setAlignment(QtCore.Qt.AlignRight)
        self.errorLock = labels.Switch()
        self.errorLock.setAlignment(QtCore.Qt.AlignRight)
        self.rxFifoEmpty = labels.Switch()
        self.rxFifoEmpty.setAlignment(QtCore.Qt.AlignRight)
        self.txFifoFull = labels.Switch()
        self.txFifoFull.setAlignment(QtCore.Qt.AlignRight)
        self.antSelect = labels.Switch()
        self.antSelect.setAlignment(QtCore.Qt.AlignRight)
        self.state = QtGui.QLabel("Unk")
        self.state.setAlignment(QtCore.Qt.AlignRight)
        
        self.updateStatusButton = QtGui.QPushButton("Refresh Status")
        self.updateStatusButton.clicked.connect(self.updateStatus)
        
        statusLayout = QtGui.QFormLayout(self)
        statusLayout.addRow("State:", self.state)
        statusLayout.addRow("XO On:", self.XO_On)
        statusLayout.addRow("Error Lock:", self.errorLock)
        statusLayout.addRow("RX FIFO Empty:", self.rxFifoEmpty)
        statusLayout.addRow("TX FIFO Full", self.txFifoFull)
        statusLayout.addRow("ANT Select:", self.antSelect)
        statusLayout.addRow(self.updateStatusButton)
        
    def updateStatus(self):
        output = self.serial.readRegisters(spirit_regs.MC_STATE1_BASE, 2)
        self.parse_status(output[2:])
        
    def parse_status(self, statusBuff):
        self.XO_On.set_on(statusBuff[1] & 0x01)
        self.errorLock.set_on(statusBuff[0]  & 0x01)
        self.rxFifoEmpty.set_on(statusBuff[0] & 0x02)
        self.txFifoFull.set_on(statusBuff[0] & 0x04)
        self.antSelect.set_on(statusBuff[0] & 0x08)
        
        state = statusBuff[1] >> 1
        if state == spirit_status.STATE_LOCK:
            self.state.setText("LOCK")
        elif state == spirit_status.STATE_PM_SETUP:
            self.state.setText("PM SETUP")
        elif state == spirit_status.STATE_PROTOCOL:
            self.state.setText("PROTOCOL")
        elif state == spirit_status.STATE_READY:
            self.state.setText("READY")
        elif state == spirit_status.STATE_RX:
            self.state.setText("RX")
        elif state == spirit_status.STATE_SLEEP:
            self.state.setText("SLEEP")
        elif state == spirit_status.STATE_STANDBY:
            self.state.setText("STANDBY")
        elif state == spirit_status.STATE_SYNTH_CALIBRATION:
            self.state.setText("SYNTH CAL")
        elif state == spirit_status.STATE_SYNTH_SETUP:
            self.state.setText("SYNTH SETUP")
        elif state == spirit_status.STATE_TX:
            self.state.setText("TX")
        elif state == spirit_status.STATE_XO_SETTLING:
            self.state.setText("XO SETTLING")
        else:
            self.state.setText("Unk")
            
class LowLevelCommands(QtGui.QWidget):
    def __init__(self, serial, parent=None):
        super(LowLevelCommands, self).__init__(parent)
        self.serial = serial
        
        #Register ops
        self.addressInput = labels.HexInput('00')
        
        self.readLine = labels.HexInput('00')
        self.readLine.setReadOnly(True)
        
        self.readButton = QtGui.QPushButton("Read")
        self.readButton.clicked.connect(self.readRegister)
        
        self.writeLine = labels.HexInput('00')
        
        self.writeButton = QtGui.QPushButton("Write")
        self.writeButton.clicked.connect(self.writeRegister)
        
        #layout
        regLayout = QtGui.QGridLayout(self)
        regLayout.addWidget(QtGui.QLabel("Address:"), 0, 0)
        regLayout.addWidget(self.addressInput, 0, 1)
        regLayout.addWidget(self.readLine, 1, 0)
        regLayout.addWidget(self.readButton, 1, 1)
        regLayout.addWidget(self.writeLine, 2, 0)
        regLayout.addWidget(self.writeButton, 2, 1)
        regLayout.addWidget(functions.addSpacer(), 3, 0)
        
    def readRegister(self):
        output = self.serial.readRegisters(self.addressInput.value())
        self.readLine.setValue(output[-1])
        
    def writeRegister(self):
        self.serial.writeRegisters(self.addressInput.value(), [self.writeLine.value()])
        
MODULATION = {"FSK":0x00,
              "GFSK BT05":0x50,
              "GFSK BT1":0x10,
              "ASK_OOK":0x20,
              "MSK":0x30}

POWER_SEL = {"Normal":0x00,
             "Boost":0x00,
             "PA":0x00}
        
class RadioSetting(QtGui.QGroupBox):
    def __init__(self, title='Radio Setting', parent=None):
        super(RadioSetting, self).__init__(title, parent)
        
        self.freqBaseInput = QtGui.QDoubleSpinBox()
        self.freqBaseInput.setRange(0.0, 1000.0)
        self.freqBaseInput.setSuffix(" MHz")
        
        self.dataRateInput = QtGui.QDoubleSpinBox()
        self.dataRateInput.setRange(100.0, 500000.0)
        self.dataRateInput.setSuffix(" bps")
        
        self.fDevInput = QtGui.QDoubleSpinBox()
        self.fDevInput.setSuffix(" kHz")
        
        self.channelFilterInput = QtGui.QDoubleSpinBox()
        self.channelFilterInput.setSuffix(" kHz")
        
        self.modInput = QtGui.QComboBox()
        self.modInput.addItems(MODULATION.keys())
        
        self.outputPowerInput = QtGui.QSpinBox()
        self.outputPowerInput.setSuffix(" dBm")
        
        self.outputPowerModeInput = QtGui.QComboBox()
        self.outputPowerModeInput.addItems(POWER_SEL.keys())
        
        self.configurePAButton = QtGui.QPushButton("CONFIGURE PA..")
        
        self.maxPowerCheckBox = QtGui.QCheckBox("MAX Power")
        
        self.configureRadioButton = QtGui.QPushButton("CONFIGURE RADIO")
        
        self.testRFBox = QtGui.QGroupBox("Test RF")
        testRfLayout = QtGui.QVBoxLayout(self.testRFBox)
        self.txCwStartButton = QtGui.QPushButton("TX CW START")
        self.txPn9StartButton = QtGui.QPushButton("TX PN9 START")
        testRfLayout.addWidget(self.txCwStartButton)
        testRfLayout.addWidget(self.txPn9StartButton)
        
        l1 = QtGui.QFormLayout()
        l1.addRow("Frequency Base", self.freqBaseInput)
        l1.addRow("Data Rate", self.dataRateInput)
        l1.addRow("Frequency Deviation", self.fDevInput)
        l1.addRow("Channel Filter", self.channelFilterInput)
        
        l2 = QtGui.QFormLayout()
        l2.addRow("Modulation", self.modInput)
        l2.addRow("Power Mode", self.outputPowerModeInput)
        l2.addRow("Output Power", self.outputPowerInput)
        l2.addRow(self.maxPowerCheckBox)
        
        l3 = QtGui.QVBoxLayout()
        l3.addWidget(self.configurePAButton)
        l3.addWidget(self.configureRadioButton)
        
        layout = QtGui.QHBoxLayout(self)
        layout.addLayout(l1)
        layout.addLayout(l2)
        layout.addLayout(l3)
        layout.addWidget(self.testRFBox)
        
class PacketSetting(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PacketSetting, self).__init__(parent)
        self.stackRadioButton = QtGui.QRadioButton("Stack")
        self.wmbusRadioButton = QtGui.QRadioButton("WM-Bus")
        self.wmbusRadioButton.setEnabled(False)
        self.basicRadioButton = QtGui.QRadioButton("Basic")
        self.basicRadioButton.setChecked(True)
        
        packetFormatGroup = QtGui.QGroupBox("Packet Format")
        pfL = QtGui.QVBoxLayout(packetFormatGroup)
        pfL.addWidget(self.basicRadioButton)
        pfL.addWidget(self.stackRadioButton)
        pfL.addWidget(self.wmbusRadioButton)
        
        self.stackPacketConfig = STackPacketConfig()
        self.basicRadioConfig = BasicPacketConfig()
        
        layout = QtGui.QHBoxLayout(self)
        pfLayout = QtGui.QVBoxLayout()
        pfLayout.addWidget(self.basicRadioConfig)
        pfLayout.addWidget(self.stackPacketConfig)
        
        lsLayout = QtGui.QVBoxLayout()
        lsLayout.addWidget(packetFormatGroup)
        lsLayout.addStretch(1)
        
        layout.addLayout(lsLayout)
        layout.addLayout(pfLayout)
        
class STackPacketConfig(QtGui.QGroupBox):
    def __init__(self, title='STack Packet Config', parent=None):
        super(STackPacketConfig, self).__init__(title, parent)
            
        self.preambleLenInput = QtGui.QSpinBox()
        self.preambleLenInput.setSuffix(" bytes")
        self.preambleLenInput.setRange(1, 32)
        
        self.syncInput = labels.HexInput()
        self.syncInput.lineEdit.setMaxLength(8)
        self.syncInput.lineEdit.setText("88888888")
        
        self.destinationAddressInput = labels.HexInput()
        self.destinationAddressInput.lineEdit.setPlaceholderText("optional")
        self.sourceAddressInput = labels.HexInput()
        
        self.controlFieldInput = labels.HexInput()
        self.controlFieldInput.lineEdit.setMaxLength(8)
        
        layout = QtGui.QFormLayout(self)
        layout.addRow("Preamble Length", self.preambleLenInput)
        layout.addRow("Sync Word", self.syncInput)
        layout.addRow("Destination Address", self.destinationAddressInput)
        layout.addRow("Source Address", self.sourceAddressInput)
        layout.addRow("Control", self.controlFieldInput)
        
class BasicPacketConfig(QtGui.QGroupBox):
    def __init__(self, title="Basic Packet Config", parent=None):
        super(BasicPacketConfig, self).__init__(title, parent)
        
        self.preambleLenInput = QtGui.QSpinBox()
        self.preambleLenInput.setSuffix(" bytes")
        self.preambleLenInput.setRange(1, 32)
        
        self.syncInput = labels.HexInput()
        self.syncInput.lineEdit.setMaxLength(8)
        self.syncInput.lineEdit.setText("88888888")
        
        self.destinationAddressInput = labels.HexInput()
        self.destinationAddressInput.lineEdit.setPlaceholderText("optional")
        
        self.controlInput = labels.HexInput()
        self.controlInput.lineEdit.setMaxLength(8)
        
        layout = QtGui.QFormLayout(self)
        layout.addRow("Preamble Length", self.preambleLenInput)
        layout.addRow("Sync Word", self.syncInput)
        layout.addRow("Destination Address", self.destinationAddressInput)
        layout.addRow("Control", self.controlInput)
        
class TransmissionView(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TransmissionView, self).__init__(parent)
        
class TXView(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TXView, self).__init__(parent)
        
        self.payloadInput = QtGui.QLineEdit("FIRECODE")
        
        self.encryptCheckBox = QtGui.QCheckBox("Encrypt")
        self.encryptionKeyInput = QtGui.QLineEdit()
        
        self.totalPacketsInput = QtGui.QSpinBox()
        self.totalPacketsInput.setRange(0, 500)
        self.totalPacketsInput.setValue(10)
        
        self.timer = QtGui.QSpinBox()
        self.timer.setRange(0, 1000000)
        self.timer.setValue(500)
        self.timer.setSuffix(" ms")
        
        self.lowPowerCheckBox = QtGui.QCheckBox("Low Power")
        
        self.startButton = QtGui.QPushButton("START")
        
class RXView(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RXView, self).__init__(parent)
        
        
class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self.serial = SerialConnect()
        self.registerTable = register_table.RegisterTable(self.serial.getRegisterModel())
        
        dockWidget = QtGui.QDockWidget()
        dockWidget.setWidget(self.registerTable.widget)
        dockWidget.setMinimumWidth(560)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dockWidget)
        
        lowLevelCommandTab = QtGui.QWidget()
        lllayout = QtGui.QHBoxLayout(lowLevelCommandTab)
        self.lowLevel = LowLevelCommands(self.serial)
        self.status = Status(self.serial)
        lllayout.addWidget(self.lowLevel)
        lllayout.addWidget(self.status)
        lllayout.addStretch(1)
        
        packetConfigTab = PacketSetting()
        
        self.serial.setCallback(self.status.parse_status)
        
        self.radioSetting = RadioSetting()
        
        commandTabWidget = QtGui.QTabWidget()
        commandTabWidget.addTab(packetConfigTab, "Packet Setting")
        commandTabWidget.addTab(lowLevelCommandTab, "Low Level Command")
        
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.addWidget(self.serial)
        layout.addWidget(self.radioSetting)
        layout.addWidget(commandTabWidget)
        
        self.setCentralWidget(widget)
        
def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(ICON_PATH))
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()