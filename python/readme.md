# Python Examples

Base Python 3.6

## Language


Scripting language. Interpreted. Converted to Python bytecode before execution. 
Bytecode is a set of instructions for a virtual machine (Python interpreter).

Supports interactive mode.

Supports functional and structured programming methods as well as OOP.

Types:
- dynamically typed language: variable name is bound only to an object not a type (unless it is null).
- strongly typed language: explicit conversion is required (eg. from int to string).
- supports dynamic type checking.

Supports automatic garbage collection.

Comment: '#' or ''' for multiline 

Case sensitive. Identifier restrictions and reserved words (eg. cannot start with a number or use 'def').

Blocks of code:
- Blocks of code are denoted by line indentation.
- A group of statements in a single code block are called 'suites'. 
- Compound or complex statements, such as if, while, def, and class require a header line and a suite.
- Header lines begin the statement and terminate with a colon ( : ), followed by suite.
```
if condition:
    statement1
    statement1
    ....
```

Semicolon ( ; ) allows multiple statements on the single line


Versions: python 2.X legacy; python 3.6, 3.7 more recent. Keep version in mind.

## Naming conventions

Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
Starting with a single leading underscore (eg. _ident) is a protected  identifier.
Starting with two leading underscores (eg. __ident) indicates a strongly private identifier.
If the identifier also ends with two trailing underscores (eg. ident__), the identifier is a language-defined special name.

## Coding Style

PEP 8 style guide (Python Enhancement Proposal)
- Use 4-space indentation, and no tabs.
- Wrap lines so that they don’t exceed 79 characters.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.
- When possible, put comments on a line of their own.
- Use docstrings.
- Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
- Convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. 
- Always use self as the name for the first method argument.


## Modes

Modes
- Interactive Mode Programming
- Script Mode Programming


## Install Python

Python 3

Install python3
- Linux Yum based
```
$ sudo yum -y install python3
```
- Apt get based:
```
$ sudo apt -y install python3
```

## Running interactive mode

```
$ python
```

Enter instructions
```
print("hello")
```

## Running a script calling python

Run
```
python file.py
```

## Running a shell script

As shell script. Include first line of file
```
#!/usr/bin/env python
```

Change permission
```
chmod +x file.py
```

And run
```
./file.py
```

Use Ctl-D to stop execution

If more than one Python version installed, use 'python3' command


## Examples

Common Examples in examples.py

Run
```
python examples.py
```

## Run inside Virtual Environment

Install pip (package-management system)
```
$ sudo python3 -m easy_install pip
```

Install virtualenv
```
$ sudo pip install virtualenv
```

Run in virtualenv
```
$ virtualenv venv
$ source venv/bin/activate
$ python3 examples.py
```

To Leave virtualenv: 
```
$ deactivate
```

virtualenv: virtual environment (separates resources from current operating system).


## Refs

Operators
- https://www.tutorialspoint.com/python/python_basic_operators.htm

Built-in types
- https://docs.python.org/3/library/stdtypes.html

Expressions
- https://docs.python.org/3/reference/expressions.html


- https://docs.python.org/3/tutorial
- https://thomas-cokelaer.info/tutorials/python/
- https://www.tutorialspoint.com/python/
- https://www.datacamp.com/community/tutorials/functions-python-tutorial
- http://book.pythontips.com/en/latest/
- https://github.com/scikit-learn/scikit-learn/tree/master/sklearn
- https://github.com/pandas-dev/pandas/tree/master/pandas
- https://www.w3resource.com/python-exercises/

- https://runestone.academy/runestone/books/published/pythonds/index.html