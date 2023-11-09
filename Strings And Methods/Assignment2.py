# Task 1
myName = "Abdelrahman Morsy"
myAge = "20"
myCountry = "Egypt"
print(
    f'"Hello \'{myName}\', How You Doing \\ """ Your Age Is "{myAge}"" + And Your Country Is: {myCountry}'
)
# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

# Task 2
print(
    f'Hello \'{myName}\', How You Doing \\\n\
""" Your Age Is "{myAge}"" +\n\
And Your Country Is: {myCountry}'
)
# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

# Task 3
name = "Elzero"

print(name[1])
print(name[2])
print(name[-1])
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"

# Task 4
name = "Elzero"
print(name[1:4])
print(name[::2])
print(name[::2][::-1])
# Needed Output
# "lze"
# "Ezr"
# "rzE"

# Task 5
name = "#@#@Elzero#@#@"
print(name.strip("#@"))
# Needed Output
# Elzero

# Task 6
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))
# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

# Task 7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

# Task 8
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
# Needed Output
# osAMa
# OSAma

# Task 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
# Needed Output
# 2

# Task 10
name = "Elzero"
print(name.index("z"))
# Needed Output
# 2

# Task 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))
# Needed Output
# I Love Python And Although <3 Elzero Web School

# Task 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))
# Needed Output
# I Love Python And Although Love Elzero Web School

# Task 13
name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {myName}, And My Age Is {myAge}, And My Country Is {myCountry}")
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
