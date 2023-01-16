first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)

    if command == "Add First":
        [first.add(int(el)) for el in data]
    elif command == "Add Second":
        [second.add(int(el)) for el in data]
    elif command == "Remove First":
        [first.discard(int(n)) for n in data]
    elif command == "Remove Second":
        [second.discard(int(n)) for n in data]
    else:
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
