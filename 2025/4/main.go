package main

import (
	"bufio"
	"os"
	// "strconv"
)

type Point struct {
	X, Y int

}

func main(){

	f, _ := os.Open("puzzle")

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var arr = make([]string, 0, 0)

	for scanner.Scan(){
		arr = append(arr, scanner.Text())
	}

	println(marknsweep(arr))

}

func marknsweep(arr []string) int {
	// println("Starting")
	total := 0
	tbr := []Point{}
	starting := true
	for len(tbr) > 0 || starting == true {
		starting = false
		for len(tbr) > 0 {
			row := tbr[0].X
			col := tbr[0].Y
			arr[row] = arr[row][:col] + "x" + arr[row][col+1:]
			tbr = tbr[1:]
		}
		for i := 0; i < len(arr); i++ {
				if i == 0 { // only check row below
					// println("Checking top level")
					for j := 0; j < len(arr[i]); j++ { // println("Checking a thing on top level") 
						if arr[i][j] == '@' { // '@' is ascii for @
							// println("Checking a found @")
							obs := 0
							if j == 0 { // cant reach 4
								total++; tbr = append(tbr, Point{X: i, Y: j})
							} else
							if j == len(arr[i])-1 {
								total++; tbr = append(tbr, Point{X: i, Y: j})
							} else {
								if (arr[i][j-1]) == '@' { obs++ }
								if (arr[i][j+1]) == '@' { obs++ }
								if (arr[i+1][j-1]) == '@' { obs++ }
								if (arr[i+1][j]) == '@' { obs++ }
								if (arr[i+1][j+1]) == '@' { obs++ }
								if obs < 4 { total++; tbr = append(tbr, Point{X: i, Y: j}) }
							}
						}
					}
				} else {
					if i == len(arr)-1 { // only check row above
					for j := 0; j < len(arr[i]); j++ {
						if (arr[i][j]) == '@' {
							obs := 0
							if j == 0 { // only check to the right
								total++; tbr = append(tbr, Point{X: i, Y: j})
							} else
							if j == len(arr[i])-2 { // only check to the left
								total++; tbr = append(tbr, Point{X: i, Y: j})
							} else {
								if (arr[i][j-1]) == '@' { obs++ }
								if (arr[i][j+1]) == '@' { obs++ }
								if (arr[i-1][j-1]) == '@' { obs++ }
								if (arr[i-1][j]) == '@' { obs++ }
								if (arr[i-1][j+1]) == '@' { obs++ }
								if obs < 4 { total++; tbr = append(tbr, Point{X: i, Y: j}) }
							}
						}
					}
				} else { // check row above and below
					for j := 0; j < len(arr[i]); j++ {
						if (arr[i][j]) == '@' {
							// println("Checking middle level")
							obs := 0
							if j == 0 { // only check to the right
								if (arr[i-1][j]) == '@' { obs++ }
								if (arr[i-1][j+1]) == '@' { obs++ }
								if (arr[i][j+1]) == '@' { obs++ }
								if (arr[i+1][j]) == '@' { obs++ }
								if (arr[i+1][j+1]) == '@' { obs++ }
								if obs < 4 { total++; tbr = append(tbr, Point{X: i, Y: j}) }
							} else
							if j == len(arr[i])-1 { // only check to the left
								if (arr[i-1][j]) == '@' { obs++ }
								if (arr[i-1][j-1]) == '@' { obs++ }
								if (arr[i][j-1]) == '@' { obs++ }
								if (arr[i+1][j]) == '@' { obs++ }
								if (arr[i+1][j-1]) == '@' { obs++ }
								if obs < 4 { total++; tbr = append(tbr, Point{X: i, Y: j}) }
							} else { // check everywhere
								if (arr[i-1][j-1]) == '@' { obs++ }
								if (arr[i-1][j]) == '@' { obs++ }
								if (arr[i-1][j+1]) == '@' { obs++ }
								if (arr[i][j-1]) == '@' { obs++ }
								if (arr[i][j+1]) == '@' { obs++ }
								if (arr[i+1][j-1]) == '@' { obs++ }
								if (arr[i+1][j]) == '@' { obs++ }
								if (arr[i+1][j+1]) == '@' { obs++ }
								if obs < 4 { total++; tbr = append(tbr, Point{X: i, Y: j}) }
							}
						}
					}
				}
			}
		}
	}
	return total
}

// 10585 too high
// 1443 too low
// 1444
// 1445
// 8609 too high
