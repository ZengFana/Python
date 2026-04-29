def cal(a : int ,b : int , r : str) -> float:
    if r == "+":
        return a + b
    elif r == "-":
        return a-b
    elif r == "*":
        return a*b
    elif r == "/":
        return a/b
    else:
        if a or b == 0:
            print("你在打什麼")
        print("??")

n1 = int(input("a"))
n2 = int(input("b"))
q = input("R")
result = cal(n1,n2,q)
print(f"a={n1},r={q},b={n2}={result}")