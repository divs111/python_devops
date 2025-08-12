# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests
url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)
#print(response.json())
if response.status_code == 200:
    pull_request = response.json()

    pr_creator ={}
    for pr in pull_request:
        creator = pr["user"]["login"]
        #print(creator)
        if creator in pr_creator:
            pr_creator[creator] += 1
            #print(pr_creator[creator])

        else:
            pr_creator[creator] = 1

    for creator , count in pr_creator.items():
        print(f"{creator} : {count} PRs")
else:
    print(f"failed to fetch data, StatusCode : {response.status_code}")