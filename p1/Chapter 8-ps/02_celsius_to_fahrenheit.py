# Write a python program using function to convert Celsius to Fahrenheit.

# f = (c*9/5) +32

# c= (f-32)*5/9

# c/5 = (f-32)/9


def convert_c_to_f(c):
    # f = (c * 9 / 5) + 32
    f = (9 / 5 * c) + 32
    return f


Celsius = int(input("Enter a celsius Number: "))

rounded = round(convert_c_to_f(Celsius))
print(f"Fahrenheit Output: {rounded} °F")
