import myStructure
def display(a):
    print("In Python Function!!!!")
    myStructure.lib.display(a)

if __name__ == "__main__":
    a = (1,25000,"Ashwini".encode('ascii'))
    display(a)    