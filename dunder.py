# Learn the functions of different underscores
# https://dbader.org/blog/meaning-of-underscores-in-python
# 5 types: bare, combinations of leading/trailing and single/double


############################### 
# 1. bare underscore 
############################### 
## temporary variable
# convention, no Python interpreter enforcement
for _ in range(10):
    print(_)
# also represent the reesult of the last expression evaluated
for _ in range(10):
    print(_)
# 0 - 9 displayed
# >>> _
# 9


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
## name mangling, interpreter enforcement; the most complicated
# interpreter changes the variable name to avoid collisions in future extensions
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
>>> t = Test()
>>> dir(t)
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'
>>> t2 = ExtendedTest()
>>> t2.foo
'overridden'
>>> t2._bar
'overridden'
>>> t2.__baz
AttributeError: "'ExtendedTest' object has no attribute '__baz'"
>>> dir(t2)
>>> t2._ExtendedTest__baz
'overridden'


############################### 
# 4. single trailing
############################### 
## to avoid clashing with reserved keywords
def init_class(t, class_):  
    print('making class')

    
############################### 
# 5. double leading and trailing
############################### 
## reserved by Python, don't use 
