rows, cols = [int(x) for x in input().split()]

start_end = ord('a')

for row in range(start_end, start_end + rows):
    for col in range(start_end, start_end + cols):
        print(f"{chr(row)}{chr((row + col) - start_end)}{chr(row)}", end=" ")

    print()
