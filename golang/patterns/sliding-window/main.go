package main

import "fmt"

// Given an array, find the average of all contiguous subarrays of size 'K' in it.
func findAverages(K int, arr []int) []float64 {
	var result []float64
	for i := 0; i <= len(arr)-K; i++ {
		var sum float64
		for j := i; j < i+K; j++ {
			sum += float64(arr[j])
		}
		result = append(result, sum/float64(K))
	}

	return result
}

func main() {
	res := findAverages(5, []int{1, 3, 2, 6, -1, 4, 1, 8, 2})
	fmt.Println("Averages of subarrays of size K: ", res)
}
