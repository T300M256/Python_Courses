#!/usr/local/bin/python3
"""this program tests more use of functions"""

import sys

def capitalize(text):
    return text.capitalize()

def title(text):
    return text.title()

def upper(text):
    return text.upper()
    
def lower(text):
    return text.lower()

def exit(text):
    print("Goodbye!")
    sys.exit()

if __name__ == "__main__":

    sw = {
        'title':title,
        'capitalize':capitalize,
        'upper':upper,
        'lower':lower,
        'exit':exit,
    }
    prompt = "Enter a function name (" + ", ".join(sw.keys()) + "): "
    while True:
        inp = input(prompt)
        option = sw.get(inp, None)
        if option:
            text = input("Enter a string: ")
            print(option(text))
        else:
            print("Unrecognized function name!")
        