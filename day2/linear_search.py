list_of_env = ["dev","prd","stg","testing","qa"]
key = "qb"
is_found = False
for env in list_of_env:
    if env == key:
        is_found = True
if is_found:
    print("Found")
else:
    print("Not Found")
