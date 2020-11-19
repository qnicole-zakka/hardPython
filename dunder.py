# Learn the functions of different underscores
# https://dbader.org/blog/meaning-of-underscores-in-python
# 5 types: bare, combinations of leading/trailing and single/double
############################### 
# 1. bare underscore 
############################### 

############################### 
# 2. single leading
############################### 
## internal use
## only can be functional recognize when in the following case 1
# case 1:
# This is the my_mod.py
def _int_func():
    print('internal')
def ext_func():
    print('external')
# import method 1: _ not enforced by the Python interpreter
import my_mod
my_mod._int_func() 
my_mod.ext_func()

# import method 2: enforced
# but * does not match coding convention, should use method 1 or explicit class/function names
from my_mod import *
_int_func() # error
ext_func() 
 
 
############################### 
# 3. double leading
############################### 

############################### 
# 4. single trailing
############################### 
## to avoid clashing with reserved keywords
def init_class(t, class_):  
    print('making class')
############################### 
# 5. double trailing
############################### 
