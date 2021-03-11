from mylib import ffi, lib

class callbackchar():
    def __init__(self,str1,str2):
        self.data = lib.get_somedata(str1,str2)
    def show_somedata(self):
        lib.show_somedata(self.data)
        

@ffi.def_extern()
def my_callback(str1, str2):
    print("Inside python callback function")
    print("arg1", ffi.string(str1))
    print("arg2", ffi.string(str2))
    return 0
    
if __name__ == '__main__':

    print("Pass a struct into C")
    a = "Ashwini".encode('ascii')
    b = "Patil".encode('ascii')
    c = callbackchar(a,b) 
    print("callbackchar in python is", c)
    c.show_somedata()

    arg1 = "Higfg"
    arg2 = "Asgrfdg"
    #pass_arg1 = int(ffi.cast('wchar_t', arg1))
    pass_arg1 = arg1.encode('ascii')
    pass_arg2 = arg2.encode('ascii')
    #pass_arg2 = int(ffi.cast('wchar_t', arg2))
    lib.library_function(lib.my_callback, pass_arg1, pass_arg2)
    