
#-----------------------------------------------
# Start script

#-----------------------------------------------
# Print hello
print('-----------------------------------------------')
print('Hello Python')

#-----------------------------------------------
# Comments

# A comment

print('Comment') # This is again comment

'''
This is a multiline
comment.
'''

#-----------------------------------------------
print('-----------------------------------------------')
print('Functions')
# Functions

#------------------------------------
# Use 'def' to declare a function with a name. 
# Place parameters inside parametheses to pass arguments to function
def my_function(param):

    # parameters = names used when defining a function or a method (arguments will be mapped
    # to when calling a function)

    # arguments = values supplied on function or method call

    # Argument types:
    # - Default arguments
    # - Required positional arguments:
    # - Keyword arguments
    # - Variable number of arguments (*args)
    # - Variable number of Keyword arguments (**kwargs)

    print('\nCalled my_function')

    # Do some operation
    ret = param * 5

    # return from function
    # End  function with a return statement if the function should output something. 
    # Without the return statement, your function will return an object 'None'.
    return ret

# Call the function
result = my_function(5)

#------------------------------------
# Argument types
def my_function_args(req_arg, def_arg1 = 5, def_arg2 = 15, *args, **kwargs):

    # Argument types:
    # - Required positional arguments: have to be passed in the right order
    # - Default arguments: default value if no argument value is passed
    # - Keyword arguments: identify the arguments by their parameter name (have to the last arguments to pass)
    # - Non-keyworded variable length argument list: *args by convention
    # - keyworded variable length argument list: **kwargs by convention

    print('\nCalled my_function_args')
    print('Argument types')

    #print('Required argument: ' + str(req_arg)
    print('Required positional argument: ', req_arg)

    print('Default argument 1: ', def_arg1)
    print('Default argument 2: ', def_arg2)

    print('Non-keyworded variable length argument list:')
    for arg in args:
        print("item in *argv: ", arg)

    print('Keyworded variable length argument list:')
    for key, value in kwargs.items():
        print("Item in **kwargs: {0} = {1}".format(key, value))


# Call the function with positional arguments
my_function_args(5, 10, 60, 'arg_var1', 'arg_var2', 30, kw_arg1 = 'someval', kw_arg2 = 'otherval')

# Call the function with Keyword arguments (can change the order, but have to the last arguments to pass)
my_function_args(35, def_arg2 = 1, def_arg1 = 45)

#------------------------------------
# Function can return multiple values
def my_function_multiple(param):
    # Do some operation
    reta = param * 5
    retb = param * 10
    # return multiple values
    return reta, retb


# Get multiple returns
resulta, resultb = my_function_multiple(5)
print(resulta, resultb)

# Ignore a return value
resulta, _ = my_function_multiple(20)
print(resulta)

#------------------------------------
# Docstrings
# Docstrings describe what your function does
# docstrings are placed in the immediate line after the function header and in between triple quotation marks.
def my_function_doc():
    """Prints 'Function Doc'.

    Returns:
        None
    """

    print('\nCalled my_function_doc')

#------------------------------------
# Anonymous / lambda functions

my_lambda_function = lambda x: x*2

print('\nLambda function:')
print(my_lambda_function(100))

#-----------------------------------------------
print('-----------------------------------------------')
print('Classes')

# Classes, methods, extendind classes

# First argument of class method is always a reference to the current instance of the class,
# called 'self' by convention.
# When calling a method (eg. instance.method(), self is implicitly inserted as
# first argument (don't pass it explicitly).


# Base Class
class BaseClass:
    # Attributes - default
    # Creates and init refnumber attribute
    refnumber = 5

    # Constructor (optional)
    def __init__(self, new_number):
        # Creates and init number attribute
        self.number = new_number

    # Method
    def change_number(self, new_number):
        self.number = new_number

    def change_refnumber(self, new_number):
        self.refnumber = new_number

# Extending a class
# Extended Class
class ExtendedClass(BaseClass):

    # Attributes - default
    name = 'default name'

    def change_name(self, new_name):
        self.name = new_name

# Use extended class (will call base class constructor)
myinstance = ExtendedClass(10)

# Print attributes
print("\nPrint Class attributes")
print(myinstance.refnumber)
print(myinstance.number)
print(myinstance.name)

# Change attributes
myinstance.change_name('other name')
myinstance.change_number(20)
myinstance.change_refnumber(50)

# Print changed attributes
print("\nPrint changed Class attributes")
print(myinstance.refnumber)
print(myinstance.number)
print(myinstance.name)

#-----------------------------------------------
print('-----------------------------------------------')
print('Type basic')
# Basic

# dynamically typed language: variable name is bound only to an object not a type
var1 = 5
var1 = 'Now a string '
var2 = 10

# strongly typed language: explicit conversion is required
new_str = var1 + str(var2)
print(new_str)


# None, True, False

# principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.

# Operators
#- Arithmetic Operators
#- Comparison (Relational) Operators
#- Assignment Operators
#- Logical Operators
#- Bitwise Operators
#- Membership Operators
#- Identity Operators

# Note: Change default behavior: Class methods, eg. __bool__() ; __len__()  ; __eq__()

# Numeric Types — int, float, complex
# math operation (and math and cmath modules)


# Multiple Assignment
# Single value to several variables
a = b = c = 1
# Assign multiple objects to multiple variables
a,b,c = 1,2,"john"


# Global vs Local Variables. Force local ('local')

# get variable type

# Attributions (Multiples)

# pass
# does nothing, used when a statement is required syntactically but the program requires no action


#-----------------------------------------------
# Strings
print('----------------------------------------------')
print('Strings')

# Python accepts single ('), double (")
str_word = 'word'
str_sentence = "This is a sentence."

# Triple (''' or """) quotes used to span across multiple lines
str_paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

# formating
# {0}.{1}.format

#-----------------------------------------------
# output
# print(str, end='')

# after change end, must restore
#print(end='\n')

#-----------------------------------------------
# Conditionals
print('----------------------------------------------')
print('Conditionals')

#test_bool = True
test_bool = False

if test_bool:
   print("True")
else:
   print("False")

test_num = 0

if test_num == 0:
   print("Zero")
elif test_num > 0: 
   print("Positive")
else:
   print("Else")



#-----------------------------------------------
# Loops
print('-----------------------------------------------')
print('Loops')

# range: generate a sequence of integer numbers (range object)
# range (stop)
# range (start, stop[, step])
# exclusive (stop not included)

# for 
for i in range(1, 6, 2):
    print(i, end=', ')

print(end='\n')

loop_list = [1,2,3,4,5]
for i in range(len(loop_list)):
    print(i, end=', ')

print(end='\n')


 # while
count = 0
while (count < 9):
    count = count + 1


# Behind the scenes, the for statement calls iter() on the container object. The iter() returns an iterator object 
# that defines the method __next__() which accesses elements in the container one at a time.
# When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. 

# break and continue Statements

#-----------------------------------------------
# Multi-Line Statements
print('----------------------------------------------')
print('Multi-Line Statements')

# Statements typically end with a new line. Line continuation character = backslash (\) denote that the line should continue.
# Statements contained within the [], {}, or () brackets do not need to use the line continuation character.

total = 1 + \
        2 + \
        3


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

#-----------------------------------------------
# Collections : containers used to store collections of data
print('----------------------------------------------')
print('Collections')

# Built-in:
# - list, sequence, mutable, usually homogeneous, defined with square brackets []
# - tuple: sequence, immutable, faster than list, usually heterogeneous, defined with parenthesis ()
# - set: sequence, unique elements, defined with  set() function or curly braces {}
# - string: sequence characters, define with "" or '' or """ for multiline 
# - dict (dictionary): mapping, maps key = value, defined with curly brackets and key value pair {'key': value}


my_list = [20, 21, 22, 23]
print(my_list[1])
my_list[1] = 60
print(my_list[1])

my_tuple = (10, 15, 20, 'dog')
# tuple does not support item assignment, eg: my_tuple[1] = 35
print(my_tuple[1])
print(my_tuple[3])

nonunique_list = [20, 21, 22, 21, 20]
unique_list = set(nonunique_list)
print(unique_list)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

my_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
print(my_dict['key2'])
my_dict['key2'] = 'val4'
print(my_dict['key2'])
for k, v in my_dict.items():
    print(k, ' = ', v)

# iterable interface: An object capable of returning its members one at a time (iter() returns an iterator object).
# iterable has 3 descendants: sequence, mapping, generator
# - sequence: iterable with random access. supports slicing
# - mapping: elements accessed via keys instead of integers
# - generator: no random access, consume items in order. Only create items when iterate over them.
#              A function that uses yield returns a generator.

# slicing: create a slice (sequence subset) with start, stop, step

# Built-in collections have Functions to handle data


#-----------------------------------------------
# Error handling

#try:
    #sentence - do something
#except ValueError:
    # error handling
    #pass
#except (RuntimeError, TypeError, NameError):
    #pass
#finally:
    #Clean-up Actions
    #pass

# if exception type matches the exception named after the except keyword, the except clause is execute

#Raising Exceptions
#raise NameError('HiThere')

# User-defined Exceptions
# Class derived from the Exception class

# Assert

#-----------------------------------------------
# Using module

# Import modules in search path
#import module1[, module2[,... moduleN]
# import specific attributes from a module
#from modname import name1[, name2[, ... nameN]]

# A search path is a list of directories that the interpreter searches before importing a module. 


#-----------------------------------------------
# Creating module

#https://thomas-cokelaer.info/tutorials/python/packaging.html

#-----------------------------------------------
print('-----------------------------------------------')
print('Iterator')

# Iterator behavior can be added to classes. Define  __iter__() and __next__() methods.

print('Generator')
# Generators: tool for creating iterators. Written like regular functions but use yield statement whenever they want to return data. 
# Each time next() is called on it, the generator resumes where it left off
# Local variables and execution state are automatically saved between calls
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
     print(char)


# Decorators

# Unpacking (*var)
print("Unpacking")
my_args = [1, 6, 2]

# call with arguments unpacked from a list
print(list(range(*my_args)))

# Function Annotations
print("Function Annotations")

# optional metadata information about the types used by user-defined functions
def my_annot_func(arg1: str, arg2: str = 'def value') -> str:
    return arg1 + ' and ' + arg2

result = my_annot_func('value1', 'value2')
print(result)

#-----------------------------------------------
# Map filter reduce
print('-----------------------------------------------')
print("map filter reduce:")
# 

# import reduce (filter and map are built-in)
from functools import reduce

def map_filter_reduce():

    #-----------------------------------------------
    # base list
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\nmy_list:")
    print(my_list)

    # filter with lambda function
    # filter base on criterion (lambda function) and generate 
    # new filter object and list
    filtered_list = list(filter(lambda x: x > 5, my_list))
    print("filtered_list:")
    print(filtered_list)

    # map with lambda function
    # apply function to all items and generate a new map object and list
    mapped_list = list(map(lambda x: x*2, filtered_list))
    print("mapped_list:")
    print(mapped_list)

    # reduce with lambda function
    # apply function to all items cumulatively from left to right
    # and reduce sequence to a single value
    reduced_list = reduce(lambda x,y: x + y, mapped_list)
    print("reduced_list:")
    print(reduced_list)

    #-----------------------------------------------

# Call function
map_filter_reduce()

#---------------------------------------------------
# Standard Library

# Built in functions
# https://docs.python.org/3/library/functions.html


# Python collections module:
# - namedtuple(): factory function for creating tuple subclasses with named fields
# - deque: list-like container with fast appends and pops on either end
# - ChainMap: dict-like class for creating a single view of multiple mappings
# - Counter: dict subclass for counting hashable objects
# - OrderedDict: dict subclass that remembers the order entries were added
# - defaultdict: dict subclass that calls a factory function to supply missing values

# Others...


# heapq: heap queue

# numbers, decimal, fractions