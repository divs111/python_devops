#set- we've mention sthg in curly brace like set = {None} , if empty, we call it a dict.
# set does not contain duplicates
# sets sorts the data as well

set_1 = {1,2,1,3,4,45,65}
set_2 = {1,3,45,5,6,7}
print(set_1.intersection(set_2))
#print(set_2)
#print(set_1.union(set_2))

list_of_env = ["dev","uat","prd","stg","dev","prd"]
list_of_env = list(set(list_of_env))
print(list_of_env)