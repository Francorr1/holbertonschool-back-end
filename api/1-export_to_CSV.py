#!/usr/bin/python3
"""  using a REST API, for a given employee ID, returns information """
import csv
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
    completed = len(completed_res.json())
    total = len(total_response.json())
    print(f"Employee {user_name} is done with tasks({completed}/{total}):")
    for x in completed_res.json():
        print(f"\t {x.get('title')}")

    filename = f"{user_id}.csv"
    with open(filename, 'w', encoding='UTF8') as f:
        write = csv.writer(f)
        for elem in total_response.json():
            f.write('"{}","{}","{}","{}"\n'.format(
                user_id, user_name, elem["completed"], elem["title"]
            ))
