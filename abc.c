#include<stdio.h>
#include "abc.h"

void example(int (*fun_ptr)(int, int), int x, int y,void* data){
    printf("in c function");
    int rc = fun_ptr(x,y);
    printf("value of rc function is = %d\n", rc);
    //printf("void values is %d" , data);
}

