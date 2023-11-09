# Task 1
Name = ("Abdelrahman",)
print(type(Name))
print("*" * 50)

# Task 2
friends = ("Osama", "Ahmed", "Sayed")
friends = ("Elzero",) + friends[1:]
print(friends)
print(type(friends))
print(f"{len(friends)} Elements")
print("*" * 50)

# Task 3
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")
print("*" * 50)

# Task 4
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)
