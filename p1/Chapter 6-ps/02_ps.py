"""
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.

"""

bangla = int(input("Enter your Bangla marks: "))
english = int(input("Enter your English marks: "))
math = int(input("Enter your Math marks: "))

total_percent = ((bangla + english + math) * 100) / 300

if (total_percent >= 40) & (bangla >= 33) & (english >= 33) & (math >= 33):

    print(f"Congratulations! You have passed : {total_percent}")

else:
    print(f"Your are failed. better luck next time : {total_percent}")
