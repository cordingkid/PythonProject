from random import random

#홀짝을 입력하시오
mine = ""
com = ""
res = ""

mine = input("홀짝을 입력하세요")

rnd = random()

if rnd >0.5:
    com = "홀"
else:
    com = "짝"

if mine ==com:
    res = "정답"
else:
    res = "틀림"
    
print("나: ",mine)
print("컴: ",com)
print("결과: ",res)

print("바보",end="\t")
print("천재")