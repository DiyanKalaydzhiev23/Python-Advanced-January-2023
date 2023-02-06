matrix = [
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9],  # 2
]

index = int(input())

if 0 <= index < len(matrix):
    print(matrix[index])