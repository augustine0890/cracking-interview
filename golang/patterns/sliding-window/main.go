package main

import "fmt"

// Given an array, find the average of all contiguous subarrays of size 'K' in it.
// Time complexity: O(N*K) --> O(N)
func findAveragesBF(K int, arr []int) []float64 {
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

func findAverages(K int, arr []int) []float64 {
	res := make([]float64, len(arr)-K+1)
	windowSum, windowStart := 0.0, 0

	for windowEnd := 0; windowEnd < len(arr); windowEnd++ {
		windowSum += float64(arr[windowEnd])
		if windowEnd >= K-1 {
			res[windowStart] = windowSum / float64(K)
			windowSum -= float64(arr[windowStart])
			windowStart++
		}
	}

	return res
}

func main() {
	resBF := findAveragesBF(5, []int{1, 3, 2, 6, -1, 4, 1, 8, 2})
	fmt.Println("Averages of subarrays of size K (Burte-Force):", resBF)
	res := findAverages(5, []int{1, 3, 2, 6, -1, 4, 1, 8, 2})
	fmt.Println("Averages of subarrays of size K:", res)

}
