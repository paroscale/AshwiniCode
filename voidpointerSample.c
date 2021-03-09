#include <stdio.h>
int main(){
    int a = 7;
    float b = 3.42;
    char ch [] = "Ashwini";
    void *p;
    p = &a;
    printf("value of integer is = %d\n", *((int *)p));
    p = &b;
    printf("value of float is = %f\n", *((float *)p));
    p = &ch;
    printf("value of char  is = %c\n", *(char *)p);
    return 0;
}