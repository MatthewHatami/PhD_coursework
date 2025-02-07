import numpy as np
import pandas as pd

# Exercice 1

# Method 0: we can fill an np.array with the values manually as below:
realNumberArray1 = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
print("realNumberArray1 built manually: ", realNumberArray1)

# Method 1: we can use the np.arange() function to generate the array
realNumberArray2 = np.arange(0.0, 10.0, 1.0)
print("realNumberArray1 built with arange method: ", realNumberArray2)

# Method 2: we can use the np.linspace() function to generate the array
realNumberArray3 = np.linspace(0.0, 9.0, 10)
print("realNumberArray2: ", realNumberArray3)

# Method 3: we can use the np.random.rand() function to generate the array
realNumberArray4 = np.random.rand(10)
print("realNumberArray3: ", realNumberArray4)

"""


similarities: in all methods mentioned above, or even the methods that I haven't mentioned, 
we can generate an array of numbers and after assigning the array to a variable, 
they won't be different from eachother. we can treat all of them similarly, 
no matter which method we used to generate those.

differences: 
the differences between the methods are the additional features that each method has, and each of them can become handy in different situations.
for example, when we have the first and last value and we need to have values evenly spaced between them, we can use np.linspace() or np.arange method.
the difference between these two method is that in np.arange() we can specify the step size, but in np.linspace() we can specify the number of values we want to have between the first and last value.

the last method, np.random.rand() is used to generate random numbers between 0 and 1.


"""
