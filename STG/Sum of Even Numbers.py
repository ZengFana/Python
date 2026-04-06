def sum_of_evens(numbers):
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total=total+x
    return total

print(sum_of_evens([1,2,3,4,5,6]))