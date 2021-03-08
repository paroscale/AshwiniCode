from mylib import ffi,lib
import mylib

class callbackchar():
    def __init__(self,name):
        self.data = lib.get_somedata(name)
    def show_somedata(self):
        lib.show_somedata(self.data)
    

if __name__ == '__main__':

    print("Pass a struct into C")
    a = callbackchar("Ashwini".encode('ascii'))
    print("callbackchar in python is", a)

    a.show_somedata()