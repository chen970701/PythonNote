import time
for i in range(101):
    print("\r{}{} process:{}%".format("*"*i,"_"*(100-i),i),end="")
    time.sleep(0.1)
