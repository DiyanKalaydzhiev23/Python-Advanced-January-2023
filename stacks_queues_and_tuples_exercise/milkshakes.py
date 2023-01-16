from collections import deque
#rename it
chocolates = list(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

chocolate_milkshakes = 0

while chocolate_milkshakes != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate < 1 and cup_of_milk < 1:
        continue
    elif chocolate < 1:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk < 1:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        chocolate_milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolate -= 5
        chocolates.append(chocolate)


print('Great! You made all the chocolate milkshakes needed!') \
    if chocolate_milkshakes == 5 else print('Not enough milkshakes.')
print(f'Chocolate: {", ".join(str(x) for x in chocolates) if chocolates else "empty"}')
print(f'Milk: {", ".join(str(x) for x in cups_of_milk) if cups_of_milk else "empty"}')

