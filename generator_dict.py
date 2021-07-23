import random

list_01 = []
list_02 = []
for x in range(10):
    digit = random.randint(1, 100)
    if digit % 2 == 0:
        list_01.append(digit)
    else:
        list_02.append(digit)

dict_even_odd = {'even': list_01, 'odd': list_02, 'sum_even': sum(list_01), 'sum_odd': sum(list_02)}

print("Четные числа", dict_even_odd['even'])
print("Нечетные числа", dict_even_odd['odd'])
print("Сумма четных", dict_even_odd['sum_even'])
print("Сумма нечетных", dict_even_odd['sum_odd'])