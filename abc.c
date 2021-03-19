#include<stdio.h>
#include "abc.h"

void example(int (*fun_ptr)(int, int), int x, int y,void* data){
    printf("in c function");
    fun_ptr(x,y);
    //printf("void values is %d" , data);
}

