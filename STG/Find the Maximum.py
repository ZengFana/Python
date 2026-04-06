def find_max(numbers):
    y = numbers[0]
    for x in numbers:
        if x > y:
            y=x
    return y
print(find_max([3,1,4,7,2]))
print(find_max([-5,-1,-10]))