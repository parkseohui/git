#100까지의 자연수의 합의 제곱과 제곱의 합의 차이
sum1=0
sum2=0
for i in range(1,101):
    sum1=sum1+i

sum1=sum1**2

for i in range(1,101):
    sum2=sum2+i**2

print(sum1-sum2)

