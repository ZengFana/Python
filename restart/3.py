import random,time

class Target:
    def __init__(self,target_id:str,inital_x:float):
        self.id = target_id
        self.x = inital_x

    def check_status(self):
        if self.x < 14.0:
            print(f"警告 目標{self.id} 距離 {self.x} 太近了")
        else:
            print(f"安全 目標{self.id} 距離 {self.x} 正常")

my_target = Target("t-001",15.0)
for i in range(5):
    print(f"\n 第 {i+1} 次掃描")
    new_position = random.uniform(12.0,16.0)
    my_target.x = new_position
    my_target.check_status()
    time.sleep(1)
# my_target.check_status()

