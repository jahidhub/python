# try:
#     p = int(input("Enter a number: "))

# except ValueError as e:
#     print(e)

# else:
#     print("In a else")

try:
    p = int(input("Enter a number: "))

except ValueError as e:
    print(e)

finally:
    print("In a finally")
