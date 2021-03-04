from mylib import ffi,lib

class PmdbAPI():
    def __init__(self, a=None, b=None):
        self.data = lib.get_somedata(a, b)
    def show_somedata(self):
        lib.show_somedata(self.data)
    def struct_by_ref(self):
        pmdb_test = ffi.new("PmdbAPI*", self.data)
        lib.struct_by_ref(pmdb_test)
        self.data = pmdb_test


@ffi.def_extern()
def my_callback(x, y):
    print("Inside python callback function")
    z = x + y
    print("Returning z", z)
    return z

if __name__ == '__main__':
    ################################
    print("Pass a struct into C")
    a = PmdbAPI(1, 2.5)
    print("PmdbAPI in python is", a)
    a.show_somedata()
    print()
    ###############################
    print("Pass by reference")
    a = PmdbAPI(5, 6.5)
    print("PmdbAPI in python is", a)
    a.struct_by_ref()
    print("PmdbAPI in python is", a)

    lib.library_function(lib.my_callback, 10, 20)