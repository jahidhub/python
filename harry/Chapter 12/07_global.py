a = 10


def num():
    global a  # when i provied global key then i maintion a is global means upper a , then it just change the value
    a = 3
    print(a)


num()
print(a)  # this a  global a . means a =10
