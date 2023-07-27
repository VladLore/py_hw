a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))
a_list = [a1]
for i in range(1, n+1):
    a_list.append(a_list[-1] + (i-1) * d)
    print("Список элементов арифметической прогрессии:", a_list)