#
# Бинарный поиск
#

new_list = []

a, b = map(int, input("Ввыедите через пробел два целых числа. Количество чисел в исходной последовательности "
                      "и количество чисел для проверки: ").split())
init_list = map(int, input("Исходная последовательность целых чисел через пробел: ").split())


for i in range(b):
    new_list.append(int(input(": ")))

for i in new_list:
    print("Yes") if i in init_list else print("No")
