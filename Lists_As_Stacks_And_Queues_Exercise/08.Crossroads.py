from collections import deque

green_window = int(input())
free_window = int(input())
total_cars = 0
cars = deque()
info = input()

while info != "END":
    if info != "green":
        cars.append(info)
    else:
        current_green = green_window

        while current_green > 0 and cars:
            car = cars.popleft()

            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1

    info = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
