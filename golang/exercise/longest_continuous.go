package main

import "fmt"

func maxLength(arr []int) int {
	if len(arr) == 0 {
		return 0
	}
	res := 1
	incr, decr := 1, 1
	for i := 1; i < len(arr); i++ {
		if arr[i-1] < arr[i] {
			incr++
			if incr > res {
				res = incr
			}
			decr = 1
		} else {
			decr++
			if decr > res {
				res = decr
			}
			incr = 1
		}
	}
	return res
}

func main() {
	r := maxLength([]int{1, 5, 3, 2, 1, 3, 4, 5, 6})
	fmt.Println(r)
}
