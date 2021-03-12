import myfile
from myfile import ffi,lib

class structure():
    def __init__(self, raft_uuid, peer_uuid):
        self.raft_uuid = raft_uuid
        self.peer_uuid = peer_uuid
    
    def read(self):
        print("in python function") 
        myfile.lib.call_python_func(self)
    
    def write(self):
        print("in write python function")
        myfile.lib.call_python_func(self)

if __name__ == "__main__":
    r = structure("abcd".encode('ascii'), "efgh".encode('ascii'))
    """raftStruct = ffi.new("struct API*")
    raftStruct.raft_uuid = "abcd".encode('ascii')
    raftStruct.peer_uuid = "efgh".encode('ascii')
    lib.call_python_func(raftStruct[0])
    print(raftStruct)"""

    r.read()