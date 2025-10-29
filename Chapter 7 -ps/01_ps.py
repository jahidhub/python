# Write a program to print multiplication table of a given number using for loop
num = int(input("Enter Your Number: "))
print("Multiplication table of:", num)
for i in range(1, 11):
    print(f"{i} x {num} =  {i * num}")
