package main

import (
	"bufio"
	"math"
	"os"
	// "strconv"
	// "strings"
)

type Beam struct {
	x, y int
}

func main(){

	f, _ := os.Open("puzzle")

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var arr = make([]string, 0)

	for scanner.Scan(){
		arr = append(arr, scanner.Text())
	}

	// taquito(arr)
	// graph := taquito(arr)
	graph := taquito(arr)
	// graph = graph
	// print(traverse(graph))
	print(traverse2(graph))
}

func taquito(arr []string) [][]byte {
	total := 0
	beams := []Beam{}
	graph := make([][]byte, len(arr))
	// realities := 0

	for g := 0; g < len(graph); g++ {
		graph[g] = make([]byte, len(arr[0]))
	}
	for i := 0; i < len(arr); i++ { // loop through each line
		for j := 0; j < len(arr[i]); j++ { // loop through every char
			if string(arr[i][j]) == "S" {
				beams = append(beams, Beam{ x: j, y: i + 1 })
			}

			if string(arr[i][j]) == "^" {
				graph[i][j] = '^'
				for k := 0; k < len(beams); k++ {

					if beams[k].x == j && beams[k].y == i - 1 { // if the beam if split

						total++ // increment splits

						beams = append(beams[:k], beams[k+1:]...) // remove old beam
						// realities += 2
						
						lfine := true // checking if the left isnt already there
						rfine := true // same with right

						for m := 0; m < len(beams); m++ {
							if (beams[m].x == j - 1 && beams[m].y == i) || (beams[m].x == j - 1 && beams[m].y == i - 1) {
								lfine = false
							}
							if (beams[m].x == j + 1 && beams[m].y == i) || (beams[m].x == j + 1 && beams[m].y == i - 1) {
								rfine = false
							}
						}
						
						if lfine == true { // if the left is free
							beams = append(beams, Beam{ x: j - 1, y: i })
						}
						if rfine == true { // if the right is free
							beams = append(beams, Beam{ x: j + 1, y: i })
						}

						// if lfine == false && rfine == false { realities--; }
					}
				}
			}
		}

		for l := 0; l < len(beams); l++ {
			if beams[l].y == i - 1 { beams[l].y++ } // increment beam if it hasn't been split and is on the old level
		}

		for n := 0; n < len(arr[i]); n++ { // store tree line by line
			beamfound := false
			for l := 0; l < len(beams); l++ {
				if n == beams[l].x { beamfound = true; graph[i][n] = '|' }
			}
			if beamfound != true && graph[i][n] != '^' { graph[i][n] = '.' }
		}
	}

	for p := 0; p < len(graph); p++ { // print stored graph
		for q := 0; q < len(graph[p]); q++ {
			print(string(graph[p][q]))
		}
		println()
	}
	// print("realities -> ", realities)
	return graph
}

func traverse(graph [][]byte) int {
	realities := 0
	height := len(graph)
	println("height is i think -> ", height)

	totalsplits := int(math.Pow(2, float64((height/2)-1)))
	println(totalsplits)
	realities = totalsplits

	for i := 0; i < height; i += 2 {
		splitcount := 0
		for j := 0; j < len(graph[i]); j++ {
			print(string(graph[i][j]))
			if graph[i][j] == '^' { splitcount++; }
		}

		missingsplits := (i/2) - splitcount
		println(" missing splits -> ", missingsplits)

		missingrealities := missingsplits * int(math.Pow(2, float64(height-i)/2))

		realities -= missingrealities
		println()
	}

	return realities
}

func traverse2(graph [][]byte) int {
	realities := 0
	totals := [10000]int{}
	found_start := false

	for i := 0; i < len(graph); i++ { // loop through levels

		if !found_start {
			for j := 0; j < len(graph[i]); j++ {
				if graph[i][j] == '|' {
					totals[j] = 1
					found_start = true
					break
				}
			}
		}

		if i+1 == len(graph) { // bottom of tree
			break
		}

		for j := 0; j < len(graph[i]); j++ { // loop through each part of tree

			if graph[i][j] == '|' && graph[i+1][j] == '^' { 
				println("one split found ", i, " ", j, totals[j])
				totals[j-1] += totals[j] 
				totals[j+1] += totals[j]
				totals[j] = 0
			}
		}
	}

	for i := range totals {
		realities += totals[i]
	}

	return realities
}

// pt1
// 1518 >

// pt2
// 3030 <
// 3032 <
// 2788 <


// OK 
// every level on a full tree adds n^2 possibilities 
// every time it misses a splitted it loses 2 possibilties from that 
// missing splitters at a higher level are worth more, also by n^2 so the if the one above is missing then 4 possibilities are missing
// so you can probably work down the tree subtracting that amount from the total amount of possibilities

// done
