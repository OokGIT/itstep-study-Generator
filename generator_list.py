import random
list_01 = []
list_02 = []
for digit in range(10):
    digit = random.randint(1,100)
    if digit %2 == 0:
        list_01.append(digit)
    else:
        list_02.append(digit)

print("Список с четными числами:", list_01)
print("Список с нечетными числами:", list_02)
print("Сумма всех четных чисел:", sum(list_01))
print("Сумма всех нечетных чисел:", sum(list_02))
print("Сумма чисел в обоих списках:", sum(list_01)+sum(list_02))


