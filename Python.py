import myPythonCBinding

def read():
    print("in python function") 
    myPythonCBinding.lib.call_python_func(a)

if __name__ == "__main__":
    a = ("abcd".encode('ascii'),"efgh".encode('ascii'))
    read()
    