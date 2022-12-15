def sum(*nums):
    sum = 0
    for n in nums:
        if str(n).isalpha():
            return print('Вы ввели не число')
        sum += n
    print("Сумма чисел: ", sum)

sum (1, 2, 3, 'g')