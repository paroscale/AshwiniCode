from mylib import ffi,lib
import mylib

class callbackchar():
    def __init__(self,name):
        self.data = lib.get_somedata(name)
    def show_somedata(self):
        lib.show_somedata(self.data)

@ffi.def_extern()
def my_callback(x):
    print("Inside python callback function")
    z= x + "my_call_back_function"
    print("Returning x value ", z)
    return z
    

if __name__ == '__main__':

    print("Pass a struct into C")
    a = callbackchar("Ashwini".encode('ascii'))
    print("callbackchar in python is", a)
    a.show_somedata()
    lib.library_function(lib.my_callback,"ashwini".encode('ascii'))