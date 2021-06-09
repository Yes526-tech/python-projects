import itertools
from functools import reduce

tasks = [
    {
        'name': 'Write for Envato Tuts+',
        'duration': 120
    },
    {
        'name': 'Work out',
        'duration': 60
    },
    {
        'name': 'Procrastinate on Duolingo',
        'duration': 240
    }
]

# result = sum(task['duration'] for task in tasks)
# result2 = min(task['duration'] for task in tasks)
# print(result2)

# OOP

def filterByDuration(duration):
    return list(filter(lambda x: x['duration'] == duration, tasks))

result = filterByDuration(60)

print(result)
# sum(task['duration'] for task in tasks)


# result = reduce((lambda a, b: a + b['duration']), tasks, 0)
# print(result)
# def sum_task_duration():
#     total = 0
#     for task in tasks:
#         total += task["duration"]
#     print(total)
#
# sum_task_duration()
# def add_task(name, duration):
#     tasks.insert(len(tasks), {'name': name, "duration": duration})
#
#
# def add_task2(name, duration):
#     tasks.insert(0, {'name': name, "duration": duration})
#
#
# add_task('Tidy your room', 20)
# add_task2('Tidy your room2', 200)


# print(tasks)

# users = {
#     0: {"name": 'Adam', "age": 23},
#     1: {"name": 'John', "age": 28},
#     2: {"name": 'William', "age": 34},
#     3: {"name": 'Oliver', "age": 28}
# }
#
# group = {
#     "admin": [0, 1],
#     "editor": [2, 3]
# }


#
# def make_admin(id):
#     for user_id in users.keys():
#         if user_id == id:
#             if users[id]["group"] == "admin":
#                 choice = input("wanna make him/her a editor:")
#                 if choice == "yes":
#                     users[id]["group"] = "editor"
#             else:
#                 choice = input("wanna make him/her a admin:")
#                 if choice == "yes":
#                     users[id]["group"] = "admin"
#
#
# make_admin(85)
# print(users)
# ------------------------------------------------------------------------------------------------------
# {key: value} =  11: {id: 11, "name": 'Adam', "age": 23, "group": 'editor'} (key1, value1)

# true or false
# def is_admin(id):
#     for user_id in users.keys():
#         if user_id == id:
#             if users[id]["group"] == "admin":
#                 return True
#
#     return False
# print(is_admin(id))
# ------------------------------------------------------------------------------------------------------

# print(hasattr(users, '__iter__')) ===>>>>> Iterable ?
# def getIdByName(id):
#     for name_id in users.keys():
#         if name_id == id:
#             print(users[name_id]["name"])
# getIdByName(85)
