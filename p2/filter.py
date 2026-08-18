salary = [18000, 25000, 15000, 35000,50000]
def bonus(x):
    if(x >= 20000):
        return x
eligible =  filter(bonus,salary)
def add_bonus(a):
    return a + 5000
total = map(add_bonus,eligible )
print(list(total))
