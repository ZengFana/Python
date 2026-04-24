def check_for_gem(grid, position):
    height = len(grid)
    width = len(grid[0])
    row = position[0]
    col = position[1]
    for h in range(height):
        for w in range(width):
            if grid[row][col] == "G":
                return "找到寶石了!"
            else:
                return "這裡空空如也"
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

# print(check_for_gem(farm_map, [1, 1]))
# print(check_for_gem(farm_map, [0, 0]))

# def collect_item(grid,position,inventory):
def collect_item(grid: list, position: list, inventory: dict) -> tuple:
    r,c = position[0],position[1]
    item = grid[r][c]

    if item !=0:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
        grid[r][c] = 0
    print(type(grid),type(position),type(inventory))
    return grid,inventory

farm_map = [
    ["G", 0, 0],
    [0, "M", 0],
    [0, 0, "G"]
]

# 2. 準備一個初始背包（裡面已經有一個寶石了）
my_bag = {}
path = [[0,0],[1,1],[2,2]]

print("--- 動作一：去 [1, 1] 撿蘑菇 ---")
# 呼叫你寫的完美函式！
farm_map, my_bag = collect_item(farm_map, [1, 1], my_bag)
print("目前背包:", my_bag)    # 預期：{'G': 1, 'M': 1}
print("地圖 [1, 1] 的狀況:", farm_map[1][1]) # 預期：0 (被撿走了)

print("\n--- 動作二：再去 [0, 0] 撿另一顆寶石 ---")
farm_map, my_bag = collect_item(farm_map, [0, 0], my_bag)
print("目前背包:", my_bag)    # 預期：{'G': 2, 'M': 1}
print("地圖 [0, 0] 的狀況:", farm_map[0][0]) # 預期：0

for pos in path:
    farm_map,my_bag = collect_item(farm_map,pos,my_bag)
    print(f"走到{pos},目前的背包:{my_bag}")
print("\n--- 最終結果 ---")
print("最後背包裡的東西:", my_bag)
print("最後的地圖狀態:", farm_map)

# class Player:
#     def __init__(self, name):
#         self.name = name       # 「我的」名字叫什麼？
#         self.inventory = {}    # 「我的」背包是空的

#     def collect(self, item):
#         # 這裡的 self.inventory 確保東西是進到「這個玩家」的包包
#         if item in self.inventory:
#             self.inventory[item] += 1
#         else:
#             self.inventory[item] = 1

# # 建立兩個不同的玩家
# p1 = Player("小明")
# p2 = Player("小華")

# p1.collect("寶石") # 這時候 self 就是 p1，所以只有小明拿到寶石
# 1. 先執行函式，把結果接住
result = collect_item(farm_map, [1, 1], my_bag)

# 2. 檢查這個「結果」是什麼型態
print(f"函式回傳的總型態是: {type(result)}") 

# 3. 如果想看裡面的細節（因為回傳了兩樣東西）
print(f"回傳的第一個東西是: {type(result[0])}") # 應該是 list (地圖)
print(f"回傳的第二個東西是: {type(result[1])}") # 應該是 dict (背包)
