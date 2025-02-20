num = int(input("Enter the number you think is an Armstrong number: "))
sum = 0
temp = num
n = len(str(num))  # Number of digits in the number

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** n)
    temp = temp // 10

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

