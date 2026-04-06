def filter_high_value(prices):
    good_items = []
    for x in prices:
        if x >= 100:
            good_items.append(x)
    return good_items
print(filter_high_value([40, 150, 80, 300, 250, 15]))
print(filter_high_value([10, 50, 99]))