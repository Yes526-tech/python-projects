from functools import reduce

# # inventors = [
# #     {"first": "Albert", "last": "Einstein", "year": 1879, "passed": 1955},
# #     {"first": "Isaac", "last": "Newton", "year": 1643, "passed": 1727},
# #     {"first": "Galileo", "last": "Galilei", "year": 1564, "passed": 1642},
# #     {"first": "Marie", "last": "Curie", "year": 1867, "passed": 1934},
# #     {"first": "Johannes", "last": "Kepler", "year": 1571, "passed": 1630},
# #     {"first": "Nicolaus", "last": "Copernicus", "year": 1473, "passed": 1543},
# #     {"first": "Max", "last": "Planck", "year": 1858, "passed": 1947},
# #     {"first": "Katherine", "last": "Blodgett", "year": 1898, "passed": 1979},
# #     {"first": "Ada", "last": "Lovelace", "year": 1815, "passed": 1852},
# #     {"first": "Sarah E.", "last": "Goode", "year": 1855, "passed": 1905},
# #     {"first": "Lise", "last": "Meitner", "year": 1878, "passed": 1968},
# #     {"first": "Hanna", "last": "Hammarström", "year": 1829, "passed": 1909}
# # ]
# #
# # x = list(map(lambda inventor: f"{inventor['first']} {inventor['last']}", inventors))
# # print(x)
# #
# # def combine(inventor):
# #     return f"{inventor['first']} {inventor['last']}"
# #
# # print(list(map(combine, inventors)))
#
#
# point = 1,2
# print(type(point))
#
#
# from collections import deque
# queue = deque([])
# queue.append(21)
#
# queue.append(1)
#
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
#


# numbers = [1, 1, 2, 3, 4, 5]
# first = set(numbers)
# second = {5, 6}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)


# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# # point["z"] = 20
# # if "a" in point:
# #     print(point["a"])
# # print(point.get("a", 0))
# # del point["x"]
# # print(point)
# # for key, value in point.items():
# #     print(key, value)
#
#
#
#
# values = [x * 2 for x in range(5)]
# print(values)
# values = {x * 2 for x in range(5)}
# print(values)
# values = {x: x * 2 for x in range(5)}
# print(values)
#
#
# values = {}
# for x in range(5):
#     x = x * 2
#     values += x
# print(values)
#
#
#
# from sys import getsizeof
#
# values = x * 2 for
#
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first,  **second, "z": 1 }
# print(combined)

inventors = [
    {"first": "Albert", "last": "Einstein", "year": 1879, "passed": 1955},
    {"first": "Isaac", "last": "Newton", "year": 1643, "passed": 1727},
    {"first": "Galileo", "last": "Galilei", "year": 1564, "passed": 1642},
    {"first": "Marie", "last": "Curie", "year": 1867, "passed": 1934},
    {"first": "Johannes", "last": "Kepler", "year": 1571, "passed": 1630},
    {"first": "Nicolaus", "last": "Copernicus", "year": 1473, "passed": 1543},
    {"first": "Max", "last": "Planck", "year": 1858, "passed": 1947},
    {"first": "Katherine", "last": "Blodgett", "year": 1898, "passed": 1979},
    {"first": "Ada", "last": "Lovelace", "year": 1815, "passed": 1852},
    {"first": "Sarah E.", "last": "Goode", "year": 1855, "passed": 1905},
    {"first": "Lise", "last": "Meitner", "year": 1878, "passed": 1968},
    {"first": "Hanna", "last": "Hammarström", "year": 1829, "passed": 1909}
]

# 1. Filter the list of inventors for those who were born in the 1500's

# x = filter(lambda inventor: inventor["year"] >= 1500 and inventor["year"] < 1600, inventors)
# print(list(x))

# 2. Give us a list of the inventors first and last names

# x = map(lambda inventor: f"{inventor['first']} {inventor['last']}", inventors)
# print(list(x))

# // 3. Sort the inventors by birthdate, oldest to youngest
#
# inventors.sort(key=lambda inventor: inventor["year"])
# print(inventors)
#
# x = sorted(inventors, key=lambda inventor: inventor["year"])
# print(x)

# // 4. How many years did all the inventors live all together?
# ages = map(lambda inventor: inventor["passed"] - inventor["year"], inventors)
# x = reduce(lambda a, b: a + b, ages)
# print(x)
# print(sum(map(lambda inventor: inventor["passed"] - inventor["year"], inventors)))