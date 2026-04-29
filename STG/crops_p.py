item_weights = {"Apple": 2, "Gem": 5, "Mushroom": 1}
my_bag = {}
total_weight = 0

while True:
    # 在這裡就處理好大小寫與空格！
    raw_input = input("撿到什麼？(輸入 exit/bag): ")
    item = raw_input.strip().capitalize() 
    
    # 注意：因為轉了 Capitalize，所以這裡要判斷 "Exit" 和 "Bag"
    if item == "Exit": break
    if item == "Bag":
        print(f"目前背包內容: {my_bag}, 總重: {total_weight}kg")
        continue

    # --- 以下邏輯就再也不怕大小寫了 ---
    if item == "Trash":
        print("垃圾不撿！")
        continue

    # 查重量 (現在保證能查到 Apple, Gem, Mushroom 了)
    incoming_weight = item_weights.get(item, 0.5)

    if total_weight + incoming_weight > 15:
        print(f"太重了！{item}({incoming_weight}kg) 會讓包包爆掉。")
        continue

    # 更新背包...
    my_bag[item] = my_bag.get(item, 0) + 1
    total_weight += incoming_weight