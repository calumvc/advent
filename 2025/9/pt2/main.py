from enum import Enum

def main():
    with open("puzz") as f:
        reds = [list(map(int, line.split(","))) for line in f.read().splitlines()]

    reds = coordify(reds)

    edges = edgeify(reds)

    print(floorplan(reds, edges))

class coord():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class direction(Enum):
    HORIZONTAL = 1
    VERTICAL = 2

class edge():
    def __init__(self, a: coord, b:coord, direction: direction) -> None:
        self.a = a
        self.b = b
        self.direction = direction

class rect():
    def __init__(self, tl: coord, tr: coord, bl: coord, br: coord, area: int) -> None:
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br
        self.area = area

def coordify(reds:list[list[int]]) -> list[coord]:
    new_reds = []

    for i in range(len(reds)):
        new_reds.append(coord(reds[i][0], reds[i][1]))

    return new_reds

def edgeify(reds:list[coord]) -> list[edge]:
    edges = []
    for i in range(0, len(reds)-1):
        e = edge(coord(reds[i].x, reds[i].y), coord(reds[i+1].x, reds[i+1].y), direction.HORIZONTAL if abs(reds[i].x - reds[i+1].x) != 0 else direction.VERTICAL)
        edges.append(e)

    edges.append(edge(coord(reds[-1].x, reds[-1].y), coord(reds[0].x, reds[0].y), direction.HORIZONTAL if abs(reds[-1].x - reds[0].x) != 0 else direction.VERTICAL))

    return edges

def print_edge(edge: edge) -> None:
    print(f"Edge from {(edge.a.x, edge.a.y)} to {(edge.b.x, edge.b.y)} {edge.direction.name}")

def edge_corner(edge: edge, point: coord) -> str:
    if edge.a.x == point.x and edge.a.y  == point.y:
        return "A"

    if edge.b.x == point.x and edge.b.y == point.y:
        return "B" 

    return "N"

def get_edges(r: rect) -> list[edge]:
    edges = []

    edges.append(edge(r.tl, r.tr, direction.HORIZONTAL))
    edges.append(edge(r.bl, r.br, direction.HORIZONTAL))
    edges.append(edge(r.tl, r.bl, direction.VERTICAL))
    edges.append(edge(r.tr, r.br, direction.VERTICAL))

    return edges

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

def intersection(p: coord, edge: edge) -> bool: 
    line = linify((edge.a, edge.b))

    # print("NEW INT-----------")
    # print(f" X {p.x} Y {p.y}")
    # print(f"A X {edge.a.x} Y {edge.a.y}")
    # print(f"B X {edge.b.x} Y {edge.b.y}")

    count = 0
    for i in range(0, len(line)):
        if p.x == line[i].x and p.y == line[i].y:
            count += 1
        
    if count == 1:
        # print("INT")
        return True
   
    return False

def ray_cast(p: coord, edges: list[edge], r: rect) -> bool: # not even raycasting
    hoz = []
    ver = []

    for edge in edges:
        if edge.direction == direction.HORIZONTAL:
            hoz.append(edge)
        else:
            ver.append(edge)

    # iterate over both horizontal and vertical ones going both ways and count intersections
    l_intersections = 0
    r_intersections = 0
    for i in range(0, len(ver)): # do we intersect with any vertical lines

        for j in range(p.x, r.br.x + 1):
            # print(j)
            # print(r.br.x)
            if intersection(coord(j, p.y), ver[i]):
                r_intersections += 1

        for j in range(r.tl.x - 1, p.x):
            if intersection(coord(j, p.y), ver[i]):
                l_intersections += 1

    # print(f"L {l_intersections}")
    # print(f"R {r_intersections}")

    if l_intersections % 2 == 0 and l_intersections > 0:
        return False

    if r_intersections % 2 == 0 and r_intersections > 0:
        return False

    u_intersections = 0
    d_intersections = 0

    for i in range(0, len(hoz)): # do we intersect with any horizontal lines

        for j in range(p.y, r.br.y + 1):
            if intersection(coord(p.x, j), ver[i]):
                d_intersections += 1

        for j in range(r.tl.y - 1, p.y):
            if intersection(coord(p.x, j), ver[i]):
                u_intersections += 1

    # print(f"U {u_intersections}")
    # print(f"D {d_intersections}")

    if d_intersections % 2 == 0 and d_intersections > 0:
        return False

    if u_intersections % 2 == 0 and u_intersections > 0:
        return False

    return True

def floorplan(reds: list[coord], edges: list[edge]) -> float:
    largest = float('-inf')

    # print(ray_cast(coord(4, 4), edges, rect(coord(2, 3), coord(7, 3), coord(2, 5), coord(7, 5), 9))) # should print true
    # print(ray_cast(coord(5, 6), edges, rect(coord(2, 3), coord(7, 3), coord(2, 5), coord(7, 5), 9))) # should print true
    # print(ray_cast(coord(11, 11), edges, rect(coord(2, 3), coord(7, 3), coord(2, 5), coord(7, 5), 9))) # should print true
    # print(ray_cast(coord(3, 2), edges, rect(coord(2, 1), coord(11, 1), coord(2, 5), coord(11, 5), 9))) # should print true
    # print(ray_cast(coord(4, 4), edges, rect(coord(2, 1), coord(11, 1), coord(2, 5), coord(11, 5), 9))) # should print true

    for i in range(0, len(reds)):
        for j in range(i + 1, len(reds)):

            tl = coord((min(reds[i].x, reds[j].x)), min(reds[i].y, reds[j].y))
            tr = coord((max(reds[i].x, reds[j].x)), min(reds[i].y, reds[j].y))
            bl = coord((min(reds[i].x, reds[j].x)), max(reds[i].y, reds[j].y))
            br = coord((max(reds[i].x, reds[j].x)), max(reds[i].y, reds[j].y))

            area = (max(reds[i].x, reds[j].x) - min(reds[i].x, reds[j].x) + 1) * (max(reds[i].y, reds[j].y) - min(reds[i].y, reds[j].y) + 1)

            print(f"4 corners: TL - {tl.x, tl.y} - TR - {tr.x, tr.y} - BL - {bl.x, bl.y} - BR - {br.x, br.y}")

            r = rect(tl, tr, bl, br, area)

            if r.area > largest:

                bad = False

                for k in range(r.tl.x, r.br.x):
                    for l in range(r.tl.y, r.br.y):
                        if ray_cast(coord(k, l), edges, r) == False: # the only things passing this are direct lines
                            bad = True
                            break

                if bad == False:
                    largest = r.area

    return largest

if __name__ == '__main__':
    main()
