import myPythonCBinding

def read(a):
    myPythonCBinding.lib.call_python_func(a)
    print("My raft_uuid","My peer_uuid",a)
  
def write(a):
    #print("My raft_uuid","My peer_uuid",a)
    myPythonCBinding.call_python_func(a)

if __name__ =="__main__":
    a =["abcd".encode('ascii'),"efgh".encode('ascii')]
    read(a)
