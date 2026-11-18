

def main() -> int: 
    with open("puzzle") as f:
        junctions = [list(map(int, line.split(","))) for line in f.read().splitlines()]

    return junctionate(junctions)


def junctionate(juncs: list[list[int]]) -> int:
    circuits = []
    closeness = [[0] * len(juncs) for _ in range(len(juncs))]
    connected = [[0] * len(juncs) for _ in range(len(juncs))]

    for i in range(0, len(juncs)):
        for j in range(0, len(juncs)):
           closeness[i][j] = fdot(juncs[i], juncs[j])

    print(closeness)
    print("Closeness done")

    for i in range(0, 999):
        if i % 50 == 0: 
            print(f"50 DONE, {999-i} to go")
            print(len(circuits))

        closest = float("inf")
        closest_juncs = tuple([juncs[i], juncs[i]])

        for j in range(0, len(juncs)):
            for k in range(j, len(juncs)):
                skip = False

                if j == k:
                    continue

                # for m in range(len(circuits)): # if connection already exists
                if connected[j][k] == True or connected[k][j] == True:
                    continue

                close = closeness[j][k]

                if close < closest:
                    closest = close
                    closest_juncs = tuple([j, k])

        circ_a = closest_juncs[0]
        circ_a_circ = -1
        circ_b = closest_juncs[1]
        circ_b_circ = -1

        # connected[circ_a][circ_b] = True

        print(circ_a, circ_b)
        a_not_found = True
        b_not_found = True 

        for n in range(len(circuits)): # if circuit is already found
            if circ_a in circuits[n]:
                circ_a_circ = n
                a_not_found = False 

            if circ_b in circuits[n]:
                circ_b_circ = n
                b_not_found = False

            if a_not_found == False and b_not_found == False:
                break

        # print(f"Circ a {circ_a_circ} circ b {circ_b_circ}")

        if circ_a_circ == -1:
            circuits.append([circ_a])
            # print(f"len {len(circuits)}")
            circ_a_circ = len(circuits)-1

        if circ_b_circ == -1:
            circuits.append([circ_b])
            # print(f"len {len(circuits)}")
            circ_b_circ = len(circuits)-1

        for a in range(0, len(circuits[circ_a_circ])):
            for b in range(0, len(circuits[circ_b_circ])):
                connected[circuits[circ_a_circ][a]][circuits[circ_b_circ][b]] = True

        # print(circuits)

        if circ_a_circ == circ_b_circ:
            continue 

        circuits[circ_a_circ] += circuits[circ_b_circ]
        circuits.pop(circ_b_circ)

        total = juncs[circ_a][0] * juncs[circ_b][0]
        print(total)


    print(circuits)
    print(len(circuits))
    

    #
    # big_three = []
    #
    # for y in range(0, 3):
    #     max = float("-inf")
    #     max_i = 0
    #
    #     for z in range(0, len(circuits)):
    #         if len(circuits[z]) > max:
    #             max_i = z
    #             max = len(circuits[z])
    #
    #     circuits.pop(max_i)
    #     big_three.append(max)
    #
    # total = big_three[0] * big_three[1] * big_three[2] 

    return total


def fdot(a: list[int], b: list[int]) -> int:
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)


if __name__ == "__main__":
    print(main())
