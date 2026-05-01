class TrackedPoint:
    def __init__(self,target_id,x_dist,speed,is_valid):
        self.id = target_id
        self.x = x_dist
        self.sp = speed
        self.iv = is_valid
    
    def analyze_risk(self):
        if self.iv == False:
            print("沒辦法")
        elif self.x < 10.0 and self.sp > 10.0:
            # print(f"警告{self.id}過近")
            print([self.id])
        else:
            pass
            # print(f"{self.id}很安全")


raw_frames = [
    {"target_id": "P-01", "x_dist": 15.2, "speed": 1.5, "is_valid": True},
    {"target_id": "P-02", "x_dist": 8.5,  "speed": 12.0, "is_valid": True},
    {"target_id": "P-03", "x_dist": 2.1,  "speed": 0.0,  "is_valid": False},
    {"target_id": "P-04", "x_dist": 4.0,  "speed": 15.5, "is_valid": True}
    ]
# raw_frames = TrackedPoint
# raw_frames.analyze_risk()

for data in raw_frames:
    t_id = data["target_id"]
    x = data["x_dist"]
    s = data["speed"]
    v = data["is_valid"]

    point = TrackedPoint(t_id,x,s,v)

    point.analyze_risk()