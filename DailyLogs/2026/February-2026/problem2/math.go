package main

import (
	"fmt"
	"os"
	"strconv"
)

// this is a comments

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run main.go <num1> <num2>.")
		os.Exit(1)
	}

	numA, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Printf("[Error] '%s' is not a valid integer.\n", os.Args[1])
		os.Exit(1)
	}

	numB, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Printf("[Error] '%s' is not a valid integer.\n", os.Args[2])
		os.Exit(1)
	}

	fmt.Printf("The sum of %d and %d is: %d\n", numA, numB, numA+numB)
}
