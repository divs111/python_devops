import os
import sys

my_name = os.getenv("MY_NAME")
print(f"Hello {my_name}")

if len(sys.argv) > 3:
    print("Usage : python3 env_args.py <num1> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(f"args received: {num1} and {num2}")
print(f"sum of args : {num1 + num2}")
print(f"sub of args are : {num1 - num2}")

if os.getenv("SHOW_GREETINGS") == "yes":
    print(f"Glad to see you {my_name} and you passed {num1} and {num2}")
    