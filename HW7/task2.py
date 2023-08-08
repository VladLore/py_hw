def print_operation_table(function, num_rows=6, num_columns=6):
    for i in range(num_rows):
        for j in range(num_columns):
            print(f"{i+1} {j+1} {function(i, j)}")
# Пример использования функции
def addsub(x, y):
    return x + y
print_operation_table(addsub, num_rows=3, num_columns=4)