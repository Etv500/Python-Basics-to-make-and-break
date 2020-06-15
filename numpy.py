# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:52:07 2017

@author: elvis
"""

import numpy

arra1=numpy.array([1,2,3])
print(arra1)

print("plus")

arra2=numpy.array([10,11,12])
print(arra2)

print("equals")

#con gli array numpy, fare la somma significa sommare i termini delgli array in stessa posizione
print(arra1+arra2)
arranump=arra1+arra2



#con gli array normali, fare somma di arrays significa accodare uno all altro
lista = [1,2]
listb=[1,2]
accodato=lista+listb
print(accodato)

#attenzione alle differenze tra i packages e le normali features di python!!!!!!!!!!!!1




#ritorna boolean values rispetto alla condizione
print (arranump>14)


#numpy arrays possono contenere solo un tipo di vars
examplenpar=numpy.array(1, "r", True)
print(examplenpar)
#infatti da errore




