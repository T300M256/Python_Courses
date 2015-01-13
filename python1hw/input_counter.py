#!/usr/local/bin/python3
"""this is the input counter to test sets and dicts"""

s = {""}
d = {}

while True:
    words = input("Enter text:").strip().split()
    if len(words) == 0:
        break
    else:
        for word in words:
            bef_len = len(s)
            s.add(word)
            if bef_len < len(s):
                d[word] = bef_len
        for w in d.keys():
            print(w, d[w])
print("Finished")