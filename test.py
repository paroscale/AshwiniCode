import myfile

def display():
    print("In Python Function!!!!\n")
    values  = myfile.ffi.new("Person*", a)
    myfile.lib.call_python_func(values)

if __name__ == "__main__":
    a = ("aaaa".encode('ascii'),"bbbb".encode('ascii'))
    display()