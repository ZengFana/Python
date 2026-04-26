item_weights = {
    "Apple" : 2,
    "Gem" : 5,
    "Mushroom" : 1
}
my_bag = {}
total_weight = 0
print("負重採集模式")
while True:
    item = input("撿到什麼?(輸入exit結束):")
    if item == "exit":
        break
    if item == "Trash":
        print("這是垃圾，我不撿！")
        continue
    if item in item_weights:
        incoming_weights = item_weights[item]
    else:
        incoming_weights = 0.5
    if total_weight + incoming_weights > 15:
        print(f"這個太重了{item}重,{incoming_weights}KG")
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