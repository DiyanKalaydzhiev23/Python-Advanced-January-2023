from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    left_parenthesis = parentheses.popleft()

    if left_parenthesis in "{([":
        open_parentheses.append(left_parenthesis)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + left_parenthesis}" not in "{}()[]":
            print("NO")
            break
else:
    print("YES")
