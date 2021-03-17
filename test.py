import myvoidpointer
from myvoidpointer import lib,ffi

def voidcall():
    print("in pyhton function")
    myvoidpointer.lib.function(a)

def callCFunction():
    print("in callCFunction")
    myvoidpointer.lib.f1(a)

if __name__=="__main__":
    a = 10
    b = ffi.new("void *",a)
    voidcall()
    callCFunction()