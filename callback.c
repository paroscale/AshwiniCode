#include <stdio.h>
#include "callback.h"
void show_somedata(callbackchar somedata) {
    printf("call back char in C is %s\n", somedata.name);
}

callbackchar get_somedata(char name[20]) {
    callbackchar somedata = { {name[20]} };
    printf("Returning callbackchar %s\n", somedata.name);
    return somedata;
}