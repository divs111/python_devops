# write a program to print the output in dictionary.
# cars = ["audi","audi","audi","bmw","jaguar","jaguar"] --output-  {'audi':3,'bmw':1,'jaguar':2}

# cars = ["audi","audi","audi","bmw","jaguar","jaguar"]
# final_car_count={}
# for car in cars:
#     if car not in final_car_count:
#         final_car_count.update({car:1})
#     else:
#         final_car_count.update({car:final_car_count[car]+1})
# print(final_car_count)


environment = ["uat", "dev", "prd"]
#print(len(environment))

device_info = {
    "name" : "macbook pro",
    "ram" : "16GB",
    "memory" : "256GB"
}
print(device_info.get("name"))
device_info.update({"environments" : environment})
print(device_info)

device_id1 = {1,2,3,1,2,3,3,4,5,6,7}
device_id2 = {11,12,13,12,1}
print(len(device_id1))
print(device_id1.union(device_id2))
print(device_id1.intersection(device_id2))
