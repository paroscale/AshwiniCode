#include<stdio.h>
#include "abc.h"

void example(int (*fun_ptr)(int, int), int x, int y,void* data){
    printf("in c function");
    int rc = fun_ptr(x,y);
    printf("value of rc function is = %d\n", rc);
    //printf("void values is %d" , data);
}


void passing_struct_func_ptr(struct pmdb_callback_ptr *call_back, char *raft_uuid,
								char *peer_uuid)
{
	printf("Calling func ptr using struct pointers\n");
	call_back->applycb_ptr(raft_uuid, peer_uuid);
	call_back->readcb_ptr(raft_uuid, peer_uuid);
}

void c_wrapper_fun(char *raft_uuid, char *peer_uuid, int (*applycb_ptr)(char *, char *),
					int (*readcb_ptr)(char *, char *))
{
	// Call python callback function and pass raft_uuid and peer_uuid as para to it.
	applycb_ptr(raft_uuid, peer_uuid);
	readcb_ptr(raft_uuid, peer_uuid);


	struct pmdb_callback_ptr my_cb;
	my_cb.applycb = applycb_ptr;
	my_cb.readcb = readcb_ptr;


	passing_struct_func_ptr(&my_cb, raft_uuid, peer_uuid);
}
