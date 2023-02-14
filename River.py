# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import numpy as np
from Creatures import Bear
from Creatures import Fish

class River:
    
    def __init__(self, n_room):
       self._n_room = length
       self._contents = []
        
       
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.eco, "\n")
        print("===================")
        
        
        
        
        


class River:
    """A river is in array containing animals"""

    def __init__(self, length):
        """Initialize a river with a random assortment of bears, fish, and empty cells

        length     length of the river
        """

        self._length = length
        self._contents = []
        for i in range(self._length):
            rval = random.randint(1,3)
            if rval == 1:
                self._contents.append(Bear())
            elif rval == 2:
                self._contents.append(Fish())
            else:
                self._contents.append(None)

    def __len__(self):
        """Return the length of the river"""
        return self._length

    def __getitem__(self, k):
        """Return the contents of the kth cell in the river list"""
        return self._contents[k]

    def __setitem__(self, k, val):
        """Set the contents of the kth cell in the river list"""
        self._contents[k] = val

    def count_none(self):
        """Count the number of empty cells in the river list"""
        return self._contents.count(None)

    def add_random(self, animal):
        """Add animal to empty cell of river list after mating occurs"""
        if self.count_none() > 0:
            choices = [i for i, x in enumerate(self._contents) if x==None]
            index = random.choice(choices)
            self._contents[index] = animal

    def update_cell(self, i):
        """Update the cell based on rules defined above"""
        if self._contents[i] != None:
            move = random.randint(-1,1) #animal can either move forward, back, or stay in place
            if move != 0 and 0 <= i + move < self._length:
                if self._contents[i + move] == None:
                    self._contents[i + move] = self._contents[i]
                    self._contents[i] = None
                elif type(self._contents[i]) == type(self._contents[i+move]):
                    if self._contents[i].get_gender() != self._contents[i+move].get_gender():
                        #two animals of the same type and different gender mate
                        if type(self._contents[i]) == Bear:
                            self.add_random(Bear())
                        else:
                            self.add_random(Fish())
                    else: #two animals of the same type and gender fight
                        if self._contents[i].get_stren() > self._contents[i+move].get_stren():
                            self._contents[i+move] = self._contents[i]
                        self._contents[i] = None

                else:
                    #bear always kills fish if they encounter eachother
                    if type(self._contents[i]) == Bear: 
                        self._contents[i + move] = self._contents[i]
                    self._contents[i] = None

    def update_river(self):
        """Update each cell in the river"""
        for i in range(len(self._contents)):
            self.update_cell(i)

    def print_river(self):
        """Print the river contents in human readable form
           Each cell displays the animal type, strength, and gender between two pipes

           Example: male bear with strength 8    |B8M|
                    female fish with strength 0  |F0F|
        """
        s = '|'
        for x in self._contents:
            if x:
                if type(x) == Bear:
                    s += 'B'
                elif type(x) == Fish:
                    s += 'F'
                s += str(x.get_stren())
                s += x.get_gender()
            else:
                s += '   '
            s += '|'
        print(s)







river = [None] * 20
for i in range(4):
    river[i] = Bear(i)
for i in range(16, 20):
    river[i] = Fish(i)