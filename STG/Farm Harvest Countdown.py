def count_ready_crops(farm):
    total_crops = 0
    for row in farm:
        for cell in row:
            if cell == 1:
                total_crops = total_crops+1
    return total_crops

my_farm = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

print(count_ready_crops(my_farm))