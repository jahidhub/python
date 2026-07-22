# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}

# lang = {
#     "sohan": "bangla",
#     "rohan": "english",
#     "boni": "china",
#     "foisal": "hinde",
# }

name = input('Enter your name:')
lang = input('Enter your lang:')

d.update({name: lang})
name = input('Enter your name:')
lang = input('Enter your lang:')

d.update({name: lang})
name = input('Enter your name:')
lang = input('Enter your lang:')

d.update({name: lang})
name = input('Enter your name:')
lang = input('Enter your lang:')

d.update({name: lang})


print(d)  # {'Rakib': 'bangla', 'raju ': 'english', 'priya': 'hinde', 'royal': 'urdu'}
