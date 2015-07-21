import re as RE
import inspect
from pprint import pprint

functions = inspect.getmembers(RE, inspect.isfunction)

for f in functions:
    print("def %s%s" % (f[0], inspect.formatargspec(*inspect.getfullargspec(getattr(RE, f[0])))))
    
