# Write a program to calculate the factorial of a given number using for loop.


n = int(input("Enter your number: "))
# 5! = 1*2*3*4*5 = 120
product = 1
for i in range(1, n + 1):

    product = product * i

print(f"factorial of {n} is {product}")
