from random import random

def getHollJJack():
    rnd = random()
    res = ""
    if rnd >0.5:
        res = "홀"
    else:
        res = "짝"
    return res
        
com = getHollJJack()
print("computer",com)