""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_fast(mass, density): 
    total = 0.0 
    masslog = log(mass * density)
    for i in range(1,10001):  
        total += masslog/i

    return total

mass = 2.5 
density = 12.0 

timer_s = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density") 
print("time(orig):", timer_s.timeit(number=1000)) 
timer_f = Timer("total = groffle_fast(mass, density)", 
 "from __main__ import groffle_fast, mass, density") 
print("time(fast):", timer_f.timeit(number=1000))

if groffle_slow(mass, density) != groffle_fast(mass, density):
    print("groffle_slow & groffle_fast are NOT identical")
else:
    print("groffle_slow & groffle_fast ARE identical")
