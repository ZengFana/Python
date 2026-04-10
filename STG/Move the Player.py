def move_player(current_pos, direction):
    row = current_pos[0]
    col = current_pos[1]
    # if direction == "up":
    #     new_row = row - 1
    #     new_col = col
    # elif direction == "down":
    #     new_row = row + 1
    #     new_col = col
    # elif direction == "left":
    #     new_row = row
    #     new_col = col - 1
    # elif direction == "right":
    #     new_row = row
    #     new_col = col + 1
    # else:
    #     return direction
    if direction == "up":
        new_row, new_col = row - 1, col
    elif direction == "down":
        new_row, new_col = row + 1, col
    elif direction == "left":
        new_row, new_col = row, col - 1
    elif direction == "right":
        new_row, new_col = row, col + 1
    if 0 <= new_row < 5 and 0 <= new_col < 5:
        return [new_row, new_col]
    else:
        return current_pos
    
    
print(move_player([2, 2], "down"))    # 預期輸出: [1, 2]
print(move_player([0, 1], "right"))  # 預期輸出: [0, 0] (撞牆)