

# for i in range(len(list_of_num)):
#     for j in range(len(list_of_num)):
#         if list_of_num[i] < list_of_num[j]:
#             temp = list_of_num[i]
#             list_of_num[i] = list_of_num[j]
#             list_of_num[j] = temp
# print(list_of_num)

list_of_num = [5,2,1]
for i in range(len(list_of_num)):
    for j in range(len(list_of_num) -1):
        if list_of_num[j] > list_of_num[j + 1]:
            temp = list_of_num[j]
            list_of_num[j] = list_of_num[j+1]
            list_of_num[j+1] = temp
print(list_of_num)