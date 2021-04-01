#include<stdio.h>
#include "abc.h"

void passing_struct_func_ptr(pmdb_callback_ptr *call_back, char *raft_uuid,
								char *peer_uuid)
{
	printf("Calling func ptr using struct pointers\n");
	int value1 = call_back->applycb_ptr(raft_uuid, peer_uuid);
	int value2 = call_back->readcb_ptr(raft_uuid, peer_uuid);
    printf("value1 is %d\n" , value1);
    printf("value2 is %d\n" , value2);
	}

void c_wrapper_fun(char* raft_uuid, char* peer_uuid, int (*applycb_ptr)(char *, char *),
					int (*readcb_ptr)(char *, char *))
{
	// Call python callback function and pass raft_uuid and peer_uuid as para to it.
	int value3 = applycb_ptr(raft_uuid, peer_uuid);
	int value4 = readcb_ptr(raft_uuid, peer_uuid);
    printf("value3 is %d\n" , value3);
    printf("value4 is %d\n" , value4);

	pmdb_callback_ptr my_cb;
	my_cb.applycb_ptr = applycb_ptr;
	my_cb.readcb_ptr = readcb_ptr;
    passing_struct_func_ptr(&my_cb, raft_uuid, peer_uuid);
	}


void call_python_func(pmdb_callback_ptr *call_back){   
    printf ("in c call_python fucntion \n");
    }