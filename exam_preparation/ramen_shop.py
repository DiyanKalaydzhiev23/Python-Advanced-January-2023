from collections import deque

ramen_bowls = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while customers:
    if not ramen_bowls:
        print(f"Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break

    customer = customers.popleft()
    bowl = ramen_bowls.pop()

    if customer > bowl:
        customers.appendleft(customer - bowl)
    elif customer < bowl:
        ramen_bowls.append(bowl - customer)
else:
    print(f"Great job! You served all the customers.")

    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen_bowls))}")
