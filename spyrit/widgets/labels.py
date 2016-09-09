from PyQt4 import QtGui, QtCore
import time
import configs
import dialogs
import numpy as np

DEFAULT_MAX_SAMPLES = 15000
DEFAULT_AVERAGE_SAMPLES = 500

ON_IMG_PATH = "./assets/on.png"
OFF_IMG_PATH = "./assets/off.png"

class Switch(QtGui.QLabel):
    def __init__(self, turnOn=False, parent=None):
        super(Switch, self).__init__(parent)
        self.OnPixmap = QtGui.QPixmap(ON_IMG_PATH).scaled(30, 30)
        self.OffPixmap = QtGui.QPixmap(OFF_IMG_PATH).scaled(30, 30)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.set_on(turnOn)
    
    def set_on(self, isOn):
        if isOn:
            self.setPixmap(self.OnPixmap)
        else:
            self.setPixmap(self.OffPixmap)
        self.isOn = isOn
        
    def is_on(self):
        return self.isOn

class ClickLineEdit(QtGui.QLineEdit):
    doubleClicked = QtCore.pyqtSignal()
    def __init__(self, text=None):
        super(ClickLineEdit, self).__init__()
        if text:
            self.setText(text)
        
    def mouseDoubleClickEvent(self, ev):
        self.doubleClicked.emit()
        
class HexInput(QtGui.QWidget):
    def __init__(self, text=None):
        super(HexInput, self).__init__()
        self.lineEdit = QtGui.QLineEdit()
        if text:
            self.lineEdit.setText(text)
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(QtGui.QLabel("0x"))
        self.layout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.fixCase)
        self.lineEdit.textEdited.connect(self.fixLen)
        self.lineEdit.setMaxLength(2)
        
    def setValue(self, val):
        newval = hex(val)[2:]
        if len(newval) < 2:
            newval = "0" + newval
        self.lineEdit.setText(newval)
        
    def fixLen(self, text):
        if len(text) < 2:
            text = "0" + text
        self.lineEdit.setText(text)
        
    def fixCase(self, text):
        self.lineEdit.setText(text.toUpper())
        
    def value(self):
        return int(str(self.lineEdit.text()), 16)
    
    def setReadOnly(self, val):
        self.lineEdit.setReadOnly(val)
        
class HexSpinBox(QtGui.QSpinBox):
    
    def __init__(self):
        super(HexSpinBox, self).__init__()
        self.setPrefix('0x')
        self.setRange(0, 3999)
        self.setValue(0)
        self.lineEdit().textChanged.connect(self.fixCase)
         
    def fixCase(self, text):
        self.lineEdit().setText(text.toUpper())

    def valueChanged(self, value):
        self.setValue(value)
        
    def valueFromText(self, text):
#         print int(text,16)
        return int(text, 16)
        
    def textFromValue(self, value):
#         print hex(value)
        return hex(value)[2:]

class Value(object):
    
    ##
    # Constructor. If an index is given, it finds configuration vaues within config.txt
    #
    def __init__(self, name, units, useConfig=False, category=None, averageSamples=DEFAULT_AVERAGE_SAMPLES):
#         super(Value, self).__init__(parent)
        self.name = name
        self.units = units
        self.useConfig = useConfig
        self._samples = DEFAULT_MAX_SAMPLES
        
#         self.maxLength = maxLength
        
        self.nameLabel = QtGui.QLabel(self.name)
        self.valueLabel = QtGui.QLabel('NaN')
        self.unitLabel = QtGui.QLabel(self.units)
        
        self.lineLabel = ClickLineEdit('NaN %s' % self.units)
        self.lineLabel.doubleClicked.connect(self.get_config)
        self.lineLabel.setReadOnly(True)

        self.showAverageButton = QtGui.QCheckBox(self.name)
        self.showAverageButton.setToolTip('Show Average Values')
        
        self.averageLabel = ClickLineEdit()
        self.averageLabel.setText(self.units)
        self.averageLabel.setReadOnly(True)
        self.averageLabel.doubleClicked.connect(self.get_config)
        
        if self.useConfig:
            self.config = configs.ValueLabelConfig(self.name, category)
            if self._samples != self.config.configDict[self.config.Samples]:
                self._samples = self.config.configDict[self.config.Samples]
                
        self.values = np.zeros(self._samples)
        self.times = np.zeros(self._samples)
        self.times[:] = time.time()
        self.average = np.zeros(self._samples)
    ##
    # Appends the argument to the list with the values along with a timestamp.
    # Colors the label according to the values provided in the config.
    def update_value(self, val):
        if self.useConfig:
            self.config.load_configs()
        if isinstance(val, float):
            val_float = val
        elif val is None:
            return
        else:
            val_float = float(val)
            
        self._append_value(val_float)
        
        #TODO: calculate average
#         samples = [value[0] for value in self.values[-self.samples:]]
#         average = float(sum(samples)/float(self.samples))
#         self.averageLabel.setText('%0.2f %s' %(average, self.units))
        self._update_labels(val_float)
        
        if self.useConfig:
            if self.config.configDict[self.config.Samples] != self._samples:
                self._resize_arrays()
            self.color_labels(val_float)
                
    def color_labels(self, val_float):
        val = val_float
        
        nom_val = self.config.configDict[self.config.NominalValue]
        nom_color = QtGui.QColor(self.config.configDict[self.config.NominalColor])
        crit_color_pos = QtGui.QColor(self.config.configDict[self.config.PositiveCriticalColor])
        crit_color_neg = QtGui.QColor(self.config.configDict[self.config.NegativeCriticalColor])
        pos_sens = self.config.configDict[self.config.PositiveSensitivity]
        neg_sens = self.config.configDict[self.config.NegativeSensitivity]
        direction = self.config.configDict[self.config.Direction]
        diff = abs(val - nom_val)
        
        if val > nom_val and not direction == configs.LabelDirection.LOW:
            crit_ratio = diff / pos_sens
            crit_rgb = np.array([crit_color_pos.red(), crit_color_pos.green(), crit_color_pos.blue()])

        elif val < nom_val and not direction == configs.LabelDirection.HIGH:
            crit_ratio = diff / neg_sens
            crit_rgb = np.array([crit_color_neg.red(), crit_color_neg.green(), crit_color_neg.blue()])
            
        else:
            self._set_lineedit_color(nom_color)
            return
        
        if crit_ratio > 1:
                crit_ratio = 1.
        crit_rgb = crit_rgb.astype('float64')
        crit_rgb *= crit_ratio
            
        nom_ratio = 1.0 - crit_ratio
        if nom_ratio < 0:
            nom_ratio = 0.
        nom_rgb = np.array([nom_color.red(), nom_color.green(), nom_color.blue()])
        nom_rgb = nom_rgb.astype('float64')
        nom_rgb *= nom_ratio

        new_rgb = crit_rgb + nom_rgb
        for value in new_rgb:
            if value > 255:
                value = 255
            else:
                value = int(value)
        
        new_color = QtGui.QColor(new_rgb[0], new_rgb[1], new_rgb[2])
        self._set_lineedit_color(new_color)
        
    def _resize_arrays(self):
        newsize = self.config.configDict[self.config.Samples]
        oldsize = self._samples
        diff = abs(newsize - oldsize)
        if newsize > oldsize:
            for _ in range(diff):
                self.values = np.insert(self.values, 0, self.values[0])
                self.times = np.insert(self.times, 0, self.times[0])
        else:
            for _ in range(diff):
                self.values = np.delete(self.values, 0, 0)
                self.times = np.delete(self.times, 0, 0)
        self._samples = newsize
        
    def _append_value(self, value):
        now = time.time()
        self.times[:-1] = self.times[1:]
        self.times[-1] = now
        
        self.values[:-1] = self.values[1:]
        self.values[-1] = value
        
    def _update_labels(self, val_float):
        prefix = ""
        if self.useConfig:
            if self.config.configDict[self.config.ScaleUnits]:
                if abs(val_float) < 1:
                    val_float *= 1000
                    prefix = "m"
                elif abs(val_float) < 0.001:
                    val_float *= 1000000
                    prefix = "n"
                elif abs(val_float) > 1000:
                    val_float /= 1000
                    prefix = "k"
        self.valueLabel.setText('%0.2f' % val_float)
        self.lineLabel.setText('%0.2f %s%s' % (val_float, prefix, self.units))
        
    def _set_lineedit_color(self, color):
        self.lineLabel.setStyleSheet("* {color: %s; }" % color.name())
        
    ##
    # Shows the config dialog
    #
    def get_config(self):
        if self.useConfig:
            dialogs.LabelConfigDialog(self.config)
            
class ScalablePixmapLabel(QtGui.QLabel): #Used for thumbnail display: resizes according to app size
    def __init__(self, imgLoc=None):
        super(ScalablePixmapLabel, self).__init__()
        self.setFrameStyle(QtGui.QFrame.StyledPanel)
        if imgLoc:
            self.pixmap = QtGui.QPixmap(imgLoc)
        else:
            self.pixmap = QtGui.QPixmap()

    def paintEvent(self, event):
        if not self.pixmap.isNull():
            size = self.size()
            painter = QtGui.QPainter(self)
            point = QtCore.QPoint(0,0)
            scaledPix = self.pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
            # start painting the label from left upper corner
            point.setX((size.width() - scaledPix.width())/2)
            point.setY((size.height() - scaledPix.height())/2)
    #         print point.x(), ' ', point.y()
            painter.drawPixmap(point, scaledPix)
        
    def changePixmap(self, img):
        self.pixmap = img
        self.repaint() # repaint() will trigger the paintEvent(self, event), this way the new pixmap will be drawn on the label