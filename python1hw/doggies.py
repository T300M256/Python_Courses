#!/usr/local/bin/python3
"""this is the source file for the Dog class"""

class Dog:
    """this is the Dog class"""
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
if __name__ == "__main__":
    dogs = []
    while True:
        n = input("Name: ")
        if not n:
            break
        b = input("Breed: ")
        dogs.append(Dog(n,b))
        print("DOGS")
        i = 0
        for d in dogs:
            print("{0}. {1}:{2}".format(i,d.name,d.breed))
            i += 1
        print("*" * 40)
        
            
