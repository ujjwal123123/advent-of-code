from sys import stdin

powers = []


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

    power = red * green * blue
    powers.append(power)


print(sum(powers))
