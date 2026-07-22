# Write a program to find the greatest of four numbers entered by the user

p1 = int(input("Enter your number 1: "))
p2 = int(input("Enter your number 2: "))
p3 = int(input("Enter your number 3: "))
p4 = int(input("Enter your number 4: "))

if (p1 > p2) & (p1 > p3) & (p1 > p4):
    print("The greatest of P1:", p1)

elif (p2 > p1) & (p2 > p3) & (p2 > p4):
    print("The greatest of P2:", p2)
elif (p3 > p1) & (p3 > p2) & (p3 > p4):
    print("The greatest of P3:", p3)
elif (p4 > p1) & (p4 > p2) & (p4 > p3):
    print("The greatest of P4:", p4)

else:
    print("the not greatest")
