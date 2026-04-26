item_weights = {
    "Apple" : 2,
    "Gem" : 5,
    "Mushroom" : 1
}
my_bag = {}
total_weight = 0
print("負重採集模式")
limit = 15
while True:
    item = input(f"目前重量 {total_weight}kg，撿到了什麼？ ")
    if item == "exit": break
    if item == "Trash": continue
    # 1. 算出這次想撿的東西有多重
    incoming_weight = item_weights.get(item, 0.5) 
    # 2. 核心判斷：目前重量 + 新重量 是否會超過上限？
    if total_weight + incoming_weight > limit:
        print(f"❌ 拒絕採集！{item} 重 {incoming_weight}kg，但你只剩 {limit - total_weight}kg 的空間。")
        # 如果你希望「只要一過 14.5 就算滿了」，可以加這行：
        if (limit - total_weight) < 0.5:
            print("包包徹底滿了，結算退出！")
            break
        continue # 這次不算，回頭問下一題
    # 3. 確定沒問題才更新
    total_weight += incoming_weight
    if item == "exit":
        break
    if item == "Trash":
        print("這是垃圾，我不撿！")
        continue
    if item in item_weights:
        incoming_weights = item_weights[item]
    else:
        incoming_weights = 0.5
    if item in my_bag:
        my_bag[item] += 1
    else:
        my_bag[item] = 1
    # if total_weight >= 15:
    #     print("超過15KG爆了")
    #     break
print("\n--- 結算 ---")
print(f"背包內容: {my_bag}")
print(f"總重量: {total_weight} kg")