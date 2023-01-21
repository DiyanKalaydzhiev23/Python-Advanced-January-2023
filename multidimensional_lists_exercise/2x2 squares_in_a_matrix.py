rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for row in range(int(rows))]

equal_blocks = 0

for row in range(rows-1):
    for i in range(columns - 1):
        symbol = matrix[row][i]

        if matrix[row][i+1] == symbol and matrix[row+1][i] == symbol and matrix[row+1][i+1] == symbol:
            equal_blocks += 1

print(equal_blocks)
