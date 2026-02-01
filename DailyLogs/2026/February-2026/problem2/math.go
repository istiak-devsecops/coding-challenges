package main

import (
	"fmt"
	"os"
	"strconv"
)

// this is a comments

func main() {
	switch len(os.Args) {
	case 1:
		fmt.Println("Error: I need two number to do sum.")
		os.Exit(1)
	case 2:
		fmt.Println("Error: I need one more number to do sum.")
		os.Exit(1)
	}

	A := os.Args[1]
	B := os.Args[2]

	numA, _ := strconv.Atoi(A)
	numB, _ := strconv.Atoi(B)

	fmt.Printf("The sum of %d and %d is: %d", numA, numB, numA+numB)
}
