def get_weight(item_name : str) -> float:
    weights = {"Apple":2,"Gem":5,"net":3}
    # if item_name in weights:
    #     return weights[item_name]
    # else:
    #     return 0.5
    return weights.get(item_name,0.5)

my_bag={}
total_weight=0
while True:
    raw_input = input("輸入點什麼").strip().capitalize()
    # item = raw_input
    if raw_input == "Exit":break
    incoming_weight=get_weight(raw_input)
    if total_weight + incoming_weight > 15:
        print(f"太種了{raw_input},{incoming_weight}kg 放不下了")
        continue
    my_bag[raw_input] = my_bag.get(raw_input,0) + 1
    total_weight += incoming_weight
    print(f"成功放入{raw_input}目前總重{total_weight}kg")
