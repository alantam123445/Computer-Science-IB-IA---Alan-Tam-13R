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
    def calculate_bonus(self, nearby): #Calculates the bonus score for residential districts based on neighbouring districts
        bonus = 0
        for district in nearby:
            if district == 'C':
                bonus += 10 #Commercial districts provide a bonus of 10
            elif district == 'I':
                bonus -= 5 #Industrial districts provide a penalty of -5
            elif district == 'R':
                bonus += 5 #Recreational districts provide a bonus of 5
        return bonus
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
    def neighbour_list(self, x, y): #Calculates the neighbour districts for residential districts based on neighbouring districts
            nearby = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i == 0 and j == 0) or (x + i < 0 or x + i >= self.width or y + j < 0 or y + j >= self.height):
                        continue
                    if abs(i) == abs(j):
                        continue
                    neighbour = self.grid[y + j][x + i]
                    if neighbour == 'C':
                        nearby.append('C')
                    elif neighbour == 'I':
                        nearby.append('I')
                    elif neighbour == 'R':
                        nearby.append('R')
            return nearby

grid = [[".", ".", ".", ".", "."], #Grid for the city with empty cells represented by "."
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]]

city = CityGrid(5, 5, grid)
city.grid_render()