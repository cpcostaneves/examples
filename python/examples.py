
#-----------------------------------------------
# Start script

#-----------------------------------------------
# Output
print('-----------------------------------------------')

# Print hello
print('Hello Python')

# Change line ending
print('new line - ', end='')
print('no line breaking')

#-----------------------------------------------
# Comments

# A comment

print('Comment') # This is again comment

'''
This is a multiline
comment.
'''

#-----------------------------------------------
# Quotes

# Python accepts single ('), double (")
str_word = 'word'
str_sentence = "This is a sentence."

# Triple (''' or """) quotes used to span across multiple lines
str_paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

#-----------------------------------------------
# Multi-Line Statements
print('----------------------------------------------')
print('Multi-Line Statements')

# Statements typically end with a new line. Line continuation character = backslash (\) denote that the line should continue.
total = 1 + \
        2 + \
        3

# Statements contained within the [], {}, or () brackets do not need to use the line continuation character.
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


#-----------------------------------------------
# Basic Variable types
print('-----------------------------------------------')
print('Basic variable types')

# main built-in types are numerics, sequences, mappings, classes, instances and exceptions.

#-----------------------------
# Assignment
# type is defined according to value
# Numeric
this_is_int = 8
this_is_float = 15.4
this_is_complex = 3e-4 + 1j

# String
this_is_string = 'A string'

#-----------------------------
# dynamically typed language: variable name is bound only to an object not a type
var1 = 5
var1 = 'Now a string'

var2 = 15

# strongly typed language: explicit conversion is required
new_str = var1 + str(var2)
print(new_str)


#-----------------------------
# Multiple Assignment
# Single value to several variables
a = b = c = 1
# Assign multiple objects to multiple variables
a, b, c = 1,2,"john"

# change order
a, b = b, a

#-----------------------------------------------
# Numeric Types - math operations

# built in
print(abs(-8.2))

# math Standard Library module (+ others like cmath)
import math
print(math.ceil(4.7))

#-----------------------------------------------
# Strings
print('-----------------------------------------------')
print('Strings')

# - string: sequence of characters, immutable, defined with "" or '' or """ for multiline 

# Slicing
my_string = 'Hello Python'
print(my_string)
print(my_string[0])
print(my_string[2:5])
print(my_string[2:])
print(my_string[5:-2])

# string is immutable and does not support item assignment, eg: my_string[1] = 35

# length
print(len(my_string))

# Repeat
print (my_string * 2)

# Concat
my_new_string = my_string + ' more text'
print(my_new_string)


# Iterate
for char in my_string:
    print(char, end=' , ')
print(end='\n')

# Escaping chars, eg: \n , \\, \"
my_string_escap = 'text with escape chars: \" , \\ \n'
my_string_squot = "text with 'single quotes' "
my_string_dquot = 'text with "double quotes" '
print(my_string_escap)
print(my_string_squot)
print(my_string_dquot)

# formating
my_format = 'This is the first: {}, and this is the secoond: {}'.format(34, 'other string')
print(my_format)

my_format_ordered = 'This is the second: {1}, and this is the first: {0}'.format(34, 'other string')
print(my_format_ordered)

# formatter operations available (eg. pad, align)
# ref: https://pyformat.info/


# string methods, eg: find, strip, upper
print(my_string.find('Py'))

#-----------------------------------------------
# Collections : containers used to store collections of data
print('----------------------------------------------')
print('Collections')

# Built-in:
# - list, sequence, mutable, usually homogeneous, defined with square brackets []
# - tuple: sequence, immutable, faster than list, usually heterogeneous, defined with parenthesis ()
# - set: sequence, unique elements, defined with  set() function or curly braces {}
# - string: sequence of characters, immutable, defined with "" or '' or """ for multiline 
# - dict (dictionary): mapping, maps key = value, defined with curly brackets and key value pair {'key': value}

# Can hold any data type (not only numeric or strings)
# Access element with: [index]

#-----------------------------
# List
print('List')
my_list = [20, 21, 22, 23]
print(my_list[1])
my_list[1] = 60
print(my_list[1])

# Cannot create position using [] (only using methods, eg. append)
#my_list[10] = 70

#-----------------------------
# Tuple
print('Tuple')
my_tuple = (10, 15, 20, 'dog')
# tuple is immutable and does not support item assignment, eg: my_tuple[1] = 35
print(my_tuple[1])
print(my_tuple[3])

#-----------------------------
# Set
print('Set')
nonunique_list = [20, 21, 22, 21, 20]
unique_list = set(nonunique_list)
print(unique_list)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

#-----------------------------
# Dict
# not ordered, duplicated keys not allowed (last one rules
# # keys must be of immutable type (number, string, tuple, but not list)
print('Dict')
my_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
print(my_dict['key2'])
my_dict['key2'] = 'val4'
print(my_dict['key2'])

# Can create new key, value using []
my_dict['key10'] = 'val5'

# Create using dict
my_dict_defined = dict([('key1','val1'),('key2','val2')]) 
print(my_dict_defined)

#-----------------------------
# iterable interface: An object capable of returning its members one at a time (iter() returns an iterator object).
# iterable has 3 descendants: sequence, mapping, generator
# - sequence: iterable with random access. supports slicing (eg list, tuple, set)
# - mapping: elements accessed via keys instead of integers (eg. dict)
# - generator: no random access, consume items in order. Only create items when iterate over them.
#              A function that uses yield returns a generator.

#-----------------------------
# Sequence operations (for list, tuple, set)

print('Sequence operations')
my_list = [19, 20, 21, 'apple', 23]

# Access element
print(my_list[1])

# Assign if mutable
my_list[1] = 60
print(my_list)

# Delete element if mutable
del my_list[4]
print(my_list)

# slice (:)
# slicing: create a slice (sequence subset) with start, stop, step
print (my_list[2:])

# concat (+)
print(my_list + my_list)

# repeat (*)
print(my_list * 2)

# length
print(len(my_list))

# members
print(21 in my_list)

# min, max (only for numeric only sequence) (uses Comparison Operators)
num_list = [19, 20, 21, 23]
print(max(num_list))

#-----------------------------
# Nested sequences and matrix

print('Nested sequences and matrix')

# Nested sequences
nested_list = [19, 20, 21, [30, 31, 32]]
print(nested_list[3][1])

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][2])

#-----------------------------
# Lists and strings

print('Lists and strings')

my_text = 'this is a string'

# Split string to a list (default separator is blank space)
my_text_split_list = my_text.split()
print(my_text_split_list)

# Join list to string using separator
my_text_joined = '_'.join(my_text_split_list)
print(my_text_joined)

#-----------------------------
# Mapping operations (for dict)

print('Mapping operations')

my_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

# Delete element
del my_dict['key2']
print(my_dict)

# length
print(len(my_dict))

# get lists
print(list(my_dict.keys()))
print(list(my_dict.values()))


#-----------------------------
# Sequence and mappings methods

print('Sequence and mappings methods')

# Sequence and mappings (list, tuple, set, dict) are classes with data handling methods

list_met = [1, 2, 4, 2, 4]
list_met.append(3)
print(list_met)

print(list_met.count(4))
print(list_met.index(3))

list_met.insert(3, 5)
print(list_met)

#-----------------------------
# Built-in collections have Functions to handle data

# Python collections module:
# - namedtuple(): factory function for creating tuple subclasses with named fields
# - deque: list-like container with fast appends and pops on either end
# - ChainMap: dict-like class for creating a single view of multiple mappings
# - Counter: dict subclass for counting hashable objects
# - OrderedDict: dict subclass that remembers the order entries were added
# - defaultdict: dict subclass that calls a factory function to supply missing values

#-----------------------------------------------
# Variable type
print('----------------------------------------------')
print('Variable type')
print(type(75))

# Data type convertion (eg. float(), list())
print('This is: ' + str(45))
print(int('75'))

#-----------------------------------------------
# Objects and references
print('----------------------------------------------')
print('Objects and references')

new_list = [19, 20, 21, 23]
# Python works with object reference by default
# Assigning just reference not copy to a new object
ref_list = new_list
print(new_list)
ref_list[1] = 80
print(new_list)

print('IDs')
print(id(new_list))
print(id(ref_list))
print(new_list is ref_list)


# Cloning
other_list = new_list[:]
print(new_list)
other_list[1] = 90
print(new_list)

print('IDs')
print(id(new_list))
print(id(other_list))
print(new_list is other_list)


#-----------------------------
# Delete a variable reference
temp_var = 5
del temp_var


#-----------------------------
# Booleans values: True, False

#-----------------------------
# Operators
#- Arithmetic Operators (returns numeric value): +, -, *, /, ...
#- Comparison (Relational) Operators (returns boolean value): == , != , >= , <, ...
#- Assignment Operators: var = value , var += increment, -=, /=,  ...
#- Logical Operators (returns boolean value):  and, or, e no
#- Bitwise Operators (bit operations): & , |, ^, ...
#- Membership Operators (element is member?): in , not in
#- Identity Operators (same object?): is, is not

# Note: take care of Precedence and Associativity of Operators 
# Note: Change default behavior: Class methods, eg. __bool__() ; __len__()  ; __eq__()


#-----------------------------
# None statement

# Null equivalent: None

#-----------------------------------------------
# Pass statement

# pass
# does nothing, used when a statement is required syntactically but the program requires no action
if 1:
    pass

#-----------------------------------------------
# Conditions
print('----------------------------------------------')
print('Conditions')

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

# Single line
if ( True ) : print ("Single line")


#-----------------------------------------------
# Loops
print('-----------------------------------------------')
print('Loops')


# while
# while expression: 
#   statements(s)

count = 0
while (count < 9):
    count = count + 1

# for loop works with iterator objects (with function set to start/stop loop and get next objects).

# range: generate a sequence of integer numbers (range object)
# range (stop)
# range (start, stop[, step])
# exclusive (stop not included)

# for
# for iterating_var in sequence:
#   statements(s) 

for i in range(1, 6, 2):
    print(i)

loop_list = [1,2,3,4,5]
for i in range(len(loop_list)):
    print(i, end=', ')
print(end='\n')

# sequence loop (list, tuple, set)
for element in loop_list:
    print(element, end=' , ')
print(end='\n')

# mapping loop (dict)
my_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
for k, v in my_dict.items():
    print(k, ' = ', v)


# Behind the scenes, the for statement calls iter() on the container object. The iter() returns an iterator object 
# that defines the method __next__() which accesses elements in the container one at a time.
# When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. 




# Iterator behavior can be added to classes. Define  __iter__() and __next__() methods.
# Generator (Function with 'yield' statement) creates an interator.

# Python supports break and continue statements
# Python supports 'else' statement after for and while (executed when loop has ended)



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
# Objects passed as arguments are referenced not copied
def my_function_pass_ref(param):
    param[2] = 70

my_list_func = [1, 2, 3, 4]
print(my_list_func)
my_function_pass_ref(my_list_func)
print(my_list_func)

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

#-----------------------------
# Global vs Local Variables. Force local ('local')

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

#-----------------------------------------------
# File IO

def open_file():
    try:
        # open file stream # conteúdo do bloco try
        file = open('', "r")
    except IOError: # conteúdo do bloco except
        print ("There was an error writing to", file_name)



#-----------------------------------------------
# Creating module

#https://thomas-cokelaer.info/tutorials/python/packaging.html

#-----------------------------------------------
# Datetime


#---------------------------------------------------
# C Interface

#---------------------------------------------------
# Concurrent Execution, Multi-threading


#---------------------------------------------------
# Debugging and Profiling


#-----------------------------------------------
# Functions/Iterators - extra topics
print('-----------------------------------------------')
print('Extra')

# Generator
print('Generator')

# Generators: tool for creating iterators. Written like regular functions but use yield statement whenever they want to return data. 
# 'yield' returns value (to for loop)
# for loop calls next() resuming last 'yield' where it left off. Local variables and execution state are automatically saved between calls

# A simple generator function
def my_gen():
    print('This is printed first')
    # Generator function contains yield statements
    yield 1

    print('This is printed second')
    yield 2

# Using for loop
for item in my_gen():
    print(item)


# Decorators
# decorators wrap a function, modifying its behavior. Receives a function, changes it, returns a function
# Syntactic Sugar: @decorator -> my_function = decorator(my_function). 

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

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



#---------------------------------------------------
# Standard Library

# Refs
# https://docs.python.org/3/tutorial/stdlib.html
# https://docs.python.org/3/library/index.html


# Operating System Interface
# File handling
# I/O
# Mathematics
# Internationalization
# Internet Protocols, Data Handling
# Multi-threading
# Logging
# ...
