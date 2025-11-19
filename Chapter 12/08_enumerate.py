# The ‘enumerate’ function adds counter to an iterable and returns it

l = [1, 2, 22, 4, 7, 6, 17, 9, 11, 12, 13]


# index = 0
# for item in l:
#     print(f"The number of index is {index} and value is {item}")
#     index += 1


for index, item in enumerate(l):
    print(f"The number of index is {index} and value is {item}")
