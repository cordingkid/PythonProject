# range를 이용하여 1에서 10까지 합을 구하시오

mylist = list(range(1,10+1))
print(mylist)


sum = 0
for i in mylist:
    sum += i
    
print("sum",sum)