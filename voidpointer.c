#include<stdio.h>
#include "voidpointer.h"

void f1(void* p){
    int *ip = (int*)p;
    *ip = 9;  
    printf("%d\n",*ip);
}
/*int main(){
    int p;
    printf("%d\n",p);
    f1((void*)&p);
    printf("%d\n",p);
    return 0;
}*/

void function(int a){
    //int a = 7;
    void *p;
    p=&a;
    printf("value of integer is = %d\n", *((int *)p));
}