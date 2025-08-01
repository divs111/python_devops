import builtins
cloud_env = ["aws", "azure","gcp"]

try:
    print(cloud_env[5])
except:
    print("Exception handled")
finally:
    print("this will run anyways")
#raise Exception("This is a new exception")

try:
    print(cloud_env[200])
except IndexError as e:
    print("1", e)
except ZeroDivisionError as e:
    print("2",e)

print(dir(builtins))