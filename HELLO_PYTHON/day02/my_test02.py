# 첫 수 입력
# 끝수 입력

first = int(input("첫 수를 입력하세요"))
end = int(input("끝 수를 입력하세요"))

arr = list(range(first,end+1))

sum = 0;
for i in arr:
    sum+=i;
    
print("{}에서 {}까지 합은 {}입니다.".format(first,end,sum))
