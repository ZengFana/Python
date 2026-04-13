""" name = "python"
if name == "java" or "html":print("login vlaid")
else: print("not vlaid")
if name == "java" or name == "html":
    print("login vlaid")
else: print("not vlaid")
if name in ["java","html"]:
    print("login vlaid")
else: print("not vlaid") """

fruits = ["apple","banana","mango","kiwi","grape"]
for f in fruits:
    if "a" in f:
        fruits.remove(f)
print(fruits)

food = "Pizza"
food.replace("z", "s")
print(food)

name = "Mouse"
print(name[1:4])

my_list = [10,20,30,40]
print(my_list[:-1])

arr = [1,2,3,4]
x = arr [1] + arr[2] * arr[3];
print(x)