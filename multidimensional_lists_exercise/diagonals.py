n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary][::-1])}. Sum: {sum(secondary)}")
