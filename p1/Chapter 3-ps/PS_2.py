# name = input('Enter your name:')
# date = input('Enter your date:')

# letter = f"""
# Dear <|{name}|>,
# You are selected!
# <|{date}|>

# """

# print(letter)


letter = """
Dear <|{name}|>,
You are selected!
<|{date}|>
"""

print(letter.replace("<|{name}|>", "Sohan").replace("<|{date}|>", '24 sept 2025'))
