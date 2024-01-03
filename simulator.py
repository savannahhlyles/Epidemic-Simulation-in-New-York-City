import random
import math
from matplotlib import pyplot as plt
import numpy as np

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    

recovery_time = 4 # recovery time in time-steps
virality = 0.8    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0

    def __repr__(self):
        return f"Cell(x={self.x}, y={self.y}, state={self.state}, time={self.time})"

    def infect(self): # Step 2.1
        self.state = 'I'
        self.time = 0

  
    def process(self, adjacent_cells):  # Step 2.3
        # determine recovery
        if self.state == 'I' and self.time >= recovery_time:
            self.state = 'S'
            self.time = 0
        # determine cell death
        if self.state == 'I':
            death_float = random.random()
            if death_float <= pdeath(self.time, 3, 1):
                self.state = 'R'
        # determine infection
        if self.state == 'I' and self.time>=1:
            for cell in adjacent_cells:
                if cell.state == 'S':
                    viral_float = random.random()
                    if viral_float <= virality:
                        cell.infect()
        self.time += 1


class Map(object):

    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell): # Step 1.1 
        self.cells[(cell.x, cell.y)] = cell
    # This method takes a cell object as its parameter and inserts it into the cells dictionary. The keys of this dictionary will be tuples of (x,y) coordinates, and the values will be Cell instances.

    def display(self): # Step 1.3
        red, green, blue = range(3)  # RGB indexes
        image_array = np.zeros((self.height, self.width, 3))  # Corrected dimensions

        for i in range(self.width):
            for j in range(self.height):
                if (i, j) in self.cells:
                    cell = self.cells[(i, j)]
                    if cell.state == 'S':
                        image_array[i, j, green] = 1.0
                    elif cell.state == 'I':
                        image_array[i, j, red] = 1.0
                    elif cell.state == 'R':
                        image_array[i, j, :] = [0.5, 0.5, 0.5]
                else:
                    # make cell black
                    image_array[i, j, :] = [0, 0, 0]

        plt.imshow(image_array)
        # Each cell should be displayed in the color that represents its state: green if the state is S, red if the state is I and gray if the state is R. Pixels in the image that do not correspond to a cell on the map should be displayed in black. 


    def adjacent_cells(self, x, y): # Step 2.2
        adjacent_cells = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        cell_list = [self.cells.get(cell, None) for cell in adjacent_cells]
        return [cell for cell in cell_list if cell is not None]

    def time_step(self):
        for cell in self.cells.values():
            adjacent = self.adjacent_cells(cell.x, cell.y)
            cell.process(adjacent)
        self.display()


def read_map(filename):
    m = Map()
    with open(filename) as nyc_map:
        for line in nyc_map:
            x, y = map(int, line.strip().split(','))
            # Create a new Cell instance with the extracted coordinates
            c = Cell(x, y)
            # Add the cell to the map
            m.add_cell(c)

    return m
# This function should reads in x,y coordinates from a file, create a new Cell instance for each coordinate pair. The function should return a Map instance containing all the cells.
