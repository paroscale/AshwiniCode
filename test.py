from myabc import ffi,lib

class Myfile():
    def process(self):
        h = ffi.new_handle(self)
        print("in init function")
        lib.example(lib.my_callback,x,y , h)

    def callback (self,agr1 , agr2):
        print("dbbdliknckcbz")

@ffi.def_extern()
def my_callback(agr1 , agr2 , data):
    print("in python callback function")
    return ffi.from_handle(data).callback(agr1,agr2)
   
if __name__=="__main__":
    a = Myfile()
    
    x = 45 
    y = 36
    a.process()
    a.callback(20,30)

    


