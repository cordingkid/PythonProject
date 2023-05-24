# 첫 수 입력
# 끝수 입력

first = int(input("구구단 출력할 단 수를 입력하세요"))

arr = list(range(1,9+1))

for i in arr:
    print("{} x {} = {}".format(first,i,first*i))
    

