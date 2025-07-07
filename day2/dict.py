dict_of_items_1 = {
    "env" : "dev",
    "server" : "ubuntu",
    "ram" : 8096,
    "cpu" : 4,
    "active": True
}
dict_of_items_2 = {
    "env" : "prd",
    "server" : "ubuntu",
    "ram" : 8096,
    "cpu" : 4,
    "active": False
}
env_lists = [dict_of_items_1,dict_of_items_2] # creating list of dict
for env in env_lists:  # iterating it now
    for key,value in env.items():
        if key == "active" and value == True:
            print(env)
            print(env.values())
#print(dict_of_items.get("env"))
# if dict_of_items["active"]:
#     print("Server details")
#     print("Environment is: ",dict_of_items["env"])
