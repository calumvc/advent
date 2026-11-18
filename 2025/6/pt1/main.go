package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

type Problem struct {
	a, b, c, d int
	op string
}

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

	problems := []Problem{}

	for i := 0; i < len(arr); i++ {
		tings := strings.Fields(arr[i])
		
		for j := 0; j < len(tings); j++ {
			if len(problems) <= j {
				a, _ := strconv.Atoi(tings[j])
				problems = append(problems, Problem{ a: a, b: 0, c: 0, op: "" })
			} else
			if i == 1 {
				b, _ := strconv.Atoi(tings[j])
				problems[j].b = b
			} else 
			if i == 2 {
				c, _ := strconv.Atoi(tings[j])
				problems[j].c = c
			} else 
			if i == 3 {
				d, _ := strconv.Atoi(tings[j])
				problems[j].d = d
			}
			if i == 4 {
				d := tings[j]
				problems[j].op = d
			}
		}
	}

	for k := 0; k < len(problems); k++ {
		if problems[k].op == "+" {
			total += problems[k].a + problems[k].b + problems[k].c + problems[k].d
		} else { 
			total += problems[k].a * problems[k].b * problems[k].c * problems[k].d
		}
		// println("PROBLEM -> ", problems[k].a, problems[k].b, problems[k].c, problems[k].op)
	}


	return total
}

// 6171290547579
