"""
Write a program to print multiplication table of n using for loops in reversed
order.


3*1=3
3*2=6


"""

n = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n *(11-i)} ")


