# users = {
#     11: {id: 11, "name": 'Adam', "age": 23, "group": 'editor'},
#     47: {id: 47, "name": 'John', "age": 28, "group": 'admin'},
#     85: {id: 85, "name": 'William', "age": 34, "group": 'editor'},
#     97: {id: 97, "name": 'Oliver', "age": 28, "group": 'admin'}
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

