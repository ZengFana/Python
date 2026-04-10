def check_for_gem(grid, position):
    # height = len(grid)
    # width = len(grid[0])
    # row = position[0]
    # col = position[1]
    # for h in range(height):
    #     for w in range(width):
    #         if grid[row][col] == "G":
    #             return "找到寶石了!"
    #         else:
    #             return "這裡空空如也"
    row = position[0]
    col = position[1]
    
    # 2. 不用迴圈，直接「精準定位」
    if grid[row][col] == "G":
        return "找到寶石了!"
    else:
        return "這裡空空如也"

farm_map = [
    [0, 0, 0],
    [0, "G", 0],
    [0, 0, 0]
]

print(check_for_gem(farm_map, [1, 1]))
print(check_for_gem(farm_map, [0, 0]))