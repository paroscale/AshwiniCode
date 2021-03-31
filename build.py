#!/usr/bin/env python
import os
import cffi
if __name__ == "__main__":
    ffi = cffi.FFI()
    # Define the python callback function
    ffi.embedding_api(""" extern "Python" int ApplyCb(char* , char* ); 
                                          int ReadCb(char*, char* ); 
                                          """)

    # Get the functions declarations from C library
    with open(os.path.join(os.path.dirname(__file__), "abc.h")) as f:
        ffi.cdef(f.read())

    ffi.set_source("myabc",
        '#include "abc.h"',
        sources = ['abc.c'],
        libraries=["abc"],
        library_dirs=[os.path.dirname(__file__),],
    )
    ffi.compile()