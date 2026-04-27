# 1. 建立空背包
my_bag = {}

print("--- 農場採集開始 (預計記錄 3 樣東西) ---")

# 2. 寫一個跑 3 次的迴圈 (提示：用 range(3))
for i in range(3):
    # (1) 讓使用者輸入東西名稱
    item = input(f"第 {i+1} 樣東西是：")
    if item in my_bag:
        my_bag[item] += 1
    else:
        my_bag[item] = 1
    
    # ----------------

# 3. 最後印出結果
print("\n--- 今天的採集總結 ---")
print(my_bag)