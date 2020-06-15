# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:24:43 2017

@author: elvis
"""
#set up and call function
def x ():
    x=100
    print(x)
x()

print("")
#call function in a loop
for k in range(1,4):   #so da 1 a 3 lo fa 3 volte non 4
    x()
    
    

print("")
def z(s,p):   #puoi specificare quanti argomenti vuoi tra parentesi che poi usi
    m=s+p
    print(m)
#call z
z(1,5)



################### Sample Solution ###################
def _magnitude_of_a_vector_sample_(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x**2) + (y**2) + (z**2))**(1/2)
    return mag

    


    
    

    