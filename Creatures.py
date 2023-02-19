# -*- coding: utf-8 -*-
"""
Created on 16.02.2023

@author: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt
"""


from abc import ABCMeta, abstractmethod
import numpy as np
import random

class Animal(metaclass=ABCMeta):
    def __init__(self, species, direction=None, distance=1, offspring=1, has_moved = 0):
        self.species = species
        self.direction = direction
        self.distance = distance
        self.offspring = offspring
        self.has_moved = has_moved
        
    
 #Bear class with the standard attribute movement and offspring set to 1   
class Bear(Animal):
    def __init__(self, direction=None, distance=1,offspring=1,has_moved=0):
        super().__init__("bear", direction , distance, offspring,has_moved)
        
    def move(self, idx): 
        """
        Move bear to adjacent index based on given direction and distance.
        """
        self.direction = random.choice([-1, 0, 1])
        new_idx = idx + self.direction * self.distance
        
        return new_idx

#Fish class with the standard attribute movement and offspring set to 1 
class Fish(Animal):
    def __init__(self, direction=None, distance=1,offspring=1,has_moved=0):
        super().__init__("fish", direction , distance, offspring,has_moved)
        
    def move(self, idx):
        """
        Move fish to adjacent index based on given direction and distance.
        """
        self.direction = random.choice([-1, 0, 1])
        new_idx = idx + self.direction * self.distance
        
        return new_idx
    

   