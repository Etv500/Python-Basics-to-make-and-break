# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:59:11 2017

@author: elvis
"""
import numpy
a = numpy.array([[10, 2], [3, 4], [5, 6]])
xmax = numpy.max(a[0:-1,0])
ymax = numpy.max(a[0:-1,1])
print(xmax, ymax)