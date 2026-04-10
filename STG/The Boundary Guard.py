def is_inside_map(row, col):
    if row >= 0 and row < 5 and col >= 0 and col < 5:
        return True
    else:
        return False
    # if 0 <= row < 5 and 0 <= col < 5:
    #     return True
    # else:
    #     return False

print(is_inside_map(2, 3))   # 應該印出 True
print(is_inside_map(5, 2))   # 應該印出 False
print(is_inside_map(-1, 0))  # 應該印出 False
print(is_inside_map(4, 4))   # 應該印出 True