# -*- coding: utf-8 -*-
"""
Created on Created on 16.02.2023

@author: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt 
"""
import numpy as np
import random 
from Creatures import Animal, Bear
from Creatures import Fish

class River:
    def __init__(self, length, num_bears, num_fish):
        self.length = length
        self.river = [None] * length
        self.num_bears = num_bears
        self.num_fish = num_fish
        self.valid_size_ecosystem(self.length, self.num_bears, self.num_fish) # instant call to check if parameters are valid 
        self.populate_river()  

    def valid_size_ecosystem(self, length, num_bears, num_fish):
        if length < (num_bears + num_fish):
            raise ValueError("Joint number of bears and fish exceeds the length of the river")
        return length

    def populate_river(self):
        """
        Initialize river with a given number of bears and fish at random positions.
        """
        for i in range(self.num_fish):
            # find a random empty location in the river and place a fish there
            empty_idx = random.choice([j for j in range(self.length) if self.river[j] is None])
            self.river[empty_idx] = Fish()
        for i in range(self.num_bears):
            # find a random empty location in the river and place a bear there
            empty_idx = random.choice([j for j in range(self.length) if self.river[j] is None])
            self.river[empty_idx]=Bear()


    def display(self):
        """
        Display the current state of the river.
        """
        print("=============")
        for idx in self.river:
            if idx is None:
                print("_", end="\n")
            else:
                print(idx.species, end="\n")
        print("=============")
    
    def move(self, idx, animal):
        """
        Move animal to a new index based on its specified direction and distance.
        """
        if animal.has_moved != 1:
            animal.has_moved = 1
            new_idx = animal.move(idx)

            if new_idx < 0 or new_idx >= self.length:
                return

            if self.river[new_idx] is None:
                self.river[new_idx] = animal
                self.river[idx] = None
            elif self.river[new_idx].species == animal.species and animal.direction !=0:
                self.river[new_idx] = self.reproduce(animal, new_idx)

            elif (isinstance(animal, Fish) and isinstance(self.river[new_idx], Bear)):   # or statement vice versa
                    self.river[idx] = None  # Fish gets eaten by bear and disappears
            elif (isinstance(animal, Bear) and isinstance(self.river[new_idx], Fish)):
                self.river[new_idx] = animal #Bear eats fish and takes its place
                self.river[idx] = None
            else:
                pass  # Other Animals of different species do not exist but could be added


    def reproduce(self, animal, idx):
        """
        Create new animals of the same species at random empty locations based on 
        animal's specified offspring number.
        """
        empty_indices = [i for i in range(self.length) if self.river[i] is None]
        num_offspring = animal.offspring # why do you need this? Can it not just spawn on random empty index?
        #check which is the 
        for i in range(min(num_offspring, len(empty_indices))):
            new_idx = random.choice(empty_indices)
            empty_indices.remove(new_idx)
            self.river[new_idx] = type(animal)(has_moved=1) # newly spawned animals can't move 
            
        return type(animal)()

    
    def next_timestep(self,num_rounds):
        """
        Simulate the next timestep of the river by moving and reproducing the animals.
        """
        random_order = list(range(self.length))
        #the animals take turn iteratively but in random order 
        random.shuffle(random_order)

        for i in range(num_rounds):
            for idx in random_order:
                if self.river[idx] is None:
                    continue
                else:
                    self.move(idx,self.river[idx])

            for idx in self.river:
                if idx is not None:
                    idx.has_moved = 0
        self.display()
       
  


