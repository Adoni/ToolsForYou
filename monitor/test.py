import time

for i in range(10):
    a=[]
    for j in range(10000000*i):
        a.append(j)
    print(i)
    time.sleep(i*1)
