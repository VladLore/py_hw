num1 = int(input('Введите количество элементов первого набора чисел: '))
num2 = int(input('Введите количество элементов второго набора чисел: '))
arr1 = []
arr2 = []
for i in range(num1):
    arr1.append(int(input('Введите элемент первого массива: ')))
for j in range(num2):
    arr2.append(int(input('Введите элемент второго массива: ')))
arr3 = []
for i in arr1:
    if i in arr2 and i not in arr3:
            arr3.append(i)
arr3.sort()
print(arr3)