from mylib import ffi, lib

class callbackchar():
    def __init__(self,name):
        self.data = lib.get_somedata(name)
    def show_somedata(self):
        lib.show_somedata(self.data)

@ffi.def_extern()
def my_callback(x):
    print("Inside python callback function")
    z = "A"
    print("Returning z value ", z)
    return z
    

if __name__ == '__main__':

    print("Pass a struct into C")
    b= "Ashwini".encode('ascii')
    a = callbackchar(b)
    print("callbackchar in python is", a)
    a.show_somedata()
    #s = ("Ashwini".encode('ascii'))
    s = [ffi.new("char[]","ashwini".encode('ascii'))]
    t = ffi.new("char *[]",s)
    lib.library_function(lib.my_callback,t)
