#Input a list of Numbers from user i.e take integer inputs and append to list.

#Find the smallest and Second Smallest Numbers from that list


num = int(input("how many numbers you want to enter: "))
list=[]
for i in range(num):
    n=int(input(f"Enter a number{i +1} : "))
    list.append(n)
print(list)
list.sort()
print(list)

smallest=list[0]
second_sm=None
for small in list:
    if small > smallest:
        second_sm=small
        break
#print("smallest number is:",smallest ,"and second smallest is :",second_sm)
print(f"Smallest number is : {smallest} Second smallest is {second_sm}")