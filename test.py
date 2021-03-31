from myabc import ffi,lib
import sys

@ffi.def_extern()
def ApplyCb(raft_uuid, peer_uuid):
    print("in python Apply callback function")
    print("raft_uuid value is = ", ffi.string(raft_uuid))
    print("peer_uuid value is  = ",ffi.string(peer_uuid))
    return 0

@ffi.def_extern()
def ReadCb(raft_uuid, peer_uuid):
    print("in python  Read callback function")
    return 0
   
if __name__=="__main__":
	# Store the command line parameter as raft_uuid.
    print("Arguments List:" , str(sys.argv))
    value1 = sys.argv[1]
    value2 = sys.argv[2]
    raft_uuid  = value1.encode('utf-8')
    peer_uuid  = value2.encode('utf-8')
    print(raft_uuid)
    print(peer_uuid)

    lib.c_wrapper_fun(raft_uuid,peer_uuid,lib.ApplyCb,lib.ReadCb)	