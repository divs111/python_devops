import sys
import calc

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = calc.add(num1,num2)
    print(output)
if operation == "sub":
    output = calc.sub(num1,num2)
    print(output)
if operation == "mul":
    output = calc.mul(num1,num2)
    print(output)

