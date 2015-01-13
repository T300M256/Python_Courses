#!/usr/local/bin/python3
"""Produce a listing of people's names, ages and weights."""
data = [
        ("Steve", 9, 202),
        ("Dorthy", 49, 156),
        ("Simon", 39, 155),
        ("David", 61, 135)]
for name, age, weight in data:
    print("{0:.<30s} {1:4d} {2:4d}".format(name, age, weight))