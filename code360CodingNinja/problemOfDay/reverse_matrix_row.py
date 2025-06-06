def ninjaCity(mat):
    # Reverse each row
    for row in mat:
        print(row)
        row.reverse()
    return mat

print(ninjaCity([
    [1, 4],
    [2, 4],
]))