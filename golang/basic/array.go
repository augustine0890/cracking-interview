package main

import "fmt"

// Write the method that will return the sum of all the elements of the integer list
func sumArray(data []int) int {
	var total int
	for _, e := range data {
		total += e
	}
	return total
}

// Write the method which will search a list for some give value
func sequentialSearch(data []int, value int) bool {
	for _, e := range data {
		if e == value {
			return true
		}
	}
	return false
}

func main() {
	s := sumArray([]int{34, 53, 63})
	fmt.Printf("Total: %v\n", s)

	t := sequentialSearch([]int{34, 43, 65}, 34)
	fmt.Println("Result: ", t)
	f := sequentialSearch([]int{34, 43, 65}, 76)
	fmt.Println("Result: ", f)
}
