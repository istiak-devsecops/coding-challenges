package main

import (
	"fmt"
)

func main() {

	numList := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	var evenNum []int //declaring empty list

	for _, num := range numList {
		if num%2 == 0 {
			evenNum = append(evenNum, num)
		}
	}

	fmt.Printf("The list of even numbers are: %v\n", evenNum)
}
