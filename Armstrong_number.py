num=int(input("Enter the number you think is a amstrong number "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if num==sum:
    print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number")