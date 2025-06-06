def matrix_multiply(mat1, mat2):
    r1 = len(mat1)
    c1 = len(mat1[0])
    r2 = len(mat2)
    c2 = len(mat2[0])
    if c1 != r2:
        print("Invalid Input")
        return None

    # Initialize the result matrix with zeros
    res = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j]+= mat1[i][k]* mat2[k][j]
    return res
print(matrix_multiply([
    [2, 1, 4],
    [2, 7, 4],
],[
    [1, 4],
    [2, 4],
    [3, 5]
]))