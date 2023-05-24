# 가위 바위 보를 선택하세요
# 나 는 가위
# 컴퓨터는 바위
#
# 나 가위
# 컴퓨터 바위
# 결과 짐

from random import random

me = input("가위/바위/보 를 입력하세요.")
com = ""

rnd = random()
print(rnd)
if rnd > 0.666666:
    com = "가위"
elif rnd > 0.333333:
    com = "바위"
else:
    com = "보"
res = "";

if me == com:
    res = "비겻쓔"
elif (me=="가위" and com=="보") or (me=="바위" and com=="가위") or (me=="보" and com=="바위"):
    res = "이겼슈"
else:
    res = "졋슈"

print("나 : ",me)
print("컴퓨터 : ",com)
print("결과 : ",res)