# 첫 수를 입력하시오 1
# 끝수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10 까지의 5의 배수의 합은 15 입니다.

first = int(input("첫 수를 입력하세요"))
end = int(input("끝 수를 입력하세요"))
num = int(input("배수를 입력하시오"))

summ = 0;
for i in range(first,end+1):
    if i % num == 0:
        summ += i 

print("{}에서 {}까지의 {}배수의 합은 {} 입니다".format(first,end,num,summ))
        