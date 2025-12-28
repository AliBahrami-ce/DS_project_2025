
rowsandcols = int(input())

row_list = []
col_list = []
val_list = []

count = 0

for i in range(rowsandcols):
    for j in range(rowsandcols):
        x = int(input())

        if x != 0:
            row_list += [i]
            col_list += [j]
            val_list += [x]
            count += 1


for i in range(rowsandcols):
    for j in range(rowsandcols):

        value = 0
        for k in range(count):
            if row_list[k] == i and col_list[k] == j:
                value = val_list[k]
                break

        print(value)

    print()
