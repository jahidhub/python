
# *****
# *****
# *****
# *****
# *****

# rows = 5
# cols = 5

# for i in range(rows):
#     for j in range(cols):
#         print("*" , end=" ")
#     print()
    


# 1-10
# - 100

# rows = 10
# cols = 10
# num = 1

# for i in range(rows):
#     for j in range(cols):
#         print(num , end= " ")
#         num += 1
#     print()



# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# for row in range(1 ,6):
#     for col in range(1 , row+1 ):
#         print(col , end=" ")
#     print()



# while loop

# *****
# *****
# *****
# *****
# *****



# rows= 5
# cols= 5
# i = 1
# while i<= rows:
#     j = 1
#     while j <= cols:
#         print( "*", end=" " )
#         j += 1
#     print()
#     i += 1


# 1 to 5 namta

# 1*1 = 1
# 1*2 = 2
# 1*3 = 3
# 1*4 = 4
# 1*5 = 5
# 1*6 = 6
# 1*7 = 7
# 1*8 = 8
# 1*9 = 9
# 1*10 = 10
# ----------------
# 2*1 = 2
# 2*2 = 4
# 2*3 = 6
# 2*4 = 8
# 2*5 = 10
# 2*6 = 12
# 2*7 = 14
# 2*8 = 16
# 2*9 = 18
# 2*10 = 20


t = 5
num = 1
n= 10

while num <= t:
    i = 1
    while i <= n:
        print(f"  {num} * {i} = {num * i}")
        i+=1 
    print("-"* 15)
    num += 1