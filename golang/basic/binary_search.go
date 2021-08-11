package main

import "fmt"

func BinarySearch(data []int, value int) bool {
	size := len(data)
	var mid int
	low := 0
	high := size - 1
	for low <= high {
		mid = low + (high-low)/2
		if data[mid] == value {
			return true
		} else {
			if data[mid] < value {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}
	}
	return false
}

func main() {
	v1 := BinarySearch([]int{5, 10, 15, 20, 25}, 1)
	fmt.Println(v1)

	v2 := BinarySearch([]int{5, 10, 15, 20, 25}, 20)
	fmt.Println(v2)

}
