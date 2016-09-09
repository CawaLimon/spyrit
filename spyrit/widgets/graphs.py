import time
import configs
import dialogs
import pyqtgraph as pg
import numpy as np
from PyQt4 import QtGui

DEFAULT_VIEW_RANGE = 60#S
DEFAULT_TIME_FORMAT = "%m/%d/%Y %H:%M:%S"
LOAD_EVERY_RESET = 1

#TODO
#Add grid config to graph

class ModAxisItem(pg.AxisItem):
        def __init__(self, *args, **kwargs):
            super(ModAxisItem, self).__init__(*args, **kwargs)
            self.plotDate = 0
        def tickStrings(self, values, scale, spacing):
            if not self.plotDate:
                places = max(0, np.ceil(-np.log10(spacing*scale)))
                strings = []
                for v in values:
                    vs = v * scale
                    if abs(vs) < .001 or abs(vs) >= 10000:
                        vstr = "%g" % vs
                    else:
                        vstr = ("%%0.%df" % places) % vs
                    strings.append(vstr)
                return strings
            else:
                return [time.ctime(value) for value in values if value > 0]

class singleAxesGraph(pg.PlotWidget):
    def __init__(self, name, plotLabels):
        self.modAxis = ModAxisItem(orientation='bottom')
        super(singleAxesGraph, self).__init__(axisItems={'bottom' : self.modAxis})
        self.name = name
        self.plotLabels = plotLabels
        self.pause = False
        self.plotItem.setTitle(name)
        
        self.config = configs.GraphConfig(self.name, self.plotLabels)
        self.modAxis.plotDate = self.config.configDict[self.config.PlotDate]
        self.viewRange = self.config.configDict[self.config.ViewRange]
        
        if self.modAxis.plotDate:
            now = time.time()
            self.setXRange(now - self.viewRange, now, 0)
        else:
            self.setXRange(-self.viewRange, 0, 0)
        
        self.primaryPlots = [self.plot(name=item, pen=self.makePen(item)) for item in plotLabels]
        self.setLabel('bottom', 'Time', units='s')
        legend = self.addLegend()
        for plot in self.primaryPlots:
            legend.addItem(plot, plotLabels[self.primaryPlots.index(plot)])
            
        self.menu = self.getPlotItem().getViewBox().menu
        self.configure = QtGui.QAction("Configure..", self.menu)
        self.configure.triggered.connect(self.open_config)    
        self.menu.addAction(self.configure)
        
        self.pauseAction = QtGui.QAction("Pause", self.menu)
        self.pauseAction.triggered.connect(self.toggle_pause)
        self.pauseAction.setCheckable(True)
        self.menu.addAction(self.pauseAction)
            
    def makePen(self, label):
        color = QtGui.QColor(self.config.configDict[self.config.PlotDataItemColor % label])
        width = self.config.configDict[self.config.PlotDataItemWidth % label]
        style = self.config.configDict[self.config.PlotDataItemPattern % label]
        return pg.mkPen(color=color, width=width, style=style)
        
    def setAxisNames(self, name, units):
        self.setLabel('left', name, units=units)
        
    def update_data(self, dataList):
        if self.isVisible() and not self.pause:
            if LOAD_EVERY_RESET:
                self.config.load_configs()
                self.load_config()
            for i in range(len(self.primaryPlots)):
                now = time.time()
                if not self.modAxis.plotDate:
                    xdata = dataList[i][1] - now
                    self.setXRange(-self.viewRange, 0, 0)
                else:
                    xdata = dataList[i][1]
                    self.setXRange(now - self.viewRange, now, 0)
                ydata = dataList[i][0]
                self.primaryPlots[i].setData(x=xdata, y=ydata)
                
    def open_config(self):
        dialogs.GraphConfigDialog(self.config)
        self.load_config()
        
    def load_config(self):
        self.modAxis.plotDate = self.config.configDict[self.config.PlotDate]
        self.viewRange = self.config.configDict[self.config.ViewRange]
        pens = [self.makePen(label) for label in self.plotLabels]
        for plot in self.primaryPlots:
            i = self.primaryPlots.index(plot)
            plot.setPen(pens[i])
                
    def toggle_pause(self):
        if self.pause:
            self.pause = False
            self.pauseAction.setChecked(False)
        else:
            self.pause = True
            self.pauseAction.setChecked(True)
                    
class doubleAxesGraph(pg.PlotWidget):
    def __init__(self, name, plotLabelsLeft, plotLabelsRight):
        self.modAxis = ModAxisItem(orientation='bottom')
        super(doubleAxesGraph, self).__init__(axisItems={'bottom' : self.modAxis})
        self.name = name
        self.plotLabelsLeft = plotLabelsLeft
        self.plotLabelsRight = plotLabelsRight
        self.pause = False
        
        self.config = configs.GraphConfig(self.name, self.plotLabelsLeft, self.plotLabelsRight)
        self.modAxis.plotDate = self.config.configDict[self.config.PlotDate]
        self.viewRange = self.config.configDict[self.config.ViewRange]
        
        if self.modAxis.plotDate:
            now = time.time()
            self.setXRange(now - self.viewRange, now, 0)
        else:
            self.setXRange(-self.viewRange, 0, 0)

        self.leftAxis = self.plotItem
        self.leftAxis.setTitle(name)
        self.leftAxis.getAxis('bottom').setLabel('Time', units='s')
        legend = self.leftAxis.addLegend()
        
        self.rightAxis = pg.ViewBox()
        #legend1 = self.rightAxis.addLegend()
        self.leftAxis.showAxis('right')
        self.leftAxis.scene().addItem(self.rightAxis)
        self.leftAxis.getAxis('right').linkToView(self.rightAxis)
        self.rightAxis.setXLink(self.leftAxis)
        
        self.leftAxis.vb.sigResized.connect(self.updateViews)
        
        self.leftAxisPlots = [self.leftAxis.plot([], [], name=plot, pen=self.makePen(plot)) for plot in plotLabelsLeft]
        for plot in plotLabelsRight:
            self.rightAxis.addItem(pg.PlotCurveItem([], [], name=plot, pen=self.makePen(plot)))
        self.rightAxisPlots = [self.rightAxis.allChildren()[1]]
        for plot in self.rightAxisPlots:
            legend.addItem(plot, plotLabelsRight[self.rightAxisPlots.index(plot)]) 
        
        self.menu = self.getPlotItem().getViewBox().menu
        self.configure = QtGui.QAction("Configure..", self.menu)
        self.configure.triggered.connect(self.open_config)    
        self.menu.addAction(self.configure)
        
        self.pauseAction = QtGui.QAction("Pause", self.menu)
        self.pauseAction.triggered.connect(self.toggle_pause)
        self.pauseAction.setCheckable(True)
        self.menu.addAction(self.pauseAction)
        
    def makePen(self, label):
        color = QtGui.QColor(self.config.configDict[self.config.PlotDataItemColor % label])
        width = self.config.configDict[self.config.PlotDataItemWidth % label]
        style = self.config.configDict[self.config.PlotDataItemPattern % label]
        return pg.mkPen(color=color, width=width, style=style)
        
    def setAxisNames(self, nameLeft, unitsLeft, nameRight, unitsRight):
        self.leftAxis.getAxis('left').setLabel(nameLeft, units=unitsLeft)
        self.leftAxis.getAxis('right').setLabel(nameRight, units=unitsRight)
        
    def updateViews(self):
        self.rightAxis.setGeometry(self.leftAxis.vb.sceneBoundingRect())
        
    def open_config(self):
        dialogs.GraphConfigDialog(self.config)
        self.load_config()
        
    def load_config(self):
        self.modAxis.plotDate = self.config.configDict[self.config.PlotDate]
        self.viewRange = self.config.configDict[self.config.ViewRange]
        pens = [self.makePen(label) for label in self.plotLabelsLeft]
        for plot in self.plotLabelsRight:
            pens.append(self.makePen(plot))
        for plot in self.leftAxisPlots:
            i = self.leftAxisPlots.index(plot)
            plot.setPen(pens[i])
        for plot in self.rightAxisPlots:
            i = len(self.leftAxisPlots) + self.rightAxisPlots.index(plot)
            plot.setPen(pens[i])
                
    def toggle_pause(self):
        if self.pause:
            self.pause = False
            self.pauseAction.setChecked(False)
        else:
            self.pause = True
            self.pauseAction.setChecked(True)

    def update_data(self, dataListLeft, dataListRight): #data1 = [self.voltage.value]
        if self.isVisible() and not self.pause:
            if LOAD_EVERY_RESET:
                self.config.load_configs()
                self.load_config()
            for i in range(len(self.leftAxisPlots)):
                now = time.time()
                if not self.modAxis.plotDate:
                    xdata = dataListLeft[i][1] - now
                    self.setXRange(-self.viewRange, 0, 0)
                else:
                    xdata = dataListLeft[i][1]
                    self.setXRange(now - self.viewRange, now, 0)
                ydata = dataListLeft[i][0]
                
                self.leftAxisPlots[i].setData(x=xdata, y=ydata)

            for i in range(len(self.rightAxisPlots)):
                now = time.time()
                if not self.modAxis.plotDate:
                    xdata = dataListRight[i][1] - now
                else:
                    xdata = dataListRight[i][1]
                ydata = dataListRight[i][0]
                
                self.rightAxisPlots[i].setData(x=xdata, y=ydata)
