
def main():
    with open("puzz") as f:
        reds = [list(map(int, line.split(","))) for line in f.read().splitlines()]

    print("--Getting reds--")
    reds = coordify(reds)

    print("--Populating graph--")
    graph = populate(reds)

    print("--Working it out--")
    print(floorplan(reds, graph))

class coord():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def coordify(reds:list[list[int]]) -> list[coord]:
    new_reds = []

    for i in range(len(reds)):
        new_reds.append(coord(reds[i][0], reds[i][1]))

    return new_reds

def populate(reds: list[coord]) -> list[list[str]]:
    greens = [[int]]
    graph = init_graph(reds)

    for i in range(0, len(reds)):
        boundaries = []

        boundaries.append(reds[i])

        if i != len(reds)-1:
            boundaries.append(reds[i+1])
            boundaries.append(reds[i-1])
        else: 
            boundaries.append(reds[0])
            boundaries.append(reds[-1])

        line = linify(tuple([boundaries[0],boundaries[1]]))

        graph = draw_graph(graph, line)


    print("--Creating outline--")
    # print_graph(graph)

    print("--Populating--")
    fill_graph(graph)
    print()
    print_graph(graph)

    return graph

def init_graph(reds: list[coord]) -> list[list[str]]:
    graph = [[]]

    max_x = 0 
    max_y = 0

    for i in range(0, len(reds)):
        if reds[i].x > max_x:
            max_x = reds[i].x
        if reds[i].y > max_y:
            max_y = reds[i].y

    for i in range(0, max_y+1):
        graph.append([" "])

        for j in range(0, max_x+1):
            graph[i].append(" ")

    return graph

def draw_graph(graph: list[list[str]], line: list[coord]) -> list[list[str]]:
    for i in range(0, len(line)):
        graph[line[i].y][line[i].x] = "#"

    return graph

def print_graph(graph: list[list[str]]) -> None:
    for i in range(0, len(graph) - 1):
        line = []
        for j in range(0, len(graph[0])):
            line.append((graph[i][j]))

        print(line)

def fill_graph(graph: list[list[str]]) -> list[list[str]]:
    for y in range(0, len(graph)-1):
        for x in range(0, len(graph[0])):
            point = coord(x, y)

            surrounded = is_surrounded(graph, point)

            if surrounded == True: 
                graph[point.y][point.x] = "#"

    return graph

def is_surrounded(graph: list[list[str]], point: coord) -> bool:
    l, r, d, u = False, False, False, False

    for i in range(point.x, len(graph[0])):
        if graph[point.y][i] == "#":
            r = True

    for i in range(0, point.x):
        if graph[point.y][i] == "#": 
            l = True

    for i in range(point.y, len(graph)-1):
        if graph[i][point.x] == "#": 
            d = True

    for i in range(0, point.y):
        if graph[i][point.x] == "#": 
            u = True

            
    if (l and r and u and d):
        return True

    return False

def linify(input: tuple[coord, coord]) -> list[coord]:
    line = []

    max_x = max(input[0].x, input[1].x)
    min_x = min(input[0].x, input[1].x)
    max_y = max(input[0].y, input[1].y)
    min_y = min(input[0].y, input[1].y)

    if max_x - min_x > max_y - min_y:
        for i in range(0, max_x - min_x + 1):
            line.append(coord(min_x + i, min_y))

    else:
        for i in range(0, max_y - min_y + 1):
            line.append(coord(min_x, min_y + i))

    return line

def printline(input: list[coord]) -> None:
    for i in range(0, len(input)):
        print(f"Coord -> [{input[i].x}, {input[i].y}]")

def floorplan(reds: list[coord], graph: list[list[str]]) -> float:

    largest = float("-inf")

    for i in range(0, len(reds)):
        for j in range(i + 1, len(reds)):
            invalid = False

            tl = coord((min(reds[i].x, reds[j].x)), min(reds[i].y, reds[j].y))
            tr = coord((max(reds[i].x, reds[j].x)), min(reds[i].y, reds[j].y))
            bl = coord((min(reds[i].x, reds[j].x)), max(reds[i].y, reds[j].y))
            br = coord((max(reds[i].x, reds[j].x)), max(reds[i].y, reds[j].y))

            # print(f"4 corners: TL - {tl.x, tl.y} - TR - {tr.x, tr.y} - BL - {bl.x, bl.y} - BR - {br.x, br.y}")

            for k in range(tl.y, bl.y+1):
                for l in range(tl.x, br.x+1):
                    if graph[k][l] != "#":
                        invalid = True

            if invalid:
                continue

            area = (max(reds[i].x, reds[j].x) - min(reds[i].x, reds[j].x) + 1) * (max(reds[i].y, reds[j].y) - min(reds[i].y, reds[j].y) + 1)

            if area > largest:
                largest = area

    return largest


if __name__ == '__main__':
    main()
