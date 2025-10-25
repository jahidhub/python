# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s = set()

user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))
user_num = input("Enter your number:")
s.add(int(user_num))

print(s)
