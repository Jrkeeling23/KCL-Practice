import numpy as np

"""
Finding largest cluster of ones in 2D array
"""

# Possible Directions to Search
right = np.array([0, 1])
left = np.array([0, -1])
top = np.array([-1, 0])
bottom = np.array([1, 0])
adjacent_list = [right, left, bottom, top, bottom + right, bottom + left, top + right, top + left]

MAX_CLUSTER = 0  # static variable of max size cluster found


def check_surrounding(mx, loc, in_adjacent_list, in_stack):
    """
    Searchs surrounding locations for 1's
    :param mx: matrix
    :param loc: current location
    :param adjacent_list: list of directions
    :param in_stack: stack to append to
    :return: None
    """
    in_stack.append((loc[0], loc[1]))
    for adj in in_adjacent_list:  # iterate through each possible direction
        check_max = loc + adj > np.array(mx.shape) - 1  # True or False if out of bounds
        check_min = loc + adj < 0  # True of false if out of bounds
        if bool(True) in check_max or bool(True) in check_min:  # Determines if out of bounds
            pass
        else:
            temp_loc = loc + adj  # numpy calculation for possible 1
            if mx[temp_loc[0]][temp_loc[1]] == 1:
                if (temp_loc[0], temp_loc[1]) in in_stack:  # do not append to stack if 0
                    pass
                else:
                    in_stack.append((temp_loc[0], temp_loc[1]))  # append to stack if 1


# matrix to use
matrix = np.array(([1, 0, 0, 0, 1], [0, 0, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 0]))
row_len, col_len = matrix.shape

# iterate through rows and columns
for i in range(row_len):
    for j in range(col_len):
        if matrix[i][j] == 1: # check if value is 1
            stack = []  # initalize empty list
            check_surrounding(matrix, np.array([i, j]), adjacent_list, stack)  # check surround locations
            if len(stack) > 1:  # check if there is neighboring 1's
                temp_stack = []
                for elem in stack:  # iterate through neighbors that are 1
                    check_surrounding(matrix, np.array([elem[0], elem[1]]), adjacent_list, temp_stack)
                    stack = temp_stack.copy()  # temp stack contains possible new neighbors
                stack = list(dict.fromkeys(temp_stack))  # unique locations only
                if len(stack) > MAX_CLUSTER:  # change max cluster found if need be
                    MAX_CLUSTER = len(stack)
print(MAX_CLUSTER)
