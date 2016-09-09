import logging
from PyQt4 import QtCore
from PyQt4 import QtGui

class QSignalHandler(QtCore.QObject, logging.Handler):
    sendMessage = QtCore.pyqtSignal(str)
    def __init__(self):
        logging.Handler.__init__(self)
        QtCore.QObject.__init__(self)
        
    def emit(self, record):
        record = self.format(record)
        self.sendMessage.emit(record)