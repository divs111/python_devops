def linear_search(cloud_env,key):
    is_found = False
    for env in cloud_env:
        if env == key:
            is_found = True
    return is_found
    
# cloud_env = ["aws","azure","gcp"]
# key = "testing"
# found=linear_search(cloud_env,key)
# print(found)