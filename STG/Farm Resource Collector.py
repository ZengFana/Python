def collect_item(grid, position, inventory):
    row = position[0]
    col = position[1]
    item = grid[row][col]
    if item != 0:
        if item in inventory: 
            inventory[item] += 1
        else:
            inventory[item] = 1
        grid[row][col] = 0
    return grid, inventory
farm_map = [
    ["G", 0],
    [0, "M"]
]
my_bag = {"G": 1}

print("原本的地圖:", farm_map)
print("原本的背包:", my_bag)

updated_map, updated_bag = collect_item(farm_map, [1, 1], my_bag)

print("--- 採集後 ---")
print("更新後的地圖:", updated_map)
print("更新後的背包:", updated_bag)