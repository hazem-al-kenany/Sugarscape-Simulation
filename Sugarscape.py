import numpy as np
import matplotlib.pyplot as plt
import random

class Sugarscape:
    def __init__(self, grid_size, num_agents):
        self.grid_size = grid_size
        self.num_agents = num_agents
        #initialize a grid with hotspots by setting higher sugar values in certain areas
        self.grid = np.random.randint(1, 4, (grid_size, grid_size))  #base sugar levels (1-3)
        for _ in range(10):  #create 10 hotspots with high sugar values
            x, y = np.random.randint(0, grid_size, 2)
            self.grid[x-1:x+2, y-1:y+2] = 10  #3x3 area with high sugar (10)
        
        #initialize agents at random positions
        self.agents = [(np.random.randint(0, grid_size), np.random.randint(0, grid_size)) for _ in range(num_agents)]
        
    def move_agents(self):
        new_positions = []
        for x, y in self.agents:
            #define possible moves: stay in place, move up, down, left, or right
            possible_moves = [(x, y), 
                              ((x-1) % self.grid_size, y), ((x+1) % self.grid_size, y), 
                              (x, (y-1) % self.grid_size), (x, (y+1) % self.grid_size)]
            
            #choose a move based on sugar levels, allowing some randomness
            sugar_levels = [self.grid[pos[0], pos[1]] for pos in possible_moves]
            max_sugar = max(sugar_levels)
            preferred_moves = [pos for pos, sugar in zip(possible_moves, sugar_levels) if sugar >= max_sugar - 1]
            next_move = random.choice(preferred_moves)
            new_positions.append(next_move)
        
        #update agent positions after moving
        self.agents = new_positions
    
    def update_grid(self):
        #decrease sugar in each cell gradually (regeneration effect can be added here)
        self.grid = np.clip(self.grid - 0.1, 1, None)  #ensure minimum sugar level remains 1

    def calculate_density(self):
        #calculate clustering based on local density in a 3x3 area around each agent
        density_count = 0
        for x, y in self.agents:
            neighbors = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2)]
            cluster_size = sum(1 for nx, ny in neighbors if (nx % self.grid_size, ny % self.grid_size) in self.agents)
            if cluster_size > 4:  #more than 4 agents within the 3x3 area indicates clustering
                density_count += 1
        return density_count / len(self.agents)  #ratio of agents in clustered areas

    def run(self, iterations):
        density_data = []
        for _ in range(iterations):
            self.move_agents()  #move agents
            self.update_grid()  #update sugar values
            density_data.append(self.calculate_density())  #calculate density (clustering) index
        return density_data

#simulation parameters
grid_size = 20
num_agents = 50
iterations = 1000

#run the Sugarscape model
sugarscape = Sugarscape(grid_size=grid_size, num_agents=num_agents)
density_data = sugarscape.run(iterations=iterations)

#plot the density (clustering) index over time
plt.plot(density_data)
plt.xlabel('Iteration')
plt.ylabel('Density (Clustering) Index')
plt.title('Clustering Index Over Time in Revised Sugarscape Model')
plt.show()
