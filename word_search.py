import numpy as np

matrix = np.array((['a', 'b', 'c', 'd', 'e', 'f'],
                   ['a', 'h', 'i', 'j', 'k', 'l'],
                   ['a', 'b', 'c', 'c', 'd', 'e'],
                   ['b', 'b', 'c', 'u', 'v', 'x'],
                   ['c', 'd', 'd', 'w', 'w', 'w']))
input_string = 'abc'
row_len, col_len = matrix.shape
MAX_FREQ = 0


def check_string(in_str):
    print(in_str)
    if in_str == input_string:
        return 1
    else:
        return 0


def concat_list_char(i, j, in_adjacent_list):
    row_len, col_len = matrix.shape
    if i + len(input_string) > row_len:
        pass
    if j + len(input_string) > row_len:
        pass
    


for i in range(row_len):
    for j in range(col_len):
        # print(matrix[i][j])
        if matrix[i][j] == input_string[0]:
            temp_string = matrix[i][j]
            # print(temp_string)
            MAX_FREQ += check_string(temp_string)
            temp_string = matrix[i][j:j + 3]
            MAX_FREQ += check_string(temp_string)
print(MAX_FREQ)
