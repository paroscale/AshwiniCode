import myfile
from myfile import ffi,lib

def read():
    print("in python function") 
    values = myfile.ffi.new("API*",r)
    myfile.lib.call_python_func(values)
    
def write():
    print("in write python function")
    myfile.lib.call_python_func()

@ffi.def_extern()
def my_callback(str1):
    print("Inside python callback function")
    print("argument passed ", ffi.string(str1))
    return 0

if __name__ == "__main__":
    r = ("abcd".encode('ascii'), "efgh".encode('ascii'))
    read()
    str1 = "abcd"
    pass_str = str1.encode('ascii')
    lib.callback_function(lib.my_callback,pass_str,r)