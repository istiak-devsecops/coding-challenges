def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose(matrix)

print("Original:", matrix)
print("Transposed:", transposed)