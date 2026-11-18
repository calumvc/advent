package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main(){

	f, _ := os.Open("puzzle")

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var arr = make([]string, 0, 0)

	for scanner.Scan(){
		arr = append(arr, scanner.Text())
	}

	println(cephalomaths(arr))
}

func cephalomaths(arr []string) int {
	total := 0

	minitotal := 0
	operation := ""
	for i := 0; i < len(arr[0]); i++ {
		op := string(arr[4][i])
		a := string(arr[0][i])
		b := string(arr[1][i])
		c := string(arr[2][i])
		d := string(arr[3][i])

		combo := a + b + c + d
		combo = strings.ReplaceAll(combo, " ", "")
		combotron, _ := strconv.Atoi(combo)

		println("working with combo -> ", combo)
		if op == " " {
			if operation == "+" {
				println("minitotal -> ", minitotal, " adding")
				minitotal += combotron
			} else {
				println("minitotal -> ", minitotal, " timesing")
				if combotron != 0 {
					minitotal *= combotron
				}
			}
		} else {
			total += minitotal
			println("adding -> ", minitotal ," : next operation is -> ", op, "total is now -> ", total)
			minitotal = combotron
			operation = op
		}
	}

	total += minitotal

	return total

}

// 6171290547579
// 5781495
// 8811937968081 too low
// 26439365022308 too high
// 8811937976367
