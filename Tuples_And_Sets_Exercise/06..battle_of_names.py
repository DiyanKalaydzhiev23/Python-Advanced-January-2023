odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(l) for l in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.union(even_set), sep=", ")
