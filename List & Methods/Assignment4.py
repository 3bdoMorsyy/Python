# Task 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])
print("_" * 50)

# Task 2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])
print("_" * 50)

# Task 3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])
print("_" * 50)

# Task 4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[3:] = ["Elzero", "Elzero"]
print(friends)
print("_" * 50)

# Task 5
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)
print("_" * 50)

# Task 6
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove("Nasser")
friends.pop(0)
print(friends)
friends.pop(-1)
print(friends)
print("_" * 50)

# Task 7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)
print("_" * 50)

# Task 8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
print("_" * 50)

# Task 9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
print("_" * 50)

# Task 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])


