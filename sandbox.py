def func(f):
    def wrapper():
        print("Started")
        a = "Hello"
        f(a)
        print("Ended")
    return wrapper

@func
def func2(a):
    print(a)

func2()