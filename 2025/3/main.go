package main

import (
	"bufio"
	"fmt"
	"os"
	// "strconv"
	"time"
)

func main(){

	f, _ := os.Open("puzzle.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var arr = []string{}

	for scanner.Scan(){
		arr = append(arr, scanner.Text())
	}

	start := time.Now()
	println(batterify(arr))
	fmt.Printf("Took %v", (time.Since(start)))

}

func batterify(arr []string) int {
	total := 0
	
	for i := 0; i < len(arr); i++ { // for every batterypack
		// println("NEW NUM---------------------------------")
		highest := arr[i][0]
		highest_index := 0
		power := [12]byte{}
		
		for j := 1; j < len(arr[i])-11; j++ { // for every number in batterpack starting at 1
			if arr[i][j] > highest { highest = (arr[i][j]); highest_index = j } 
		} // highest should now be found not including the final number

		power[0] = highest

		cnt := 1

		for k := highest_index+1; k < len(arr[i]); k++ {

			if len(arr[i]) - k == 12 - cnt { // if you have to take every other number
				power[cnt] = arr[i][k]
				cnt++
			} else {

				highestnow := arr[i][k]
				surplus := 0

				for l:= 0; l < (len(arr[i])-k) - (12-cnt)+1; l++ {
					if arr[i][k+l] > highestnow { highestnow = arr[i][k+l]; surplus = l }
				}

				power[cnt] = highestnow
				cnt++
				if cnt == 12 { break }
				k += surplus
			}
		}

		// string := ""

		newpower := 0
		for z := 0; z < len(power); z++{
			newpower = newpower * 10 + int(power[z]-48)
			// num := int(power[z])
			// string = string + strconv.Itoa(num-48)
		}
		// println(newpower)
		// println(string)
		// newpower, _ = strconv.Atoi(string)
		total += newpower
	}
	return total 
}


// 3884297052318
// 109855080055217 too low
// 165593638655605 too low
// 173300819005913
