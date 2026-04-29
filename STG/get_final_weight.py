# def get_final_weight(item:str,level:int) -> float:
#     weight = {"Apple":2,"Gem":5}
#     base_w = weight.get(item,0.5)
#     if level > 5:
#         return base_w * 0.8
#     else:
#         return base_w
# while True:
#     item_input = input("要送什麼")
#     level_input = input("等級")
#     if item_input == "Exit": break
# --- 第一步：定義機器 (廚房) ---
def get_final_weight(item: str, level: int) -> float:
    weights = {"Apple": 2.0, "Gem": 5.0}
    base_w = weights.get(item, 0.5)
    
    if level > 5:
        return base_w * 0.8
    else:
        return base_w

# --- 第二步：拿到使用者的輸入 (櫃檯) ---
# 這裡就是你最擅長的 input 部分！
item_name = input("你想撿什麼？ ").strip().capitalize()
user_level = int(input("你現在幾級？ ")) # 記得要轉成 int，因為等級是數字

# --- 第三步：把兩個東西一起「投進」機器裡 (執行) ---
result = get_final_weight(item_name, user_level)

print(f"計算結果：{item_name} 對於 {user_level} 級玩家的重量是 {result}kg")