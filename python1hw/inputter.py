#!/usr/local/bin/python3
"""this tests reading and writing from files"""

filename = "persist_input.txt"

"""if the persisted file does not exist yet create it"""
p = open(filename, 'a')
p.close()

while True:
    """read the persisted file and display any content"""
    r = open(filename, 'r')
    content = r.read()
    if content:
        print(content)
    r.close()
    """get new input from user"""
    w =  open(filename, 'a')
    text = input("Enter text: ")
    if not text:
        w.close()
        break
    w.write(text)
    w.close()