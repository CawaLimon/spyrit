from PyQt4 import QtGui
from PyQt4 import QtCore

import buttons
import functions
from configs import LabelDirection

from re import compile

IP_REGEX = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
DEFAULT_PEER_IP = "" #"10.1.2.0"

class IPDialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(IPDialog, self).__init__(parent)
        
        self.setWindowTitle("Get IP")
        
        self.ipEdit = QtGui.QLineEdit()
        self.ipEdit.setText(DEFAULT_PEER_IP)
        
        self.IPRegex = compile(IP_REGEX)
        
        okButton = QtGui.QPushButton('OK')
        okButton.setDefault(True)
        okButton.clicked.connect(self.proceed)
        cancelButton = QtGui.QPushButton('Cancel')
        cancelButton.clicked.connect(self.reject)
        
        form = QtGui.QHBoxLayout()
        form.addWidget(QtGui.QLabel('IP:'))
        form.addWidget(self.ipEdit)
        
        self.message = QtGui.QLabel("")
        self.message.setStyleSheet("font-size : %dpt;" % 5)
        self.message.setAlignment(QtCore.Qt.AlignRight)
        
        bottom = QtGui.QHBoxLayout()
        bottom.addStretch(1)
        bottom.addWidget(cancelButton)
        bottom.addWidget(okButton)
        
        layout = QtGui.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.message)
        layout.addLayout(bottom)
        
    def run(self):
        return self.exec_(), str(self.ipEdit.text())
    
    def proceed(self):
        self.accept()
        if self.IPRegex.match(str(self.ipEdit.text())) is not None:
            self.accept()
        else:
            self.message.setText("invalid IP expression")
            
class ImageViewDialog(QtGui.QDialog):
    def __init__(self, file_loc, parent=None):
        super(ImageViewDialog, self).__init__(parent)
        self.setWindowTitle(file_loc)
        self.setWindowFlags(self.windowFlags() |
                              QtCore.Qt.WindowSystemMenuHint |
                              QtCore.Qt.WindowMinMaxButtonsHint)
        
        self.scene = QtGui.QGraphicsScene()
        self.view = QtGui.QGraphicsView(self.scene)
        
        self.pixmap = QtGui.QPixmap(file_loc)
        self.zoom_step = 0.04 
        self.scene.addPixmap(self.pixmap)

        self.ctrl_pressed = False
         
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
         
    def wheelEvent(self, event):
        if self.ctrl_pressed:
            numDegrees = event.delta() / 8
            numSteps = numDegrees / 15.0
            self.zoom(numSteps)
            event.accept()
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrl_pressed = True
            
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrl_pressed = False

    def zoom(self, step):
        self.scene.clear()
        w = self.pixmap.size().width()
        h = self.pixmap.size().height()
        w, h = w * (1 + self.zoom_step*step), h * (1 + self.zoom_step*step)
        self.pixmap = self.pixmap.scaled(w, h,
                                            QtCore.Qt.KeepAspectRatio,
                                            QtCore.Qt.FastTransformation)
        self.view_current() 
        
    def view_current(self):
        size_img = self.pixmap.size()
        wth, hgt = QtCore.QSize.width(size_img), QtCore.QSize.height(size_img)
        self.scene.clear()
        self.scene.setSceneRect(0, 0, wth, hgt)
        self.scene.addPixmap(self.pixmap)
        QtCore.QCoreApplication.processEvents()
        
class ConfigDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.setModal(False)
        
        self.layout = QtGui.QFormLayout()
        
        b = QtGui.QHBoxLayout()
        OKButton = QtGui.QPushButton("OK")
        OKButton.setDefault(True)
        OKButton.clicked.connect(self.accept)
        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.clicked.connect(self.reject)
        b.addStretch(1)
        b.addWidget(cancelButton)
        b.addWidget(OKButton)
        
        h = QtGui.QVBoxLayout(self)
        h.addLayout(self.layout)
        h.addLayout(b)
        
class GraphConfigDialog(ConfigDialog):
    def __init__(self, graphConfig, parent=None):
        super(GraphConfigDialog, self).__init__(parent)
        self.setModal(False)
        self.graphConfig = graphConfig
        self.setWindowTitle("%s Config" % self.graphConfig.name)
        
        self.viewRange = QtGui.QDoubleSpinBox()
        self.viewRange.setRange(1, 3600)
        self.viewRange.setValue(self.graphConfig.configDict[self.graphConfig.ViewRange])
        
        self.plotDate = QtGui.QCheckBox()
        self.plotDate.setChecked(self.graphConfig.configDict[self.graphConfig.PlotDate])
        
        self.plotDataItemColor = []
        self.plotDataItemWidth = []
        self.plotDataItemPattern = []
        for label in self.graphConfig.leftLabels:
            self.plotDataItemColor.append(buttons.GetColorButton(self.graphConfig.configDict[self.graphConfig.PlotDataItemColor % label]))
            self.plotDataItemWidth.append(QtGui.QDoubleSpinBox())
            self.plotDataItemWidth[-1].setValue(self.graphConfig.configDict[self.graphConfig.PlotDataItemWidth % label])
            self.plotDataItemPattern.append(buttons.GetQPenStyleComboBox(self.graphConfig.configDict[self.graphConfig.PlotDataItemPattern % label]))
        if self.graphConfig.rightLabels:
            for label in self.graphConfig.rightLabels:
                self.plotDataItemColor.append(buttons.GetColorButton(self.graphConfig.configDict[self.graphConfig.PlotDataItemColor % label]))
                self.plotDataItemWidth.append(QtGui.QDoubleSpinBox())
                self.plotDataItemWidth[-1].setValue(self.graphConfig.configDict[self.graphConfig.PlotDataItemWidth % label])
                self.plotDataItemPattern.append(buttons.GetQPenStyleComboBox(self.graphConfig.configDict[self.graphConfig.PlotDataItemPattern % label]))
        
        self.layout.addRow("View Range", self.viewRange)
        self.layout.addRow("Plot Date", self.plotDate)
        self.layout.addRow(functions.HLine())
        for label in self.graphConfig.leftLabels:
            i = self.graphConfig.leftLabels.index(label)
            hbox = QtGui.QFormLayout()
            hbox.addRow("Color", self.plotDataItemColor[i])
            hbox.addRow("Pattern", self.plotDataItemPattern[i])
            hbox.addRow("Width", self.plotDataItemWidth[i])
            self.layout.addRow(label, hbox)
        if self.graphConfig.rightLabels:
            for label in self.graphConfig.rightLabels:
                i = len(self.graphConfig.leftLabels) + self.graphConfig.rightLabels.index(label)
                hbox = QtGui.QFormLayout()
                hbox.addRow("Color", self.plotDataItemColor[i])
                hbox.addRow("Pattern", self.plotDataItemPattern[i])
                hbox.addRow("Width", self.plotDataItemWidth[i])
                self.layout.addRow(label, hbox)
        self.layout.addRow(functions.HLine())
        
        self.applyToAll = QtGui.QCheckBox()
        self.layout.addRow("Apply to All %ss\n(where applicable)" % self.graphConfig.configDict[self.graphConfig.Category], self.applyToAll)
        
        self.run()
        
    def run(self):
        if self.exec_():
            applyToAll = self.applyToAll.isChecked()
#             print self.graphConfig.configDict
            self.graphConfig.save_configs(self.graphConfig.ViewRange, self.viewRange.value(), applyToAll)
            self.graphConfig.save_configs(self.graphConfig.PlotDate, int(self.plotDate.isChecked()), applyToAll)
            for label in self.graphConfig.leftLabels:
                i = self.graphConfig.leftLabels.index(label)
                self.graphConfig.save_configs(self.graphConfig.PlotDataItemColor % label, self.plotDataItemColor[i].color.name(), applyToAll)
                self.graphConfig.save_configs(self.graphConfig.PlotDataItemWidth % label, self.plotDataItemWidth[i].value(), applyToAll)
                self.graphConfig.save_configs(self.graphConfig.PlotDataItemPattern % label, self.plotDataItemPattern[i].currentIndex(), applyToAll)
            if self.graphConfig.rightLabels:
                for label in self.graphConfig.rightLabels:
                    i = len(self.graphConfig.leftLabels) + self.graphConfig.rightLabels.index(label)
                    self.graphConfig.save_configs(self.graphConfig.PlotDataItemColor % label, self.plotDataItemColor[i].color.name(), applyToAll)
                    self.graphConfig.save_configs(self.graphConfig.PlotDataItemWidth % label, self.plotDataItemWidth[i].value(), applyToAll)
                    self.graphConfig.save_configs(self.graphConfig.PlotDataItemPattern % label, self.plotDataItemColor[i].currentIndex(), applyToAll)
#             print self.graphConfig.configDict
        
class LabelConfigDialog(ConfigDialog):
    
    def __init__(self, labelConfig, parent=None):
        super(LabelConfigDialog, self).__init__(parent)
        self.setModal(False)
        self.labelConfig = labelConfig
        self.labelConfigDict = labelConfig.configDict
        self.setWindowTitle("%s Config" % self.labelConfig.name)
        
        self.scaleUnits = QtGui.QCheckBox()
        if self.labelConfigDict[self.labelConfig.ScaleUnits]:
            self.scaleUnits.setChecked(True)
        self.samplesKept = QtGui.QSpinBox()
        self.samplesKept.setRange(1, 9999)
        self.samplesKept.setValue(self.labelConfigDict[self.labelConfig.Samples])
        
        self.nominalColorLabel = buttons.GetColorButton(self.labelConfigDict[self.labelConfig.NominalColor])
        self.positiveCriticalColorLabel = buttons.GetColorButton(self.labelConfigDict[self.labelConfig.PositiveCriticalColor])
        self.negativeCriticalColorLabel = buttons.GetColorButton(self.labelConfigDict[self.labelConfig.NegativeCriticalColor])
        
        self.nominalValue = QtGui.QDoubleSpinBox()
        self.nominalValue.setValue(self.labelConfigDict[self.labelConfig.NominalValue])
        
        self.positiveSensitivity = QtGui.QDoubleSpinBox()
        self.positiveSensitivity.setValue(self.labelConfigDict[self.labelConfig.PositiveSensitivity])
        self.negativeSensitivity = QtGui.QDoubleSpinBox()
        self.negativeSensitivity.setValue(self.labelConfigDict[self.labelConfig.NegativeSensitivity])
        
        self.posDirection = QtGui.QCheckBox()
        self.negDirection = QtGui.QCheckBox()
        if self.labelConfigDict[self.labelConfig.Direction] == LabelDirection.HIGH:
            self.posDirection.setChecked(True)
        elif self.labelConfigDict[self.labelConfig.Direction] == LabelDirection.LOW:
            self.negDirection.setChecked(True)
        elif self.labelConfigDict[self.labelConfig.Direction] == LabelDirection.BOTH:
            self.negDirection.setChecked(True)
            self.posDirection.setChecked(True)

        self.layout.addRow("Scale Units", self.scaleUnits)
        self.layout.addRow("Samples", self.samplesKept)
        self.layout.addRow(functions.HLine())
        self.layout.addRow("Nominal Color", self.nominalColorLabel)
        self.layout.addRow("Positive Critical Color", self.positiveCriticalColorLabel)
        self.layout.addRow("Negative Critical Color", self.negativeCriticalColorLabel)
        self.layout.addRow("Nominal Value", self.nominalValue)
        self.layout.addRow("Positive Sensitivity", self.positiveSensitivity)
        self.layout.addRow("Negative Sensitivity", self.negativeSensitivity)
        self.layout.addRow("Color Above Nominal", self.posDirection)
        self.layout.addRow("Color Below Nominal", self.negDirection)
        
        if self.labelConfig.category:
            self.applyToAll = QtGui.QCheckBox()
            self.layout.addRow(functions.HLine())
            self.layout.addRow("Apply to All %ss\n(where applicable)" % self.labelConfig.category, self.applyToAll)
            
        self.run()
        
    def run(self):
        if self.exec_():
            if self.labelConfig.category:
                applyToAll = self.applyToAll.isChecked()
            else:
                applyToAll = False
            self.labelConfig.save_configs(self.labelConfig.ScaleUnits, int(self.scaleUnits.isChecked()), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.Samples, self.samplesKept.value(), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.NominalColor, self.nominalColorLabel.color.name(), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.PositiveCriticalColor, self.positiveCriticalColorLabel.color.name(), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.NominalValue, self.nominalValue.value(), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.NegativeCriticalColor, self.negativeCriticalColorLabel.color.name(), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.PositiveSensitivity, self.positiveSensitivity.value(), applyToAll=applyToAll)
            self.labelConfig.save_configs(self.labelConfig.NegativeSensitivity, self.negativeSensitivity.value(), applyToAll=applyToAll)
            if self.posDirection.isChecked() and self.negDirection.isChecked():
                direction = LabelDirection.BOTH
            elif self.posDirection.isChecked():
                direction = LabelDirection.HIGH
            elif self.negDirection.isChecked():
                direction = LabelDirection.LOW
            else:
                direction = LabelDirection.NONE
            self.labelConfig.save_configs(self.labelConfig.Direction, direction, applyToAll=applyToAll)
    