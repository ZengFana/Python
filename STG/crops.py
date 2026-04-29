# crops = ["Apple","Banana","Apple","Orange","Apple","Grape"]
# count = 0
# for crop in crops:
#     if crop == "Apple":
#         count +=1
#     pass

# # print(f"總共收成了{count}個蘋果")

# bag = {"Apple":2}
# new_item = "Banana"

# if new_item in bag:
#     bag[new_item] += 1
# else:
#     bag[new_item] = 1

# print(f"更新後的包包:{bag}")

# grid = [
#     ["Soil", "Soil", "Seed"],  # 第 0 列 (Row 0)
#     ["Soil", "Water", "Soil"], # 第 1 列 (Row 1)
#     ["Rock", "Soil", "Soil"]   # 第 2 列 (Row 2)
# ]

# i = int(input("列"))
# j = int(input("行"))
# pos = [i, j] # [列, 行]

# # --- 這裡換你寫 ---
# # 提示：row 應該是 pos 的第 0 個數字，col 是第 1 個數字
# # 然後用 grid[row][col] 抓出來


# row = pos[0]
# col = pos[1]
# result = grid[row][col]

# # ----------------

# print(f"座標 {pos} 的東西是: {result}")
# # 預期輸出：座標 [2, 0] 的東西是: Rock

# 1. 建立空背包
# my_bag = {}

# print("--- 農場採集開始 (預計記錄 3 樣東西) ---")

# # 2. 寫一個跑 3 次的迴圈 (提示：用 range(3))
# for i in range(3):
#     # (1) 讓使用者輸入東西名稱
#     item = input(f"第 {i+1} 樣東西是：")
#     if item in my_bag:
#         my_bag[item] += 1
#     else:
#         my_bag[item] = 1
    
#     # ----------------

# # 3. 最後印出結果
# print("\n--- 今天的採集總結 ---")
# print(my_bag)

# my_bag = {}

# print("--- 無限採集模式 (輸入 'exit' 結束結算) ---")

# while True:
#     item = input("撿到了什麼？ ")
#     if item == "exit":
#         break
#     elif item == "Trash":
#         print("這是垃圾，我不撿！")
#         continue
#     elif item in my_bag:
#         my_bag[item] += 1
#     else:
#         my_bag[item] = 1
#     # --- 這裡換你寫：判斷是否要 exit，或是更新背包 ---
    
#     # ----------------

# print("最後背包狀態：", my_bag)

item_weights = {
    "Apple" : 2,
    "Gem" : 5,
    "Mushroom" : 1
}
my_bag = {}
total_weight = 0
print("負重採集模式")
while True:
    raw_input = input("撿到什麼?(輸入exit結束):")
    item = raw_input.strip().capitalize()
    if item == "Exit":
        break
    if item == "Trash":
        print("這是垃圾，我不撿！")
        continue
    if item in item_weights:
        incoming_weights = item_weights[item]
    else:
        incoming_weights = 0.5
    if total_weight + incoming_weights > 15:
        incoming_weights -= total_weight
        print(f"這個太重了{item}重,{incoming_weights}KG")
        continue
    if item == "Bag":
        print(f"目前背包內有{my_bag},總重量來到{total_weight}KG")
        continue

    if item in my_bag:
        my_bag[item] += 1
    else:
        my_bag[item] = 1
    if item in item_weights:
        total_weight += item_weights[item]
    else:
        total_weight += 0.5
    # if total_weight >= 15:
    #     print("超過15KG爆了")
    #     break
print("\n--- 結算 ---")
print(f"背包內容: {my_bag}")
print(f"總重量: {total_weight} kg")