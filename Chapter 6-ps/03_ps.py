"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
"""


spams1 = "Make a lot of money"
spams2 = "buy now"
spams3 = "subscribe this"
spams4 = "click this"


massage = input("Enter your nice comment in  here: ")


if ((spams1 in massage) or (spams2 in massage) or (spams3 in massage) or (spams4 in massage)):
    print("This is a spams comment.")
else:
    print("This is not a spams comment.")