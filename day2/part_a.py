from sys import stdin

valid_indices: list[int] = []

max_red, max_green, max_blue = 12, 13, 14

for line in stdin:
    index = int(line.split(":")[0][5:])

    draws: list[list[str]] = [
        d.strip().split(", ") for d in line.split(":")[1].split(";")
    ]

    red, green, blue = 0, 0, 0

    for draw in draws:
        for color_count in draw:
            count, color = color_count.split(" ")
            count = int(count)

            if color == "red":
                red = max(red, count)
            elif color == "green":
                green = max(green, count)
            elif color == "blue":
                blue = max(blue, count)

    if red <= max_red and green <= max_green and blue <= max_blue:
        valid_indices.append(index)

print(sum(valid_indices))
