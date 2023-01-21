num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]

primary_sum = 0
secondary_sum = 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[num-i-1][i]

print(abs(primary_sum-secondary_sum))
