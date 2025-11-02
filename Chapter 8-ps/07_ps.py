# Write a python function to remove a given word from a list and strip it at the same
# time


def rem(li, word):
    n = []
    for item in li:
        # li.remove(word)
        # return li
        if not (item == word):
            n.append(item.strip(word))
    return n


list = ["Sohan", "Rohan", "Boni", "Sony", "an"]

print(rem(list, "an"))
