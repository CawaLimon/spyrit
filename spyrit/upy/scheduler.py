import pyb

class Scheduler(object):
    
    def __init__(selfs, frequency, timer):
        
        self.Tick = 0
        self.Timer = pyb.Timer(timer)
        self.Timer.init(freq=frequency)
        self.Timer.callback(self.Increment)
        self.Frequency = frequency
        self.TaskList = [[self.Dummy, 0, 0]]
        self.NumberofTasks = 0
        self.ExitState = 0
        
    def Dummy(self):
        Dummy = Dummy + 1
        
        return
    
    def Increment(self, timer):
        self.Tick = self.Tick + 1
        
        return
    
    def FrequencySet(self, frequency):
        
        self.Timer.init(freq=frequency)
        self.Frequency = frequency
        
        return
    
    def FrequencyGet(self):
        
        return self.Frequency
    
    def TickGet(self):
        
        return self.Tick
    
    def AddTask(self, Task):
        
        self.TaskList.append(Task)
        
        if (self.NumberofTasks == 0):
            del(self.TaskList[0])
            self.NumberofTasks = 1
        else:
            self.NumberofTasks += 1
            
        return
    
    def Run(self):
        for Task in range(len(self.TaskList)):
            if self.TaskList[Task][2] <= self.Tick:
                self.TaskList[Task][2] += self.TaskList[Task][1]
                Result = self.TaskList[Task][0]()
                
                if Result == True:
                    self.ExitState = True
                    
    def StateGet(self):
        return self.ExitState
    
    def Exit(self):
        self.ExitState = True