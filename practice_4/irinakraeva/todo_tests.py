'''
Created on Mar 17, 2014

@author: Java Student
'''
from examples_4 import todo
from IrinaKraeva.autotest import *

def emty_test():
    todo.clear()
    result=todo.items()
    assert_equal(result, tuple())
    
