#kwargs -> keyword argument
def myfun(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
myfun(first="geeks",second="codes")
