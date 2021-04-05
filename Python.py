import myPythonCBinding
myPythonCBinding.lib.call_python_func(a)
def read():
    print("in python function") 
     

if __name__ == "__main__":
    a = ("abcd".encode('ascii'),"efgh".encode('ascii'))
    read()
    