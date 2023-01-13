from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)

numbers.reverse()

print(*numbers, sep=", ")
