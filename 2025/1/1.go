package main

import(
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func main(){

	f, err := os.Open("input.txt")
	if err != nil {
		fmt.Printf("GG")
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

	ops := []string{}

	for scanner.Scan(){
		ops = append(ops, scanner.Text())
	}

	if err := scanner.Err(); err!= nil{
		fmt.Printf("FATAL")
	}

	fmt.Printf("%d ANSWER", combination(ops))
	// fmt.Printf("%d HARDCODE", combination([]string{"L150"}))
	// fmt.Printf("%d HARDCODE", combination([]string{"R50", "R100", "L200", "R300"}))
	// fmt.Printf("%d HARDCODE", combination([]string{"L50", "R200"})) // should be 3
	// fmt.Printf("%d HARDCODE", combination([]string{"L125"})) // should be 1
	// fmt.Printf("%d HARDCODE", combination([]string{"L50", "L10"})) // should be 1
}

func combination(arr []string) int {
	result := 50
	count := 0

	for _, item := range arr{
		num, _ := strconv.Atoi(item[1:])
		os := num / 100
		if ((num % 100) == 0){
			// if its divisible perfectly by 100 just get the amount and skip
		} else {
			num = num % 100

			if string(item[0]) == "L" {
				result -= num
			} else {
				result += num
			}

		  if (result > 99) {
				result = result % 100
				if result > 0 { os++ } // it is already considered as clicking it its 0 here so do this
			} 

			if (result < 0){
				if (result + num == 0) {} else {
					os++
				}
				result = 100 + (result % 100)
			}

			if (result == 0) { os++ }

			println("Dial at -> ", result)

			println("OS ", os)
		}
		count += os
	}

	return count 
}
