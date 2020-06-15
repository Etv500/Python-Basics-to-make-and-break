# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:42:39 2017

@author: elvis
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area= areas[3]+areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)





x = ["a", "b", "b"]
x[2] = "c"    #sostituisce il terzo valore della list
x = x + ["d"]     #aggiunge un quarto valore alla list
print(x)   


del(x[2])    #cancella un elemento della list , occhio che poi il quarto diventa terzo così
print(x)  
