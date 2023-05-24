from random import random

arr = list(range(1,45+1))

for i in arr:
    rnd = int(random()*45)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp

print(arr[:6])
