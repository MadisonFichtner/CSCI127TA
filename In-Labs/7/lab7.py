def print_header(columns):
    line = "+"
    for _ in range(columns):
        line += "---+"
    print(line)

def print_matrix(matrix, nrow, ncol, name):
    print(name, end='\n\n') # print matrix's name

    # top row separator
    print('+', end='')
    for col in range(ncol):
        print('---+', end='')

    # print row values
    for row in range(nrow):
        print('\n|', end='')
        for col in range(ncol):
            val = 0 # the value to print out
            if (row, col) in matrix: # if we have an entry in the matrix, we know it is non-zero and must be set
                val = matrix[(row, col)]

            print(str(val).rjust(3), end='|') # print the value at (row,col) with a column separator afterward
        # print row separator
        print('\n+', end='')
        for col in range(ncol):
            print('---+', end='')
    print('\n')

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# subtract matrices returns the result of subtracting m2 from m1
def subtract_matrices(m1, m2, nrow, ncol):
    mres = {}
    for row in range(nrow):
        for col in range(ncol):
            v1 = 0
            v2 = 0
            if (row, col) in m1:
                v1 = m1[(row, col)]
            if (row, col) in m2:
                v2 = m2[(row, col)]

            res = v1 - v2
            if res != 0:
                mres[(row, col)] = res
    return mres


def main (file_name):
    input_file = open(file_name, "r")

    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")

    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = subtract_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 - Matrix 2")
    print("Matrix 3 =", matrix_3)

main ("sparse-matrix.txt")
