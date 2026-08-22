
def greeting(func):

    def inner():
        print("before")

        func()

        print("before")

    return inner



@greeting
def hello():
    print("hello thereis  ghjhf hfgj helo")

hello()