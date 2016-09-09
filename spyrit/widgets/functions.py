'''
Created on Jul 21, 2016

@author: markus
'''
from PyQt4 import QtGui
import sys
import glob
import serial
# from PyQt4 import QtCore

def HLine(): #Line Object
    toto = QtGui.QFrame()
    toto.setFrameShape(QtGui.QFrame.HLine)
    toto.setFrameShadow(QtGui.QFrame.Sunken)
    return toto
    
def VLine(): #Line Object
    toto = QtGui.QFrame()
    toto.setFrameShape(QtGui.QFrame.VLine)
    toto.setFrameShadow(QtGui.QFrame.Sunken)
    return toto
    
def addSpacer():
    spacer = QtGui.QWidget()
    spacer.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    return spacer

def listSerialPorts():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
