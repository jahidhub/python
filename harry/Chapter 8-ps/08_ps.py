# Write a python function to print multiplication table of a given number.


def multi(n):
    for item in range(1, 11):
        print(f"{n} X {item} = {n* item}")

n = int(input("Enter yout multiplication Number: "))
multi(n)