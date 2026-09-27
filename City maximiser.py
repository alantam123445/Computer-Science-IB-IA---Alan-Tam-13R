import sys
import os
import random #python libraries used in the program

class District:
    def __init__(self, name, symbol, cost, upkeep, base_score): #Base attributes of the district
        self.name = name #Name of the district eg. residential, commericial
        self.symbol = symbol #Letter symbol representing the district
        self.cost = cost #Cost of placing the district onto the map
        self.upkeep = upkeep #cost of maintaining (residential and recreational only)
        self.base_score = base_score #Score that it would provide to the total
    def get_details(self):  #Prints detail and attributes of the district
        return f"District Name: {self.name}, Symbol: {self.symbol}, Cost: {self.cost}, Upkeep: {self.upkeep}, Base Score: {self.base_score}"

class Residential(District): #Residential subclass
    def __init__(self, name, symbol, cost, upkeep, base_score):
        super().__init__(name, symbol, cost, upkeep, base_score) #inherits attributes of the district template
        self.population = 50 #provides a population score which contributes to the total, also is needed for placing other stuff
    def get_details(self):
        return f"{super().get_details()}"
    
class Commercial(District): #Commercial subclass
    def __init__(self, name, symbol, cost, upkeep, base_score):
        super().__init__(name, symbol, cost, upkeep, base_score)
        self.revenue = 100 #revenue per round
    def get_details(self):
        return f"{super().get_details()}"
      
class industrial(District): #industrial subclass
    def __init__(self, name, symbol, cost, upkeep, base_score):
        super().__init__(name, symbol, cost, upkeep, base_score)
        self.revenue = 300 #Revenue per round
    def get_details(self):
        return f"{super().get_details()}"

class Recreational(District): #recreational subclass
    def __init__(self, name, symbol, cost, upkeep, base_score):
        super().__init__(name, symbol, cost, upkeep, base_score)
    def get_details(self):
        return f"{super().get_details()}"
    
class CityGrid: #Object representing the city grid
    def __init__(self, width, height, grid):
        self.width = width 
        self.height = height
        self.grid = grid 
        self.bonus = 0 # 2D list representing the city grid
    def grid_render(self): #Prints the grid in a readable format
        for row in self.grid:
            print(row)
    def is_empty(self, x, y): #Checks if a specific cell in the grid is empty or occupied
        if self.grid[y][x] == '.': #Checks for an empty cell at a specific coordinate
            return "Empty"
        else:
            return "Occupied"
    def neighbour_residential(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j] == "R": #Checks for residential districts in the grid
                    if self.grid[i+1][j] == "P" or self.grid[i-1][j] == "P" or self.grid[i][j+1] == "P" or self.grid[i][j-1] == "P": #Checks for neighbouring park districts
                        self.bonus += 10
                    elif self.grid[i+1][j] == "I" or self.grid[i-1][j] == "I" or self.grid[i][j+1] == "I" or self.grid[i][j-1] == "I": #Checks for neighbouring industrial districts
                        self.bonus -= 10
                    elif self.grid[i+1][j] == "C" or self.grid[i-1][j] == "C" or self.grid[i][j+1] == "C" or self.grid[i][j-1] == "C": #Checks for neighbouring commercial districts
                        self.bonus += 3
                    else:
                        self.bonus += 0
    def neighbour_commercial(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j] == "C": #Checks for commercial districts in the grid
                    if self.grid[i+1][j] == "I" or self.grid[i-1][j] == "I" or self.grid[i][j+1] == "I" or self.grid[i][j-1] == "I": #Checks for neighbouring industrial districts
                        self.bonus += 3
                    else:
                        self.bonus += 0
                        

grid = [[".", ".", ".", ".", "."], #Grid for the city with empty cells represented by "."
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]]

city = CityGrid(5, 5, grid)
city.grid_render()