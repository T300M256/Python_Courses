"""
ccn_safety.py: anonymizes credit card numbers in strings
"""

import re

#regex = r"\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d"
#regex = re.compile(r"\d\d\d\d(-\d\d\d\d){3}")
regex = re.compile(r"""
    \d\d\d\d        # four consecutive digits
    (-\d\d\d\d){3}  # followed by 3 hyphenated occurrences of the same
    """,re.VERBOSE)

def clean_ccn(text):
    return regex.sub(r"CCN REMOVED FOR YOUR SAFETY",text)