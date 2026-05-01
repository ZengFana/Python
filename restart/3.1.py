from T_core import Target
import random,time

my_target = Target("T-003",15.0)
my_target.check_status()
for x in range(5):
    print(f"\n目前是第{x+1}次")
    new_inital = random.uniform(12.0,17.0)
    my_target.x = new_inital
    my_target.check_status()