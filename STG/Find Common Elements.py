def find_common(list1,list2):
    list=[]
    for x in list1:
        if x in list2:
            list.append(x)
    return list
print(find_common([1, 2, 3], [3, 4, 5]))
print(find_common(["apple", "banana"], ["banana", "orange", "apple"]))
print(find_common([10, 20], [30, 40]))