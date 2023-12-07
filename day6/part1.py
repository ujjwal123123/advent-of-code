max_times = list(map(int, input().split(":")[1].split()))
records = list(map(int, input().split(":")[1].split()))

ans = 1

for max_time, record in zip(max_times, records):
    beat_count = 0

    for accel_time in range(1, max_time):
        if accel_time * (max_time - accel_time) > record:
            beat_count += 1

    ans *= beat_count

print(ans)
