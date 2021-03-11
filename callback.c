#include <stdio.h>
#include "callback.h"
void show_somedata(callbackchar somedata)
{
    printf("call back char in C is {%s,%s} \n", somedata.s1,somedata.s2);
}

callbackchar get_somedata(char s1[20] , char s2[20])
{
    callbackchar somedata = { {s1[20],s2[20]}};
    printf("Returning callbackchar {%s,%s} \n", somedata.s1 , somedata.s2);
    return somedata;
}

void library_function(int (*fun_ptr)(char* ,char*), char* x , char* y)
{
	int z = fun_ptr(x,y);
    printf("the value of z is: %d " , z);
}