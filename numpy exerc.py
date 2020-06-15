

# Import numpy
import numpy as np

#declare normal list
height=[1,2]
# Create a Numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
print(type(np_height_m))   #numpy.ndarray = 1D array




# height and weight are available as a regular lists
height=[1.2, 22.3]
weight=[2.0, 22.1]

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light=np.array(bmi<21)

# Print out BMIs of all baseball players whose BMI is below 21
#print (light[bmi])   #ma non funziona mi sa che va solo nel python 3 questo è il 2.7

import numpy
a="a"
b="b"
x=numpy.nansum([1, a, 2, b])
print(x)







