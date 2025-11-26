first_number = int(input('Введите первое число - A: '))
second_number = int(input('Введите второе число - B: '))

sum_even=0
sum_odd=0

for x in range (first_number, second_number +1):
    if x % 2 == 0:
        sum_even +=x
    else:
        sum_odd +=x

result=sum_even-sum_odd
print(result)
if result > 0:
    print('Сумма четных больше')
else:
    print('Сумма нечетных больше')