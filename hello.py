#python learning phase

# first_name="simran kumari"
# user_age="25"
# print(user_age)

# total=10-7
# print(total)

# my_long_string= """
# my name is simran kumari
# my hobby is playing badminton
# """
# print(my_long_string)

# first_name="simran"
# last_name="kumari"

# new_name=first_name+" "+last_name
# print(new_name)

# long_dash="-"*15
# print(long_dash)

# print(len(new_name))

# is_true=True
# age=89
# can_vote= age>=18
# print(can_vote)

# name="simran"
# string = f"hi there, my name is {name}"
# print(string)

# name="dave"
# print(name.upper())

# name.lower()
# print(name.title())

# text = "Python Programming"

# print(text.lower())      # "python programming"
# print(text.upper())      # "PYTHON PROGRAMMING"
# print(text.title())      # "Python Programming"

# temp=26
# if temp>25:
#     print("it's hot!")
# else:
#     print("it's nice weather")

    
#     age = 13
# if age >= 18:
#     print("You can vote!")
#     print("You're an adult")

# temperature = 25

# if temperature > 30:
#     print("It's hot!")
# else:
#     print("Nice weather!")
# has_ticket=True
# age=19
# if has_ticket:
#     if age>=18:
#         print("enjoy the movie!")
#     else:
#         print("needs of supervision")
# else:
#     print("please buy ticket")

# for i in range(0, 10, 3):
#     print(i)

# age=25
# has_license=False

# my_list=["simran", 25,True, has_license]

# name=my_list[0]
# print(name)
# age=my_list[1]
# print(age)
# has_license=my_list[1]
# print(has_license)

# Empty dictionary
# my_dict = {}

# # Dictionary with data
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(person)

# # Different ways to create
# scores = dict(math=95, english=87, science=92)
# # print(scores)
# # print(person)
# print(scores["math"])
# for score in scores:
#    print(score," is " ,scores[score])

# Empty set (careful!)
# empty_set = set()  # NOT {} - that's a dict!

# # Set with values - both ways work
# numbers = {1, 2, 3, 4, 5}
# fruits = set(["apple", "banana", "orange"])

# # From a list (removes duplicates)
# scores = [85, 90, 85, 92, 90]
# unique_scores = set(scores)  # {85, 90, 92}
# print(unique_scores)

# def greet():
#     print("Hello, world!")
#     print("Welcome to Python!")

# # Call the function
# greet()
 
# name="simran"
# i=name[2]
# print(i)

# person={
#     "name": "simran",
#     "age": 20,
#     "branch": "CSE",
#     "batch": "2023"
# }

# print(person.get("job"))

# def check_weather():
#     temperature = 234
#     if temperature > 30:
#         print("It's hot!")
#     else:
#         print("Nice weather!")

# # Use the function
# check_weather()

# def func(name):
#      print(f"hello,{name}")
#      return 25

# func("simran")
# print(age)

# Bad - using global variable
# total = 0


# Good - using parameters and return
# print(total)
# def add_amounts(current_total, amount):
#     return current_total + amount

# total = 0
# total = add_amounts(total, 10)
# total = add_amounts(total, 20)
# print(total)  # 30

# Pattern 1: Import the whole module
# import math
# Now use: math.sqrt(16)
# print(math.sqrt(16))

# Pattern 2: Import specific items from a module
# from math import sqrt, pi
# Now use: sqrt(16)
# print(math.sqrt(16))

# Import entire module
# import random

# # Use module functions
# number = random.randint(1, 10)
# print(number)
# print(number)
# print(number)
# choice = random.choice(["apple", "banana", "orange"])


