package main

import "fmt"

// Given a list of positive and negative integers, find a contiguous subarray
// whose sum (sum of elements) is maximum.
func MaxSubArraySum(data []int) int {
	maxCurr := 0
	maxEnd := 0
	for _, e := range data {
		maxEnd += e
		if maxEnd < 0 {
			maxEnd = 0
		}
		if maxCurr < maxEnd {
			maxCurr = maxEnd
		}
	}
	return maxCurr
}

func main() {
	data := []int{1, -3, 5, 2, -6, 8, 3, -12}
	fmt.Println("Max sub array sum:", MaxSubArraySum(data))
}
