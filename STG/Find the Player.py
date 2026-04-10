def find_player(grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height): #for (int i = 0; i < length; i++)
        for col in range(width): #for (int i = 0; i < length; i++)
            if grid[row][col] == "P":
                return [row, col]
            
game_map = [
    [0, 0, 0, 0],
    [0, 0, "P", 0],
    [0, 0, 0, 0]
]

print(find_player(game_map))