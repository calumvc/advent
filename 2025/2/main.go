package main

import(
	// "fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func main(){

	f, _ := os.Open("puzzle.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)

	var ops string = ""

	for scanner.Scan(){
		ops = scanner.Text()
	}
	ops = ops

	println(validator(ops))
	// println(validator("123123123-123123124"))
	// println(validator("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"))
	// println(validator("879818128-879948512"))
	// println(validator("328412-412772,1610-2974,163-270,7693600637-7693779967,352-586,65728-111612,734895-926350,68-130,183511-264058,8181752851-8181892713,32291-63049,6658-12472,720-1326,21836182-21869091,983931-1016370,467936-607122,31-48,6549987-6603447,8282771161-8282886238,7659673-7828029,2-18,7549306131-7549468715,3177-5305,20522-31608,763697750-763835073,5252512393-5252544612,6622957-6731483,9786096-9876355,53488585-53570896"))
	// println(validator("1-20"))
}

func validator(args string) int {
	total := 0
	arr := strings.Split(args, ",")

	for i := 0; i < len(arr); i++ {
		newstrings := strings.Split(arr[i], "-")
		l, _ := strconv.Atoi(newstrings[0])
		r, _ := strconv.Atoi(newstrings[1])
		println("RUNNING L: ", l, " R:", r)

		for j := l; j < r+1; j++ { // iterate over a number (545454)
		
			newj := strconv.Itoa(j)

			if len(newj) == 1 { 
				if r > 11 { j = 11 }
			}

			if (newj[len(newj)/2:] == newj[:len(newj)/2]){
				total += j
			} else {
			state := ""
			state += string(newj[0])

			for k := 1; k < (len(newj)/len(state)+1); k++ { // this loop tries the next thing again with a bigger state
			// println(" K IS ", k,)

				for m := 0; m < (len(newj)); m += k { // this loop checks if the state is recurred in the rest
					if m+k > len(newj) { k-- }
					// println("best debugging M ", m, " K ", k)
					//
					// println("checking newj", newj[m:m+k], " against state ", state, " K IS ", k, " L IS ", m)
					if state == newj[m:m+k] { 
						// println("M IS ", m, " LEN NEWJ ", len(newj))
						if m >= len(newj)-len(state) { total += j }

					} else { // if theres a failure to assert increase state and try the next
						state = state + string(newj[k])
						// println("STATE IS NOW ", state, " NEWJSLICE, ", newj[0:k+1])
						break
					}
				}
			}
			// println("ONTO NEW J")
		}
		}
	}
	return total
}

// 5 x10^15 too high
// 5159057303221974 ^
// 5149883684008216
// 5149883684004468
// 5149557732058873

// 325956146265

// 2252820925730

// 18959747854
// 28858486289
// 28858485233
// 28858486244
