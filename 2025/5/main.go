package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	L, R int
}

func main(){

	f, _ := os.Open("puzzle")

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var arr = make([]string, 0, 0)

	for scanner.Scan(){
		arr = append(arr, scanner.Text())
	}

	// test_ranges := []Range{{L: 5, R:10}, {L: 6, R: 15}, {L:2, R:3}, {L:2, R:4}}
	// println(test_ranges)
	// ranges := range_merger(test_ranges)
	// println(ranges)
	print(food_identifierator(arr))

}

func food_identifierator(arr []string) int {
	total := 0
	pastline := false
	merged := false
	ranges := []Range{}

	for i := 0; i < len(arr); i++ {
		if arr[i] == "" { pastline = true }
		if pastline == true && merged == false { ranges = range_merger(ranges); merged = true }

		if pastline == false {
			leftright := strings.SplitN(arr[i], "-", 2)
			l, _ := strconv.Atoi(leftright[0])
			r, _ := strconv.Atoi(leftright[1])
			ranges = append(ranges, Range{ L: l, R: r })
		} else
		{
			for j := 0; j < len(ranges); j++ {
				num, _ := strconv.Atoi(arr[i])
				if num > ranges[j].L && num < ranges[j].R { 
					total++
					break
				}
			}
		}
	}

	return total
}

func range_merger(arr []Range) []Range {
	arr = range_mergesorter(arr)
	ranges := []Range{}
	ranges = append(ranges, arr[0])
	for i := 1; i < len(arr); i++ { // loop over old ranges
		included := false
		for j := 0; j < len(ranges); j++ { // loop over ranges that already exist
			if arr[i].L < ranges[j].L && arr[i].R > ranges[j].R {
				ranges[j].L = arr[i].L
				ranges[j].R = arr[i].R
				included = true
				break
			} else
			if arr[i].L >= ranges[j].L && arr[i].R <= ranges[j].R {
				included = true
				break
			} else
			if arr[i].L >= ranges[j].L && arr[i].L <= ranges[j].R && arr[i].R >= ranges[j].R { // if the range fits and right needs extended
				ranges[j].R = arr[i].R
				included = true
				break
			}
		}
		if included == false {
			ranges = append(ranges, arr[i])
		}
	}
	total := 0
	for k := 0; k < len(ranges); k++ {
		println("RANGES", ranges[k].L, ranges[k].R)
		total += (ranges[k].R - ranges[k].L + 1)
	}
	println("RANGE DIFFERENCES", total)
	return ranges
}

func range_mergesorter(arr []Range) []Range {
	if len(arr) <= 1 { return arr }

	mid := len(arr) / 2

	l_arr := arr[:mid]
	r_arr := arr[mid:]

	left := range_mergesorter(l_arr)
	right := range_mergesorter(r_arr)
	return range_mergesorting_merge(left, right)
}

func range_mergesorting_merge(l_arr []Range, r_arr []Range) []Range {
	res := []Range{}

	for len(l_arr) != 0 && len(r_arr) != 0 {
		if l_arr[0].L < r_arr[0].L {
			res = append(res, l_arr[0])
			l_arr = l_arr[1:]
		} else {
			res = append(res, r_arr[0])
			r_arr = r_arr[1:]
		}
	}

	for len(l_arr) != 0 {
		res = append(res, l_arr[0])
		l_arr = l_arr[1:]
	}

	for len(r_arr) != 0 {
		res = append(res, r_arr[0])
		r_arr = r_arr[1:]
	}

	return res
}


// 558 too low
// 344813017450467558 too high
