from timeit import timeit
#from random import random

print("starting")
print("list() applied to generator:",timeit("list(random() for j in range(1000000))", "from random import random",number=1)) # generator expression
print("list comprehension:         ",timeit("[random() for j in range(1000000)]", "from random import random", number=1)) # creates list
print("finished")