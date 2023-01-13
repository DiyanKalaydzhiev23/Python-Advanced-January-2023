from collections import deque

bullet_price = int(input())
mag_max = int(input())

bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])

reward = int(input())

mag = mag_max
bullets_shot = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    mag -= 1
    bullets_shot += 1

    if mag == 0 and bullets:
        mag = mag_max if len(bullets) > mag_max else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs((bullets_shot * bullet_price) - reward)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
