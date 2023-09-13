list1 = [1, 2, 3, 4, 5]
list2 = [1, -2, 3, -4, 5]

# res = [n * -1 for n in list2]
# print(res)

# i = 0
# while i < len(list1):
#     if list1[i] > 0:
#         print(list1[i] * -1, end=', ')
#         i += 1
#     elif list1[i] < 0:
#         print(abs(list1[i]), end=', ')
#         i += 1

for i in list1:
    if i > 0:
        print(i * -1, end=', ')
    elif i < 0:
        print(abs(i), end=', ')



