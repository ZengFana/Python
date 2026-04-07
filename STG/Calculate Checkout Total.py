def calculate_total(cart,prices):
    total_cost = 0
    for x in cart:
        if x in prices:
            total_cost = total_cost + prices[x]
    return total_cost
menu = {"蘋果": 50, "香蕉": 20, "牛奶": 100, "麵包": 40}

print(calculate_total(["蘋果", "蘋果", "牛奶"], menu)) 
print(calculate_total(["香蕉", "麵包", "找不到的神秘果實"], menu))