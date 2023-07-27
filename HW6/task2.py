arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_value = 2
max_value = 8
index = [i for i, x in enumerate(arr) if x >= min_value and x <= max_value]
print(index)