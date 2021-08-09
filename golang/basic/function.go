package main

import "fmt"

func max(x, y int) int {
	if x >= y {
		return x
	}
	return y
}

func main() {
	m := max(15, 3)
	fmt.Println(m)
}
