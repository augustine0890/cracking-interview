package main

import "fmt"

func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	for i, num := range nums {
		sub := target - num
		if _, ok := hash[sub]; ok {
			return []int{hash[sub], i}
		}
		hash[nums[i]] = i
	}
	return nil
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{3, 2, 4}, 6))
	fmt.Println(twoSum([]int{3, 2, 4}, 9))
}
