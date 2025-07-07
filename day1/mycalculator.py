num1=float(input("Enter the num1: "))
num2=float(input("Enter the num2: "))
opr=input("Enter the operator: ")
output=None
if opr == "+":
    output=num1+num2
if opr == "-":
    output=num1-num2
if opr == "*":
    output=num1*num2
if opr == "/":
    output=num1/num2
print("my calculation is:",output)


#Conditionls

if num1 < 3:
    print("num1 is less than 3")
elif num1 == 3:
    print("num1 is equal to 3")
else:
    print("num1 is greater than 3")