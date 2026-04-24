# 沒寫提示：電腦跑得動，但你過三天看這行會忘記它回傳什麼
def get_score(name):
    return 100

# 有寫提示：一眼就看出這函式會給你一個整數 (int)
def get_score(name: str) -> int:
    return 100