max_time = int(input().split(":")[1].replace(" ", ""))
record = int(input().split(":")[1].replace(" ", ""))

cannot_beat = 0

for accel_time in range(1, max_time):
    if accel_time * (max_time - accel_time) <= record:
        cannot_beat += 1
    else:
        break

for accel_time in range(max_time - 1, 0, -1):
    if accel_time * (max_time - accel_time) <= record:
        cannot_beat += 1
    else:
        break


print(max_time - cannot_beat - 1)
