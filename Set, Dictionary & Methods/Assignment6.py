# Task 1
# my_list = [1, 2, 3, 3, 4, 5, 1]
# my_set = set(my_list)
# my_list = list(my_set)
# print(my_list)
# print(type(my_list))
# my_list.pop(-1)
# print(my_list)
# print("*" * 50)

# Task 2
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}
# print(nums.union(letters))
# print(nums | letters)
# nums.update(letters)
# print(nums)

# Task 3
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}
# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update("A", "B")
# print(my_set)
# letters.intersection_update(my_set)
# print(letters)

# Task 4
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}
# print(set_one.issubset(set_two))

# Task 5
myDict = {
    "One": {"language": "HTML", "progress": "90%"},
    "Two": {"language": "CSS", "progress": "80%"},
    "Three": {"language": "Python", "progress": "30%"},
}
# Needed Output
print("{} Progress Is {}".format(myDict["One"]["language"], myDict["One"]["progress"]))
print("{} Progress Is {}".format(myDict["Two"]["language"], myDict["Two"]["progress"]))
print(
    "{} Progress Is {}".format(myDict["Three"]["language"], myDict["Three"]["progress"])
)
myDict["Four"] = {"language": "Ai", "progress": "20%"}
print(
    "{} Progress Is {}".format(myDict["Four"]["language"], myDict["Four"]["progress"])
)
myDict.update({"Five": {"language": "Js", "progress": "60%"}})
print(
    "{} Progress Is {}".format(myDict["Five"]["language"], myDict["Five"]["progress"])
)
