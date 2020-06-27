# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:44:57 2019

@author: Shri
"""
from constraint import *
problem = Problem()
problem.addVariable("a", [1,2,3])
problem.addVariable("b", [4,5,6])
problem.getSolutions()
[{'a': 3, 'b': 6}, {'a': 3, 'b': 5}, {'a': 3, 'b': 4},
 {'a': 2, 'b': 6}, {'a': 2, 'b': 5}, {'a': 2, 'b': 4},
 {'a': 1, 'b': 6}, {'a': 1, 'b': 5}, {'a': 1, 'b': 4}]

problem.addConstraint(lambda a, b: a*2 == b,
                          ("a", "b"))
problem.getSolutions()
[{'a': 3, 'b': 6}, {'a': 2, 'b': 4}]

problem = Problem()
problem.addVariables(["a", "b"], [1, 2, 3])
problem.addConstraint(AllDifferentConstraint())
problem.getSolutions()
[{'a': 3, 'b': 2}, {'a': 3, 'b': 1}, {'a': 2, 'b': 3},
 {'a': 2, 'b': 1}, {'a': 1, 'b': 2}, {'a': 1, 'b': 3}]