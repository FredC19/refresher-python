from functools import reduce
import string
from data import all_countries, country_info

def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

#Python allows a nested function to access the 
# outer scope(variables, etc) from the fucntion it is nested in

def add_ten():
    ten = 10
    def add(num):
        return num + ten #this variable is outside this function
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON




'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']



numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

names23 = ["g","h","gerbert","hessthegost","westside","southern"]
make_it_about_me = map(lambda x : x+": this post was sponsored by Fred",names23)
print(list(make_it_about_me))

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


#filter function
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

#Exercises

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#A map applies a function to a all the items in a given list
#A filter applies a function that outputs a boolean to all the items in a given list,
# and then if the ouptut of that function is True the item in the list stays.
# A reduce filter takes a function that takes in two or more elements to output an element and then
#applies it to all the list slowly to create the least elements

#Higher order functions take functions in as parameters
#Closure is when a nested function has access to the outer functions scope
#Decorators are higher order functions that take functions as parameters

def upper(list):
    return list.upper()

countries = map(upper,countries)
for country in countries:
    print(country)
    
numbers = map(lambda x : x*x,numbers)
for x in numbers:
    print(x)

names = map(lambda name : name.upper(),names)
print(list(names))

def contain_land(name):
    if "land" in name:
        return False
    else:
        return True 

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
result = filter(contain_land,countries)
print(list(result))

def long_countries(name):
    if len(name)==6:
        return False
    else:
        return True

def start_with_e(name):
    if name[0].upper()=="E":
        return False
    else:
        return True
    
result = filter(long_countries,countries)
print(list(result))
result = filter(start_with_e,countries)
print(list(result))


numbers=[1,2,3,4,5,6,7,8,9]
result = reduce(
    lambda x,y : x*y,
    filter(
    lambda x : x if x % 2 ==0 else False
    ,numbers
)
)
print(result)


def is_string(name):
    if type(name)==str:
        return True
    else:
        False

def get_string_lists(list_tbc):
    result = filter(is_string,list_tbc)
    print(list(result))

list_or = [3,5,6,7,8,"Fred","fdjhg","gjhdgj"]
get_string_lists(list_or)

print(numbers)
print(reduce((lambda x,y: x*y),numbers))

print(f"{reduce((lambda x,y: x + ", " + y), countries[0:len(countries)-1])} and {countries[len(countries)-1]} are north Europian countries")

stan_countries = filter((lambda x : x if "stan" in x else False), all_countries)
print(list(stan_countries))
stan_countries = filter((lambda x : x if "island" in x.lower() else False), all_countries)
print(list(stan_countries))



alphabet = list(string.ascii_lowercase)

def countries_dict(the_list):
    alphabet_dict = {letter: [] for letter in string.ascii_uppercase}
    for country in all_countries:
        alphabet_dict[country[0]].append(country)
    return alphabet_dict

print(countries_dict(all_countries))

def get_first_10(list):
    return list[:10]

def get_last_10(list):
    new_list=[]
    for x in range(len(list)-10,len(list)):
        new_list.append(list[x])
    return new_list

print(get_first_10(all_countries))
print(get_last_10(all_countries))

#more efficient way
print(all_countries[-10:])

countries_by_name = sorted(country_info , key=lambda c: c['name'])
print(countries_by_name)
