#!/usr/bin/python3
"""  using a REST API, for a given employee ID, returns information
about his/her TODO list progress """


import requests
import sys
user_id = sys.argv[1]
res = f"todos?userId={user_id}&completed=true"
user_info = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{user_id}")
total_response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
completed_res = requests.get(f"https://jsonplaceholder.typicode.com/{res}")
user_name = user_info.json()["name"]
completed = len(completed_res.json())
total = len(total_response.json())
print(f"Employee {user_name} is done with tasks({completed}/{total}):")
for x in completed_res.json():
    print(f"\t {x.get('title')}")
