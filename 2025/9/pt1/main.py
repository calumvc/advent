
def main():
    with open("puzzle") as f:
        reds = [list(map(int, line.split(","))) for line in f.read().splitlines()]


    print(floorplan(reds))

def floorplan(reds: list[list[int]]) -> float:

    largest = float("-inf")

    for i in range(0, len(reds)):
        for j in range(i + 1, len(reds)):

            area = (max(reds[i][0], reds[j][0]) - min(reds[i][0], reds[j][0]) + 1) * (max(reds[i][1], reds[j][1]) - min(reds[i][1], reds[j][1]) + 1)

            if area > largest:
                largest = area

    return largest


if __name__ == '__main__':
    main()
