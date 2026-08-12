# Write a program which finds out whether a given name is present in a list or not.

list = ["Sohan", "Rohan", "Rakib", "Raju", "Sakib"]

user = input("Enter your name and check you in a list or not: ")

if user in list:
    print("Your are in a list")
else:
    print("Your are not in list")
