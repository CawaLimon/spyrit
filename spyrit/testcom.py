import pyboard
DEBUG = False
import inspect
import time

def remote(pyb, func, *args, **kwargs):
    """Calls func with the indicated args on the micropython board."""
    args_arr = [repr(i) for i in args]
    kwargs_arr = ["{}={}".format(k, repr(v)) for k, v in kwargs.items()]
    func_str = inspect.getsource(func)
    func_str += 'output = ' + func.__name__ + '('
    func_str += ', '.join(args_arr + kwargs_arr)
    func_str += ')\n'
    func_str += 'if output is None:\n'
    func_str += '    print("None")\n'
    func_str += 'else:\n'
    func_str += '    print(output)\n'
    if DEBUG:
        print('----- About to send %d bytes of code to the pyboard -----' % len(func_str))
        print(func_str)
        print('-----')
#     pyb.enter_raw_repl()
    output, _ = pyb.exec_raw(func_str)
#     pyb.exit_raw_repl()
    if DEBUG:
        print('-----Response-----')
        print(output)
        print('-----')
    return output

def getHey():
    return "Hey"
    
def getWhy():
    return "Why"
    
def getInt():
    return 23
    
def getList():
    return [1, 2, 3]
    
def getBytes():
    return bytearray([1, 2, 3])

pybo = pyboard.Pyboard('COM5')

pybo.enter_raw_repl()

pybo.exec_("import ayo")
print remote(pybo, getInt)
print remote(pybo, getList)
# print pybo.exec_raw("ayo.getInt()")
# print pybo.exec_raw("ayo.getList()")
# print pybo.exec_raw("ayo.getBytes()")

pybo.exit_raw_repl()
pybo.close()