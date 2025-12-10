#Arbitrary Arguments
# *args -> Non keywords argument
def fun(*argsv):
    for arg in argsv:
        print(arg)
fun('hello','my','name','is','uma')
