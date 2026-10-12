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
            if district == 'P':
                bonus += 10 #Commercial districts provide a bonus of 10
            elif district == 'I':
                bonus -= 10 #Industrial districts provide a penalty of -10
            elif district == 'C':
                bonus += 3 #Commercial districts provide a bonus of 3
        return bonus
class Commercial(District): #Commercial subclass
    def __init__(self, name, symbol, cost, upkeep, base_score):
        super().__init__(name, symbol, cost, upkeep, base_score)
        self.revenue = 100 #revenue per round
    def get_details(self):
        return f"{super().get_details()}"
      
class Industrial(District): #industrial subclass
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
                    elif neighbour == 'P':
                        nearby.append('P')
            return nearby
    def upkeep_calculation(self):
        UpkeepTotal = 0
        for i in self.grid:
            for r in i:
                if self.grid[self.grid.index(i)][i.index(r)] == 'P':
                    UpkeepTotal += 10
                elif self.grid[self.grid.index(i)][i.index(r)] == 'R':
                    UpkeepTotal += 5
                elif self.grid[self.grid.index(i)][i.index(r)] == 'C':
                    UpkeepTotal += 5
                elif self.grid[self.grid.index(i)][i.index(r)] == 'I':
                    UpkeepTotal += 10
                else:
                    UpkeepTotal += 0
        return UpkeepTotal
        
class GameEngine:
    def __init__(self, budget, turn, total_score):
        self.budget = 1000 #Initial budget for the player
        self.turn = 25 #Number of turns the player has
        self.total_score = 0 #Total score of the player
    def update_budget(self): #Updates the budget based on the cost of placing a district
        self.budget -= CityGrid.upkeep_calculation(self) #Calls the upkeep calculation function to deduct the upkeep cost from the budget
        return self.budget
    def update_score(self): #Updates the total score based on the score of the placed district
        self.total_score += Residential.calculate_bonus(self) #Calls the calculate bonus function to add the bonus score to the total score
        return self.total_score
    def update_turn(self): #Updates the turn count after each round
        self.turn -= 1
        return self.turn
    def place_district(self, district,x,y):#Places district at a specific coordinate
        if CityGrid.is_empty(self,x,y) == ".":
            CityGrid.grid[y][x] = district.symbol
            self.budget -= district.cost
            self.total_score += district.base_score
            print(f"{district.name} placed at ({x}, {y}). Budget: {self.budget}, Total Score: {self.total_score}")
        else:
            print(f"Cannot place {district.name} at ({x}, {y}). Cell is occupied.")
            
grid = [[".", ".", ".", ".", "."], #Grid for the city with empty cells represented by "."
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."]]

city = CityGrid(5, 5, grid)
city.grid_render()
