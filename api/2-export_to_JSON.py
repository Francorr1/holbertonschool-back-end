#!/usr/bin/python3
"""  using a REST API, for a given employee ID, returns information """
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    res = f"todos?userId={user_id}&completed=true"
    user_info = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}")
    total_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    completed_res = requests.get(f"https://jsonplaceholder.typicode.com/{res}")
    user_name = user_info.json()["name"]
    user_username = user_info.json()["username"]
    completed = len(completed_res.json())
    total = len(total_response.json())
    print(f"Employee {user_name} is done with tasks({completed}/{total}):")
    for x in completed_res.json():
        print(f"\t {x.get('title')}")

    list_to_json = []
    for values in total_response.json():
        new_list = {"task": "{}".format(str(
            values["title"])), "completed": values["completed"],
            "username": "{}".format(str(user_username))}
        list_to_json.append(new_list)
    dict_to_json = {"{}".format(str(user_id)): list_to_json}

    with open("{}.json".format(user_id), mode="w", encoding="UTF8") as file:
        json.dump(dict_to_json, file)
