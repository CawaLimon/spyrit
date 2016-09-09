# from PyQt4 import QtCore
# from PyQt4 import QtGui
# import os
# import buttons
import ConfigParser
from pyqtgraph import intColor
from PyQt4.QtCore import Qt

# ENUMS
class LabelDirection:
    NONE, LOW, HIGH, BOTH = range(4)
    
# FUNCTIONS
def _iterateColor(index):
    return str(intColor(index).name())

def createGraphConfigDict(leftLabels, rightLabels=None):
    configDict = {"View Range" : "60",
                             "Plot Date" : "0",
                             "Background Color" : "black",
                             "Foreground Color" : "white"}
    for label in leftLabels:
        i = leftLabels.index(label)
        configDict["%s Color" % label] = _iterateColor(i)
        configDict["%s Width" % label] = "3"
        configDict["%s Pattern" % label] = str(Qt.SolidLine)
    if rightLabels:
        for label in rightLabels:
            i = len(leftLabels) + rightLabels.index(label)
            configDict["%s Color" % label] = _iterateColor(i)
            configDict["%s Width" % label] = "3"
            configDict["%s Pattern" % label] = str(Qt.SolidLine)
    return configDict
            
def createLabelConfigDict():
    return {"Scale Units": "0",
                             "Samples" : "300",
                             "Positive Critical Color" : "red",
                             "Negative Critical Color" : "red",
                           "Nominal Color" : "green",
                           "Nominal Value" : "0.0",
                           "Positive Sensitivity" : "50.0",
                           "Negative Sensitivity" : "50.0",
                           "Direction" : str(LabelDirection.BOTH)}

# GLOBASL
DEFAULT_FILE_LOC = "config.ini"

# Init configparser
config = ConfigParser.ConfigParser()
config.read(DEFAULT_FILE_LOC)

class ConfigObject(object):
    Category = "Category"
    def __init__(self, name, configDict, category=None):
        self.name = name
        self.configDict = configDict
        self.category = category
        if config.has_section(self.name):
            self.load_configs()
        else:
            self._make_configs()
        
    def load_configs(self):
        for con in self.configDict.keys():
            self.configDict[con] = config.get(self.name, con)
        if self.category:
            self.configDict[self.Category] = config.get(self.name, self.Category)
        self._cast_configs()
            
    def _make_configs(self):
        config.add_section(self.name)
        for con in self.configDict.keys():
            config.set(self.name, con, str(self.configDict[con]))
        if self.category:
            config.set(self.name, self.Category, self.category)
            
        self._write_configs()
        self.load_configs()
            
    def _write_configs(self):
        with open(DEFAULT_FILE_LOC, 'wb') as configfile:
            config.write(configfile)
            
    def _cast_configs(self):
        """Meant to be overriden
        """
        pass
            
    def save_configs(self, option, value, applyToAll=False):
        if applyToAll:
            for section in config.sections():
                if config.has_option(section, self.Category):
                    if config.get(section, self.Category) == self.configDict[self.Category]:
                        config.set(section, option, str(value))
        self.configDict[option] = value
        config.set(self.name, option, str(value))
        self._write_configs()
        
class ValueLabelConfig(ConfigObject):
    ScaleUnits = "Scale Units"
    Samples = "Samples"
    PositiveCriticalColor = "Positive Critical Color"
    NegativeCriticalColor = "Negative Critical Color"
    NominalColor = "Nominal Color"
    NominalValue = "Nominal Value"
    PositiveSensitivity = "Positive Sensitivity"
    NegativeSensitivity = "Negative Sensitivity"
    Direction = "Direction"
    def __init__(self, name, category):
        super(ValueLabelConfig, self).__init__(name, 
                                               createLabelConfigDict(), 
                                               category=category)
        
    def _cast_configs(self):
        self.configDict[self.ScaleUnits] = int(self.configDict[self.ScaleUnits])
        self.configDict[self.Samples] = int(self.configDict[self.Samples])
        self.configDict[self.NominalValue] = float(self.configDict[self.NominalValue])
        self.configDict[self.PositiveSensitivity] = float(self.configDict[self.PositiveSensitivity])
        self.configDict[self.NegativeSensitivity] = float(self.configDict[self.NegativeSensitivity])
        self.configDict[self.Direction] = int(self.configDict[self.Direction])
        
class GraphConfig(ConfigObject):
    ViewRange = "View Range"
    PlotDate = "Plot Date"
    PlotDataItemColor = "%s Color"
    PlotDataItemWidth = "%s Width"
    PlotDataItemPattern = "%s Pattern"
    BackgroundColor = "Background Color"
    ForegroundColor = "Foreground Color"
    def __init__(self, name, leftLabels, rightLabels=None):
        self.leftLabels = leftLabels
        self.rightLabels = rightLabels
        super(GraphConfig, self).__init__(name + " Graph", 
                                          createGraphConfigDict(leftLabels, rightLabels),
                                          category='Graph')
     
    def _cast_configs(self):
        self.configDict[self.ViewRange] = float(self.configDict[self.ViewRange])
        self.configDict[self.PlotDate] = int(self.configDict[self.PlotDate])
        for label in self.leftLabels:
            self.configDict[self.PlotDataItemWidth % label] = float(self.configDict[self.PlotDataItemWidth % label])
            self.configDict[self.PlotDataItemPattern % label] = int(self.configDict[self.PlotDataItemPattern % label])
        if self.rightLabels:
            for label in self.rightLabels:
                self.configDict[self.PlotDataItemWidth % label] = float(self.configDict[self.PlotDataItemWidth % label])
                self.configDict[self.PlotDataItemPattern % label] = int(self.configDict[self.PlotDataItemPattern % label])
