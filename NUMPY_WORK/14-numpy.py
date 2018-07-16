#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 04:32:20 2018

@author: tsachanowski
"""

import numpy as N
import numpy.random       

x = N.array([0, 0.5, 1, 1.5])
print(x)
x = N.array(["ds", 0.5, 1, 1.5])
print(x)

x = N.arange(0, 2, 0.5)
print(x)
x = N.zeros(4)
print(x)

x = N.zeros(4)
x[0] = 3.4
x[2] = 4
print(x)
print(x[0])
print(x[0:-1])

x = N.arange(0, 2, 0.5)
print(x)
print(x + 10)
print(x ** 2)
print(N.sin(x))

x = N.array([[1, 2, 3], [4, 5, 6]])
print(x)

x = N.zeros((5, 4))
print(x)
x=N.array([[1, 2, 3], [4, 5, 6]])
print(x)
print(x.shape)
x=N.array([[1, 2, 3], [4, 5, 6]])
print(x[0, 0]) 
print(x[0,1])
print(x[0,2])
print(x[1,0])
print(x[:,0])
print(x[0,:])

a = N.array([1, 4, 10])
print(list(a))
print(tuple(a))



A = numpy.random.rand(5, 5)    # generates a random 5 by 5 matrix 
x = numpy.random.rand(5)       # generates a 5-element vector
b = N.dot(A, x)                  # multiply matrix A with vector x 
print("##############\n\n",A)
print("##############\n\n",x)
print("##############\n\n",b)
      

x = numpy.linalg.solve(A, b)
print("###############\n",x)
A = numpy.eye(3)     #'eye'->I->1 (ones on the diagonal)
print(A)

evalues, evectors = numpy.linalg.eig(A)
print("3333333\n",evalues,"############33\n",evectors)
      
      
      
import numpy

# demo curve fitting : xdata and ydata are input data
xdata = numpy.array([0.0 , 1.0 , 2.0 , 3.0 , 4.0 , 5.0])
ydata = numpy.array([0.0 , 0.8 , 0.9 , 0.1 , -0.8 , -1.0])
# now do fit for cubic (order = 3) polynomial
z = numpy.polyfit(xdata, ydata, 5) #3 onzacza jakeigo stopnia jest wielomian
# z is an array of coefficients , highest first , i . e .
#                 X^3            X^2          X             0
# z = array ([ 0.08703704 , -0.81349206 , 1.69312169 , -0.03968254])
print(z)# z to moje wspolczynik 
# It is convenient to use ‘poly1d‘ objects for dealing with polynomials:
p = numpy.poly1d(z) # creates a polynomial function p from coefficients
                    # and p can be evaluated for all x then .
# p to moje wielomina ze wspolczynikami z 
print(p)
# create plot
xs = [0.1 * i for i in range (60)]
ys = [p ( x ) for x in xs]   # evaluate p(x) for all x in list xs

import pylab
pylab.plot(xdata, ydata, 'o', label='data') #to drukuje punkty
pylab.plot(xs, ys, label='fitted curve') # to wielomian
pylab.ylabel('y')
pylab.xlabel('x')