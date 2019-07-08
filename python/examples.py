
#-----------------------------------------------
# Start script

# print hello
print('-----------------------------------------------')
print('Hello Python')

#-----------------------------------------------
print('-----------------------------------------------')
# functions

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

    print('\nMy Function')

    # Do some operation
    result = param * 5

    # return from function
    # End  function with a return statement if the function should output something. 
    # Without the return statement, your function will return an object 'None'.
    return result

# Call the function
my_function(5)

#------------------------------------
# Argument types
def my_function_args(req_arg, def_arg1 = 5, def_arg2 = 15, *args, **kwargs):

    # Argument types:
    # - Required positional arguments: have to be passed in the right order
    # - Default arguments: default value if no argument value is passed
    # - Keyword arguments: identify the arguments by their parameter name (have to the last arguments to pass)
    # - Non-keyworded variable length argument list: *args by convention
    # - keyworded variable length argument list: **kwargs by convention

    print('\nArgument types')

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

    print('\nFunction Doc')

#------------------------------------
# Anonymous / lambda functions
# 
testnumber = 5
doublenumber = lambda x: x*2

print('\nLambda function:')
print(doublenumber(100))

#-----------------------------------------------
print('-----------------------------------------------')
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

# Use extended class
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
# Basic

# dynamically typed language
var1 = 5
var1 = 'Now a string '
var2 = 10

# strongly typed language
new_str = var1 + str(var2)
print(new_str)

# Primitives
# None, True, False,pass


# String formating
# {0}.{1}.format

# output
# print(str, end='')

# Global vs Local Variables. Force local ('local')


# get variable type

# Attributions (Multiples)

#-----------------------------------------------
# data structs

# list, tuple, dictionary

# collections

#-----------------------------------------------
# Error handling

#-----------------------------------------------
# Decorators

#-----------------------------------------------
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

