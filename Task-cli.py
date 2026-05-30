import sys
from Tasks import Task
import regex
import os

import json

if not os.path.exists("data.json"):
    with open("data.json", "w") as f:
        json.dump({}, f)
else:
    try:
        with open("data.json", "r") as f:
            json.load(f)
    except (json.JSONDecodeError, ValueError):
        with open("data.json", "w") as f:
            json.dump({}, f)


def help():
    print("Invalid command, here's the method to write them")
    print("""# Adding a new task
    task-cli add "Buy groceries"
    # Output: Task added successfully (ID: 1)

    # Updating and deleting tasks
    task-cli update 1 "Buy groceries and cook dinner"
    task-cli delete 1

    # Marking a task as in progress or done
    task-cli mark-in-progress 1
    task-cli mark-done 1

    # Listing all tasks
    task-cli list

    # Listing tasks by status
    task-cli list done
    task-cli list todo
    task-cli list in-progress
    """)

args=sys.argv
if len(args)<2:
    help()
elif args[1]=="add" and len(args)==3:
    Task(f"{args[2]}")
elif args[1]=="update" and len(args)==4:
    Task.update(args[2],args[3])
elif args[1]=="delete" and len(args)==3:
    Task.delete(args[2])
elif args[1].startswith("mark-") and len(args)==3:
    data=args[1].split("mark-")
    if data[1] not in ["in-progress","todo","done"]:
        print("Invalid option, try again")
    else:
        Task.mark(args[2],data[1])
elif args[1]=="list" and (len(args)==3 or len(args)==2):
    if len(args)==2: Task.listing("all")
    elif args[2] not in ["all","done","todo","in-progress"]:
        print("Invalid option,try again")
    else:
        Task.listing(args[2])
else:
    help()

