# Key words

# and --> logical and
# as --> import keras as kr
# assert --> assert (a condition), a message if failed

x = 'hello'
assert x== 'hello', 'x should be bye'

# break --> exit from the current loop. if nested loops, exits only from the immediate loop
# class --> defines a class.  class Person(Object)
# continue --> to the next iteration of a loop
# def --> defines a functiion
# del --> delete from a dictionary
# elif -->
# else -->
# except --> try,except
# exec --> Run a string as python code

code = "print('Hello World')"
exec(code)

# finally --> exception or not, do after all try excepts.
# for
# from --> from sys import ...
# global
x = "Im Global"

def fun1():
    global x
    x = "I can change in fun()"
    print(x)

fun1()
print(x)

# if
# import
# in: for x in list || for c in string
# is --> 1 is 1 == True
# lambda -->

s = lambda x: x**x
print(s(3))

# not
# or
# pass
# print
# raise --> raise ValueError('No')
# return
# try
# while
# with --> with open('filePath/fileName', 'w') as file: pass
# yield --> pause in fun() and return to caller, then return to fun() until an exit condition

###
# Data Types
# True
# False
# None
# bytes
x = b"hello"
print(x)

# strings
# numbers
# floats
# lists
# dicts

###
# Excape sequence
# \\ backslash
# \' single quote
# \" double quote
# \a bell
# \b backspace
# \f formfeed
# \n newline
# \r carriage return
# \t tab
# \v vertical tab

print('hi');
print('there')