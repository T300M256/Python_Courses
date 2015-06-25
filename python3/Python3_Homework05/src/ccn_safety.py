"""
ccn_safety.py: anonymizes credit card numbers in strings
"""

import re

regex = r"(\d\d\d\d-\d\d\d\d-\d\d\d\d)(-\d\d\d\d)"

def clean_ccn(text):
    return re.sub(regex, r"XXXX-XXXX-XXXX\2",text)