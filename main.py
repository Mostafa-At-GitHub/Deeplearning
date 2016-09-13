# Question
# Wrangle
# Explore
# Drawing conclusions phase
#     predict: which movies users will like
#     conclude:
# Communication Phase
#     Blog, post
import numpy as np

np.array([])
#More vectorized operations
#mathe Operations add+, subtract-, multiply*, divide/, exponetiate**
#Logical operatons and&, or| negation~
a = np.arange(1, 5)
b = np.array([1,2,1,2])
print a
print (a**b)
print a > b
print a < b
def standardize_data(values):
    return (values - values.mean())/values.std()
c = a
a+= np.ones(4, dtype =np.int)
print c
# plus equal operates in-place while plus makes a different instance
a = np.arange(1,5)
d = a
a = a+np.ones(len(a), dtype=np.int)
print d