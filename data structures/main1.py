# #from functools import reduce
# import collections
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

# List Comprehensions

# 1. Filter the list of inventors for those who were born in the 1500's

# people = [inventor for inventor in inventors if inventor["year"] >= 1500 and inventor["year"] < 1600]
#
# print(people)
#
# # 2. Give us a list of the inventors first and last names
# people = [f"{inventor['first']} {inventor['last']}" for inventor in inventors]
# print(people




print(a == b)
