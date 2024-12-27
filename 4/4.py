
import numpy as np
import re

file_data = np.loadtxt("input4.txt", dtype=str)

def count(grid):
    rows = len(grid)
    cols = len(grid[0])
    total_count=0

    def extract_diagonal(start_row, start_col, direction):
            diagonal = []
            row, col = start_row, start_col
            while 0 <= row < rows and 0 <= col < cols:
                diagonal.append(grid[row][col])
                if direction == "major":  # Top-left to bottom-right
                    row += 1
                    col += 1
                elif direction == "anti":  # Top-right to bottom-left
                    row += 1
                    col -= 1
            return "".join(diagonal)   

    def count_string(string):
        count = 0
        count += len(re.findall("XMAS", string))
        count += len(re.findall("SAMX", string))
        return count

    for row in grid:
        total_count += count_string(row)
    for col in range(cols):
        column_string = ''.join(grid[row][col] for row in range(rows))
        total_count += count_string(column_string)
    for row in range(rows):
        total_count += count_string(extract_diagonal(row, 0, "major"))
        total_count += count_string(extract_diagonal(row, cols - 1, "anti"))
    for col in range(1, cols):
        total_count += count_string(extract_diagonal(0, col, "major"))
    for col in range(cols - 2, -1, -1):
        total_count += count_string(extract_diagonal(0, col, "anti"))

    return total_count

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count=0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            top_left_bottom_right = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            top_right_bottom_left = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
            if top_left_bottom_right in ("MAS", "SAM") and top_right_bottom_left in ("MAS", "SAM"):
                count += 1

    return count

print(count_x_mas(file_data))
        
