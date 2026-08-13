# 1
# numbers = [1,2,3,4,5]
# def sqare(n):
#     return n * n
# result = map(sqare, numbers)
# print(list(result))


# create func to add gst in price:

prices = [124,152,541,445,]

def add_gst(price):
    return price + (price *  0.18)
result = map(add_gst ,prices)

print(list(result))

