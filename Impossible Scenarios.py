#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def impossibleScenarios(n, m):
    # Initialize the grid with 0 indicating an empty cell
    grid = [[0] * n for _ in range(n)]

    # Place gold at a random location (start location may be considered)
    gold_row, gold_col = 0, 0  # Default to start location
    if n > 1:
        gold_row, gold_col = random.randint(0, n - 1), random.randint(0, n - 1)
        while (gold_row == 0 and gold_col == 0):
            gold_row, gold_col = random.randint(0, n - 1), random.randint(0, n - 1)
    grid[gold_row][gold_col] = "G"

    # Place pits at random locations (not at start or gold locations)
    for _ in range(m):
        pit_row, pit_col = random.randint(0, n - 1), random.randint(0, n - 1)
        while (pit_row == 0 and pit_col == 0) or (pit_row == gold_row and pit_col == gold_col):
            pit_row, pit_col = random.randint(0, n - 1), random.randint(0, n - 1)
        grid[pit_row][pit_col] = "P"

    # Define a helper function to check if a cell is valid
    def is_valid(row, col):
        return 0 <= row < n and 0 <= col < n

    # Define a recursive function to explore different scenarios
    def explore(row, col, visited):
        if not is_valid(row, col) or grid[row][col] == "P" or (row, col) in visited:
            return 0
        if grid[row][col] == "G":
            return 1
        visited.add((row, col))  # Mark cell as visited
        count = explore(row + 1, col, visited) + explore(row - 1, col, visited) + explore(row, col + 1, visited) + explore(row, col - 1, visited)
        visited.remove((row, col))  # Reset cell as not visited
        return count

    # Check the scenario from the start cell
    start_count = explore(0, 0, set())

    # If no path from the start cell to the gold cell exists, return 1, otherwise 0
    return 1 if start_count == 0 else 0

# Example usage:
n = 4  # Size of the grid
m = 5  # Number of pits

# Number of impossible scenarios
impossible_count = sum(impossibleScenarios(n, m) for _ in range(1000))  # Adjust the number of iterations as needed
print("Number of impossible scenarios:", impossible_count)


# In[ ]:




