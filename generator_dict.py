import random

dict_even_odd = {'even': [], 'odd': [], 'sum_even': [], 'sum_odd': []}
for x in range(10):
    digit = random.randint(1, 100)
    if digit % 2 == 0:
        dict_even_odd['even'].append(digit)
    else:
        dict_even_odd['odd'].append(digit)

print("Четные числа", dict_even_odd['even'])
print("Нечетные числа", dict_even_odd['odd'])
print("Сумма четных", sum(dict_even_odd['even']))
print("Сумма нечетных", sum(dict_even_odd['odd']))
