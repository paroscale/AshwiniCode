#include <stdio.h>
#include "raft.h"

void call_python_func(API *my_api)
{   printf("adbkjdzbvb\n");
    printf("my raft uuid in c is: %s \n" ,my_api->raft_uuid);
    printf("my peer uuid in c is: %s \n" , my_api->peer_uuid);
};

void callback_function(int (*fun_ptr)(char *), char *x, char *y){
	printf("In C function x: %s\n", x); 
	printf("In C function y: %s\n", y);
	int z = fun_ptr(x);
	printf("The result is: %d\n", z);
}