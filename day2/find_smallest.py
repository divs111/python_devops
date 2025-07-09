#Input a list of Numbers from user i.e take integer inputs and append to list.

#Find the smallest and Second Smallest Numbers from that list


num=int(input("enter a num:"))
list=[]
for i in range(num):
    n=int(input(f"Enter a number {i + 1}:"))
    list.append(n)
print(list)

list.sort()
print(list)
smallest=list[0]
second_sm=None
for number in list:
    if number > smallest:
        second_sm = number
        break
print("smallest number: ",smallest)
print("second smallest: ",second_sm)

