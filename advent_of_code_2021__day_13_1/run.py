import os


def fold_by_x(data_matrix, input_x):
    # split matrix
    folding_matrix = []
    back_matrix = []
    new_matrix = []

    for data_matrix_row in data_matrix:
        i = 0
        temp_folding_row = []
        temp_back_row = []
        for data_matrix_col in data_matrix_row:
            if i >= input_x:
                temp_folding_row.append(data_matrix_col)
            else:
                temp_back_row.append(data_matrix_col)
            i += 1

        temp_folding_row.pop(0)
        folding_matrix.append(temp_folding_row)
        back_matrix.append(temp_back_row)

    folding_matrix_height = len(folding_matrix)
    folding_matrix_width = len(folding_matrix[0])

    for folding_matrix_y in range(0, folding_matrix_height):
        new_matrix.append([])
        for folding_matrix_x in range(0, folding_matrix_width):
            if back_matrix[folding_matrix_y][folding_matrix_x] or folding_matrix[folding_matrix_y][folding_matrix_width-1-folding_matrix_x]:
                new_matrix[folding_matrix_y].append(True)
            else:
                new_matrix[folding_matrix_y].append(False)
    return new_matrix

data = []

with open(os.path.join(os.path.dirname(__file__), './matrix'), 'r') as f:
    lines = f.readlines()
    for line in lines:
        data.append([int(line.strip().split(',')[0]), int(line.strip().split(',')[1])])

width = 0
height = 0
matrix = []

# measure width, height
for row in data:
    width = max(width, row[0])
    height = max(height, row[1])

# create empty matrix
for y in range(0, height+1):
    row = []

    for x in range(0, width+1):
        row.append(False)

    matrix.append(row)

# fill matrix with data
for row in data:
    matrix[row[1]][row[0]] = True

matrix = fold_by_x(matrix, 655)

dots_count = 0

for matrix_row in matrix:
    for matrix_col in matrix_row:
        if matrix_col:
            dots_count += 1

print(dots_count)
