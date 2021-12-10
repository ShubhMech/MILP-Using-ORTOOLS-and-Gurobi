# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:57:35 2021

@author: Asus
"""

import ortools.linear_solver.pywraplp as pyo
solver=pyo.Solver.CreateSolver('GLOP')
x=solver.IntVar(0,3,'x')
y=solver.NumVar(0,float('inf'),'y')

solver.Add(x+y<=8)
solver.Add(8*x+3*y>=-24)
solver.Add(-6*x+8*y<=48)
solver.Add(3*x+5*y<=15)

solver.Minimize(-4*x-2*y)
result= solver.Solve()
x=x.solution_value()
y.solution_value()