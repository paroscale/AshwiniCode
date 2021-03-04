#this code is giving error Python.py is working
import myPythonCBinding

def read(*args):
    print("My raft_uuid = " , raft_uuid)
    print("My peer_uuid = " , peer_uuid)
    myPythonCBinding.lib.call_python_func(Py_api)
    

if __name__ == "__main__":
    raft_uuid = "abcd"
    peer_uuid = "efgh"
    # here Py_api is a strcutre of type Struct API*
    Py_api = (id(read))
    print(Py_api)
    read(raft_uuid,peer_uuid)
    
    

  
    