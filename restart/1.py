name = "這是一個重新開始的地方"
status = "啟動中"
version = 1.0

print(name,status,version)
print("系統紀錄：" + name + "，狀態：" + status + "，版本：" + str(version))

print(version+1)

x_positions = [12.5,13.0,14.2]
target_info = {"id":"T-001","speed":2.5,"is_active":True}

print(f"id{target_info['id']},speed{target_info['speed']}")

x_positions.append(15.8)
print(x_positions)

if target_info["is_active"]:
    print("True")
else:
    print("No")

for x in x_positions:
    if x < 14.0:
        print(f"{x}")
    else:
        print("爆了")
    # print(f"X={x}")

def greet(target_name):
    print(f"目標:{target_name}")

greet("T-001")
greet("T-002")

def check_distance(data_list):
    for x in data_list:
        if x < 14.0:
            print(f"X:{x}")
        else:
            print("Error")


x_positions = [12.5,13.0,14.2,15.8]
check_distance(x_positions)