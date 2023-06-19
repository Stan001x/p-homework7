a = 1

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows +1):
        print(sep='/n')
        for j in range(1, num_columns +1):
            a = operation(i,j)
            print(a, end=' ')

print(print_operation_table(lambda x, y: x * y))