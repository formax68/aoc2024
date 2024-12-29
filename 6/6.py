
map_file = "map.txt"
grid = []
guard_directions = ["^",">","v","<"]

with open(map_file, 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

def next_position(direction,x,y,grid):
    if direction == "^":
        return x-1,y,grid[x-1][y]
    elif direction == "v":
        return x+1,y,grid[x+1][y]
    elif direction == "<":
        return x,y-1,grid[x][y-1]
    elif direction == ">":
        return x,y+1,grid[x][y+1]

def get_guard_position(grid):
    for x,row in enumerate(grid):
        for y,direction in enumerate(row):
            if direction in guard_directions:
                return direction,x,y
    raise ValueError("No guard found in the grid")

def move_guard(direction,x,y,grid):
    if 0 > x or x >= len(grid[0])-1 or 0 > y or y >= len(grid)-1:
        grid[x][y] = "X"
        return "F",x,y,grid
    new_x, new_y, new_spot = next_position(direction,x,y,grid)
    if new_spot == "#":
        direction_index = guard_directions.index(direction)
        new_direction = guard_directions[(direction_index + 1) % len(guard_directions)]
        grid[x][y] = new_direction
        return new_direction,x,y,grid
    else:
        grid[x][y] = "X"
        grid[new_x][new_y] = direction
        return direction,new_x,new_y,grid

if __name__ == "__main__":
    # print(get_guard_position(grid))
    direction,x,y = get_guard_position(grid)
    print(f"x is {x}, y is {y}")
    print(f"len(grid[0] is {len(grid[0])}")
    print(f"len(grid) is {len(grid)}")
    input("Press any key to continue")
    while direction != "F":
        direction,x,y,grid = move_guard(direction,x,y,grid)
        print(direction,x,y)
        # input("Press Enter")
    positions = 0
    for row in grid:
        print(''.join(row))
        for char in row:
            if char == "X":
                positions += 1
    print(positions)
