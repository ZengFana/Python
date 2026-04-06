def count_ores(inventory):
    counts = {}
    for ore in inventory:
        if ore not in counts:
            counts[ore]=1
        else:
            counts[ore] = counts[ore] + 1
    return counts
print(count_ores(["鐵礦", "銅礦", "鐵礦", "鑽石", "銅礦", "鐵礦"]))
print(count_ores(["煤炭", "煤炭", "煤炭"]))