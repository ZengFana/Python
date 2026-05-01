class Target:
    def __init__(self,target_id,inital_x):
        self.id = target_id
        self.x = inital_x
        return


    def check_status(self):
        if self.x < 14.0:
            print(f"警告 目標{self.id} 距離 {self.x} 太近了")
        else:
            print(f"安全 目標{self.id} 距離 {self.x} 正常")

#這邊的意思是 我用T1跟T2建立一個橋 連接__init__這個一開場的物件 並把值傳回去
# target1 = Target("t-001", 12.0)
# target2 = Target("t-002", 25.8)

#這邊就是 T1跟T2呼叫工具 把上面的參數 調到工具內
# target1.check_status()
# target2.check_status()

# target1.x
# target1.check_status()