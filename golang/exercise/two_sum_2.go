package main

import "fmt"

func twoSum(nums []int, target int) []int {
	lo, hi := 0, len(nums)-1
	for lo < hi {
		sum := nums[lo] + nums[hi]
		if sum == target {
			return []int{lo, hi}
		}
		if sum < target {
			lo++
		} else {
			hi--
		}
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{2, 3, 4}, 6))
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 2))
	fmt.Println(twoSum([]int{-1, 0}, -1))
}
