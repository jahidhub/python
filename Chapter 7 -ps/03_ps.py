# Attempt problem 1 using while loop.


# Write a program to print multiplication table of a given number using for while

num = int(input("Enter Your Number: "))
print("Multiplication table of:", num)
i = 1
while i < 11:
    print(f"{num} X {i} = {num*i} ")
    i += 1
