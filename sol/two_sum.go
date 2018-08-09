package main

import "fmt"

func twoSum(nums []int, target int) []int {
	complementMap := make(map[int]int)

	for index, element := range nums {
		complement := target - element

		if _, ok := complementMap[complement]; ok {
			return []int{index, complementMap[complement]}
		}

		complementMap[element] = index
	}

	return []int{}
}

func mainTwoSum() {
	result := twoSum([]int{2, 7, 11, 15}, 9) // [0,1]
	fmt.Println(result)
}
