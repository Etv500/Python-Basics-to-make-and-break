# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:22:04 2017

@author: elvis
"""

import numpy




################################################importante############
h=numpy.array([[1,1,1,1,1,2],[2,2,2,2,2,3]])

print(max(h))

print("")
print("")
print("")

print (numpy.mean(h)) #mean di tutti gli elementi
print (numpy.mean(h[1:3,5]))  #mean della colonna 5
print (numpy.mean(h[1,:]))  #mean della riga 2
print (numpy.mean(h[:,5]))



print (numpy.std(h))
print (numpy.median(h))
print (numpy.corrcoef(h[:,0,], h[:,1]))
################################################importante############


print("")



height= numpy.round(numpy.random.normal(1.75, 0.20, 30),2)
print(height)
#mi stampa 30 random numbers che hanno:
#mean 1.75, stdev 0.20, number of data samples
#pero occhio perchè li stampa ogni volta diversi li rigenera a ogni esecuzione
