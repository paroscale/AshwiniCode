#include "CFunction.h"
#include <stdio.h>

void call_python_func(API a1 )
{
   printf("my raft uuid in c is: %s \n" ,a1.raft_uuid );
   printf("my peer uuid in c is: %s \n" , a1.peer_uuid);
};