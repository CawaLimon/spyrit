IRQ = False

class SPI:
    MASTER = 1
    def __init__(self, num, caste):
        self.num = num
        self.caste = caste
        
    def send(self, data):
        print (data)
        
    def init(self):
        print ('started')
        
    def send_recv(self, data, recv=None):
        print (data)
        if recv:
            recv = bytearray([0x00 * len(data)])
            return recv
        
class Pin:
    OUT_PP = 1
    PULL_UP = 1
    IN = 1
    PULL_DOWN = 1
    def __init__(self, pin, task):
        self.pin = pin
        self.task = task
        
class ExtInt:
    IRQ_FALLING = 1
    def __init__(self, num, caste, nu):
        pass
    
def enable_irq(state=True):
    global IRQ
    IRQ = state
    print("Accepting Interrupt Requests")
    
def disable_irq():
    global IRQ
    old = IRQ
    IRQ = False
    return old
    print("Rejecting Interrupt Requests")
    
def wfi():
    print("waiting for interrupt")
    
def have_cdc():
    return True

def delay(time):
    pass
    
class USB_VCP:
    def __init__(self):
        pass
    
    def any(self):
        return True
    
    def readall(self):
        return bytearray(3)
    
    def readline(self):
        return bytearray(3)
    
    def read(self, n):
        return bytearray(n)
    
    def recv(self, data, timeout=5000):
        return data
    
    def send(self, data):
        return data
    
    def write(self, buf):
        return buf