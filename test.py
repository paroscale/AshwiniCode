from myabc import ffi,lib

class Myfile():
    def process(self):
        h = ffi.new_handle(self)
        print("h values is ",h)
        print("in process function")
        lib.example(lib.my_callback,45,56,h)

    def callback (self,agr1 , agr2):
        print("in callback function values are ")
        h = ffi.new_handle(self)
        lib.example(lib.my_callback,23,69,h)

@ffi.def_extern()
def my_callback(agr1 , h):
    #h = ffi.new_handle(x)
    print("in python callback function")
    agr1  = ffi.cast("int", 42)
    print( "ffi.cast value = ",agr1)
    print(" h value in my_callback is :",h)
    return 0
    #return ffi.from_handle(h).callback(agr1)
   
if __name__=="__main__":
    a = Myfile()
    x = 45 
    y = 36
    a.process()
    a.callback(20,30)

    


