# -*- coding: utf-8 -*-
"""
Created on  Created on 16.02.2023

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt


Use Case we had in mind: 
Our aim was to develop an ecosystem which includes some examples of modular code that go beyond a narrow interpretation of the task we were presented with. 
For instance, our code allows variability in the behaviour of different animals such as the distance of movement or the number of offspring generated from a mating.
Defaults for amendable features where set to meet the task's requirements.


Assumptions: 

- When a new animal spawns, it only moves in the next round 

- The player must define the length of the river, the number of fish and the number of bears; the total number of bear and fish cannot exceed the length of the river 

- Elements of randomness: 
            (i) initial position of fish and bear, 
            (ii) direction of movement, 
            (iii) the order in which animals move in any round, 
            (iv) the position of new offspring after spawning 

- The river list is never handed to animals, ensure robustness

 - Since the code is not intended as an interface for public use, we decided against using private variables. However, this could be implemented easily

"""

from River import River

river = River(10,2,2) # set the parameters for your desired ecosystem (length of river, number of bears, number of fish)
river.display()
river.next_timestep(2) # number of rounds to be simulated