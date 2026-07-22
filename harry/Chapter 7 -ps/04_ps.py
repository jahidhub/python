# Write a program to find whether a given number is prime or not.


num = int(input("Enter your number: "))

for i in range(2, num):

    # jodi vag korar por jodi 0 thaka tar mana oi sonka vag kora jai , ta hola prime ba mowlik umber hoba na

    if (num % i) == 0:
        print("This is not a prime number")
        break

else:
    print("This is a prime number")
