# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
# example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students = ['Mike', 'Sara', 'Molly']
    first_student = students[1]
    last_student = students[2]
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ('pizza', 'pasta', 'burgers')
    meals = ''

    for food in foods:
        meals += food + ' ' #I tried the .append method and had initially had meals as an empty string in parentheses, wondering if it would work similar to a tuple, but since it's still a string the .append method didn't work. I got this portion of the code form ChatGPT to append, though I'm not sure what exactly it does. I recall similar formatting in the previous python labs. 

    return meals

# Call the function and print the result
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    foods = ('pizza', 'pasta', 'burgers')
    last_two_foods = slice(-2, None)
    return (foods[last_two_foods]) #Used this article to understand the slice methodhttps://www.w3schools.com/python/ref_func_slice.asp. I still coudldn't get it tor work, so then used ChatGPT to ask why it wasn't working. The -2 makes sense to me from the lesson, but not how it's used here nor does the non parameter. I don't really think I understand the slice method here as it wasn't part of the lesson, and I don't believe I've used in Javascript before if it's also applicable there (or if I have, I don't recall it).

# Call the function and print the result
print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # your code here
    hometown= {
        'city': 'Kendallville',
        'state' : 'Indiana',
        'population': 10000
    }

    home_town_message=(f"I was born in {hometown['city']}, {hometown['state']} - population of {hometown['population']}")
    return home_town_message
# Call the function and print the result
print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # your code here
    hometown= {
        'city': 'Kendallville',
        'state' : 'Indiana',
        'population': 10000
    }

    home_town_items = []
    for key, val in hometown.items():
        home_town_items.append(f"{key} = {val}")
    return home_town_items
# Call the function and print the result
print('Exercise 5:', list_home_town_items())
