#!/usr/bin/env python
import os
import cffi
if __name__ == "__main__":
    ffi = cffi.FFI()
    # Define the python callback function
   # ffi.embedding_api(""" extern "Python" int my_callback(int, int); """)

    # Get the functions declarations from C library
    with open(os.path.join(os.path.dirname(__file__), "callback.h")) as f:
        ffi.cdef(f.read())

    ffi.set_source("mylib",
        '#include "callback.h"',
        sources = ['callback.c'],
        libraries=["callback"],
        library_dirs=[os.path.dirname(__file__),],
    )
    ffi.compile()