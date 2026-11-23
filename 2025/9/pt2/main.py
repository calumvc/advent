from enum import Enum

def main():
    with open("puzz") as f:
        reds = [list(map(int, line.split(","))) for line in f.read().splitlines()]

    reds = coordify(reds)

    edges = edgeify(reds)

    # for edge in edges:
    #     print_edge(edge)

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

def floorplan(reds: list[coord], edges: list[edge]) -> float:
    largest = float('-inf')

    for i in range(0, len(reds)):
        for j in range(i + 1, len(reds)):

            tl = coord((min(reds[i].x, reds[j].x)), min(reds[i].y, reds[j].y))
            tr = coord((max(reds[i].x, reds[j].x)), min(reds[i].y, reds[j].y))
            bl = coord((min(reds[i].x, reds[j].x)), max(reds[i].y, reds[j].y))
            br = coord((max(reds[i].x, reds[j].x)), max(reds[i].y, reds[j].y))

            area = (max(reds[i].x, reds[j].x) - min(reds[i].x, reds[j].x) + 1) * (max(reds[i].y, reds[j].y) - min(reds[i].y, reds[j].y) + 1)

            if area > largest:

                print(f"Trying, area = {area} coords = ({reds[i].x, reds[i].y}{reds[j].x, reds[j].y})")

                bad = False
                for k in range(0, len(edges)):

                    foundges = [edge_corner(edges[k], tl), edge_corner(edges[k], tr), edge_corner(edges[k], bl), edge_corner(edges[k], br)]
                    print(foundges)

                    for foundge in foundges:
                        if foundge == "A":
                            if edges[k].direction == direction.HORIZONTAL:
                                if edges[k].b.x < max(tl.x, br.x) and edges[k].b.x > min(tl.x, br.x):
                                    print_edge(edges[k])
                                    print("BAD")
                                    bad = True

                            else: 
                                if edges[k].b.y < max(tl.y, br.y) and edges[k].b.y > min(tl.y, br.y):
                                    print_edge(edges[k])
                                    print("BAD")
                                    bad = True

                        if foundge == "B":
                            if edges[k].direction == direction.HORIZONTAL:
                                if edges[k].b.x < max(tl.x, br.x) and edges[k].a.x > min(tl.x, br.x):
                                    print_edge(edges[k])
                                    print("BAD")
                                    bad = True

                            else: 
                                if edges[k].b.y < max(tl.y, br.y) and edges[k].a.y > min(tl.y, br.y):
                                    print_edge(edges[k])
                                    print("BAD")
                                    bad = True

                if bad != True:
                    largest = area

    return largest

if __name__ == '__main__':
    main()
