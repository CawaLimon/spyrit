from PyQt4 import QtGui

QPEN_STYLE_OPTIONS = ("None",
                      "Solid Line",
                      "Dashed Line",
                      "Dotted Line",
                      "Dash Dot Line",
                      "Dash Dot Dot Line")

class GetColorButton(QtGui.QPushButton):
    def __init__(self, color, parent=None):
        super(GetColorButton, self).__init__(parent)
        self.color = QtGui.QColor(color)
        self.setStyleSheet("* { background-color: %s; border: 1px solid black; }" % self.color.name())
        self.setFixedSize(30, 30)
        self.clicked.connect(self.get_color)
        
    def get_color(self):
        col = QtGui.QColorDialog.getColor(self.color)
        
        if col.isValid():
            self.setStyleSheet("* { border: 1px solid black; background-color: %s }" % col.name())
            self.color = col
            
class GetQPenStyleComboBox(QtGui.QComboBox):
    def __init__(self, penStyle=None, parent=None):
        super(GetQPenStyleComboBox, self).__init__(parent)
        
        self.addItems(QPEN_STYLE_OPTIONS)
        
        self.setCurrentIndex(penStyle)