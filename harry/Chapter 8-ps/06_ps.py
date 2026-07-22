# Write a python function which converts inches to cms
# multiply the length value by 2.54

def inches_cms(inch):
    return inch * 2.54


num = int(input("enter your inch number: "))
print(f"Your cms: {inches_cms(num)}")
