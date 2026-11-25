from enum import Enum

def main():
    with open("puzzle") as f:
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
    def __init__(self, tl: coord, tr: coord, bl: coord, br: coord, area: int, valid_edges = []) -> None:
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br
        self.area = area
        self.valid_edges = valid_edges

    def init_cast(self, edges: list[edge]) -> None:
        valid = []
        for edge in edges: # do we intersect with any vertical lines
            if edge.a.x < self.bl.x and edge.a.x < self.br.x:
                continue

            if edge.b.x < self.bl.x and edge.b.x < self.br.x:
                continue

            valid.append(edge)

        self.valid_edges = valid

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

def get_edges(r: rect) -> list[edge]:
    edges = []

    edges.append(edge(r.tl, r.bl, direction.VERTICAL))
    edges.append(edge(r.tr, r.br, direction.VERTICAL))

    return edges

def ray_cast(p: coord, r: rect) -> bool:
    # iterate over vertical lines going and count intersections
    intersections = 0

    for edge in r.valid_edges: # do we intersect with any vertical lines
        if (p.x < edge.a.x) and p.y < max(edge.a.y, edge.b.y) and p.y >= min(edge.a.y, edge.b.y):
            intersections += 1

    if intersections % 2 == 0: return False

    return True

def sort_rects(l: list[rect]) -> list[rect]:
    l.sort(key = lambda x: x.area, reverse = True)
    
    return l

def floorplan(reds: list[coord], edges: list[edge]) -> float:
    largest = float('-inf')

    print("--Checking rects--")

    lenr = len(reds)

    rects = []

    for i in range(0, lenr):
        for j in range(i + 1, lenr):

            red_a = reds[i]
            red_b = reds[j]

            area = (max(red_a.x, red_b.x) - min(red_a.x, red_b.x) + 1) * (max(red_a.y, red_b.y) - min(red_a.y, red_b.y) + 1)

            tl = coord((min(red_a.x, red_b.x)), min(red_a.y, red_b.y))
            tr = coord((max(red_a.x, red_b.x)), min(red_a.y, red_b.y))
            bl = coord((min(red_a.x, red_b.x)), max(red_a.y, red_b.y))
            br = coord((max(red_a.x, red_b.x)), max(red_a.y, red_b.y))

            r = rect(tl, tr, bl, br, area)

            rects.append(r)

    r = sort_rects(rects)

    for r in rects:
        if r.area > 1429999999:
            continue
        print(f"New rect -> {r.area}")

        if r.area <= largest:
            continue

        r.init_cast(edges)

        bad = False

        for k in range(r.tl.x + 1, r.br.x - 1): # the row below the top row
            if ray_cast(coord(k, r.tl.y + 1), r) == False:
                bad = True
                break
        
        if bad == True:
            continue

        for l in range(r.bl.x + 1, r.br.x - 1): # the row above the bottom row
            if ray_cast(coord(l, r.br.y - 1), r) == False:
                bad = True
                break

        if bad == True:
            continue

        for m in range(r.tl.y + 1, r.br.y - 1): # the row above the bottom row
            if ray_cast(coord(r.tl.x + 1, m), r) == False:
                bad = True
                break

        if bad == True:
            continue

        for n in range(r.tr.y + 1, r.br.y - 1): # the row above the bottom row
            if ray_cast(coord(r.tr.x - 1, n), r) == False:
                bad = True
                break

        if bad == True:
            continue

        return r.area

    return -1 

if __name__ == '__main__':
    main()

# answer > 129411462 unless code is wrong
# 224891505 
# 328493280
# 771940415
