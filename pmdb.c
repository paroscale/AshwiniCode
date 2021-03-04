#include <stdio.h>
#include "pmdb.h"
void show_somedata(PmdbAPI somedata) {
    printf("PmdbAPI in C is (%d, %f)\n", somedata.a, somedata.b);
}
/* Increment a PmdbAPI which was passed by reference */
void struct_by_ref(PmdbAPI *somedata) {
    show_somedata(*somedata);
    somedata->a++;
    show_somedata(*somedata);
}

PmdbAPI get_somedata(int a, float b) {
    PmdbAPI somedata = { a, b };
    printf("Returning PmdbAPI (%d, %f)\n", somedata.a, somedata.b);
    return somedata;
}

void library_function(int (*fun_ptr)(int, int), int x, int y)
{
	fun_ptr(x, y);
}
