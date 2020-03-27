def print_result(matrix):
    print("The result is:")
    if type(matrix[0][0]) != str:
        matrix_str = []
        row = 0
        for i in matrix:
            matrix_str.append([])
            for j in range(len(i)):
                matrix_str[row].append(str(matrix[row][j]))
            row += 1
        for i in matrix_str:
            print(" ".join(i))
    else:
        for i in matrix:
            print(" ".join(i))

def matrix_size(command):

    if command == "2_matrix":
        A_dimensions = [int(n) for n in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        A = [[float(n) for n in input().split()] for k in range(A_dimensions[0])]
        B_dimensions = [int(n) for n in input("Enter size of second matrix: ").split()]
        print("Enter second matrix:")
        B = [[float(n) for n in input().split()] for k in range(B_dimensions[0])]

        return A_dimensions, A, B_dimensions, B

    elif command == "matrix_const":
        A_dimensions = [int(n) for n in input("Enter size of matrix: ").split()]
        print("Enter matrix")
        A = [[float(n) for n in input().split()] for k in range(A_dimensions[0])]
        constant = float(input("Enter constant: "))

        return A_dimensions, A, constant

    elif command == "1_matrix":
        A_dimensions = [int(n) for n in input("Enter size of matrix: ").split()]
        print("Enter matrix")
        A = [[float(n) for n in input().split()] for k in range(A_dimensions[0])]

        return A_dimensions, A

def add_mat(A_dimensions, A, B_dimensions, B):

    if A_dimensions == B_dimensions:
        result = []
        for i in range(A_dimensions[0]):
            lst = []
            for j in range(A_dimensions[1]):
                lst.append(str(A[i][j] + B[i][j]))
            result.append(lst)
        print_result(result)
    else:
        print("ERROR")
    print()


def mult_const(A_dimensions, A, constant):

    result = []
    for i in range(A_dimensions[0]):
        lst = []
        for j in range(A_dimensions[1]):
            lst.append(str(A[i][j] * constant))
        result.append(lst)
    print_result(result)

def mult_mat(A_dimensions, A, B_dimensions, B):

    result = []

    for row in range(A_dimensions[0]):
        lst = []
        for column in range(B_dimensions[1]):
            dot_product = 0
            for i in range(A_dimensions[1]):
                dot_product += A[row][i]*B[i][column]
            lst.append(str(dot_product))
        result.append(lst)

    print_result(result)

def transp_main_diag(A_dimensions, A):

    result = []
    for i in range(A_dimensions[1]):
        result.append([])
    for i in range(A_dimensions[0]):
        for j in range(A_dimensions[1]):
            result[j].append(A[i][j])

    return result

def transp_side_diag(A_dimensions, A):

    result = []
    for i in range(A_dimensions[1]):
        result.append([])
    for i in range(A_dimensions[0]-1, -1, -1):
        row = 0
        for j in range(A_dimensions[1]-1, -1, -1):
            result[row].append(str(A[i][j]))
            row += 1

    print_result(result)

def transp_vert_line(A_dimensions, A):

    result = []
    for i in range(A_dimensions[1]):
        result.append([])
    for i in range(A_dimensions[0]):
        for j in range(A_dimensions[1]-1, -1, -1):
            result[i].append(str(A[i][j]))

    print_result(result)

def transfp_horizont_line(A_dimensions, A):

    result = []
    row = 0
    for i in range(A_dimensions[0]-1, -1, -1):
        result.append([])
        for j in range(A_dimensions[1]):
            result[row].append(str(A[i][j]))
        row += 1

    print_result(result)

def determinant(dimensions, matrix):
    result = 0
    if dimensions == [2, 2]:
        result = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return result
    elif dimensions == [1, 1]:
        return matrix[0][0]
    else:
        for i in range(dimensions[0]):
            dimensions_new = []
            matrix_new = []

            for index in dimensions:
                dimensions_new.append(index - 1)

            for row in range(1, dimensions[0]):
                lst = []
                for column in range(dimensions[0]):
                    if column != i:
                        lst.append(matrix[row][column])
                matrix_new.append(lst)

            result += matrix[0][i] * pow((-1), (1 + i + 1)) * determinant(dimensions_new, matrix_new)
        return result


def inverse_matrix(dimensions, matrix):
    det_A = determinant(dimensions, matrix)
    if det_A == 0:
        return "Inverse matrix doesn't exists"

    adjust_A = []
    dimensions_new = []
    for index in dimensions:
        dimensions_new.append(index - 1)

    for i in range(dimensions[0]):
        adjust_A.append([])
        for j in range(dimensions[1]):
            matrix_new = []

            for row in range(dimensions[0]):
                if row != i:
                    lst = []
                    for column in range(dimensions[1]):
                        if column != j:
                            lst.append(matrix[row][column])
                    matrix_new.append(lst)
            adjust_A[i].append(pow((-1),(i + 1 + j +1)) * determinant(dimensions_new, matrix_new))

    return mult_const(dimensions, transp_main_diag(dimensions, adjust_A), (1/det_A))

command = 1
while command != 0:
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    command = int(input("Your choice: "))

    if command == 1:
        a_dim, a, b_dim, b = matrix_size("2_matrix")
        add_mat(a_dim, a, b_dim, b)
    elif command == 2:
        a_dim, a, const = matrix_size("matrix_const")
        mult_const(a_dim, a, const)
    elif command == 3:
        a_dim, a, b_dim, b = matrix_size("2_matrix")
        mult_mat(a_dim, a, b_dim, b)
    elif command == 4:
        print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        transp_command = int(input("Your choice: "))
        a_dim, a = matrix_size("1_matrix")
        if transp_command == 1:
            print_result(transp_main_diag(a_dim, a))
        elif transp_command == 2:
            transp_side_diag(a_dim, a)
        elif transp_command == 3:
            transp_vert_line(a_dim, a)
        elif transp_command == 4:
            transfp_horizont_line(a_dim, a)
    elif command == 5:
        a_dim, a = matrix_size("1_matrix")
        print(determinant(a_dim, a))
    elif command == 6:
        a_dim, a = matrix_size("1_matrix")
        inverse_matrix(a_dim, a)
