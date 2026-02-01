package main

import (
	"fmt"
	"os"
	"strconv"
)

// this is a comments

func main() {
	if len(os.Args) < 4 {
		fmt.Println("[Error] Usage: <num1> <num2> <add|sub|mul|div>.")
		os.Exit(1)
	}

	// type conversion of number
	a, errA := strconv.Atoi(os.Args[1])
	b, errB := strconv.Atoi(os.Args[2])
	operations := os.Args[3]

	if errA != nil || errB != nil {
		fmt.Println("Please provide a valid integer.")
		os.Exit(1)
	}

	switch operations {
	case "add":
		fmt.Printf("The sum of %d and %d is: %d\n", a, b, a+b)
	case "sub":
		fmt.Printf("The substraction of %d and %d is: %d\n", a, b, a-b)
	case "mul":
		fmt.Printf("The multiplication of %d and %d is: %d\n", a, b, a*b)
	case "div":
		if b == 0 {
			fmt.Println("Go doesn't allow a number division with zero.")
			os.Exit(1)
		}
		fmt.Printf("The division of %d and %d is: %d", a, b, a%b)
	default:
		fmt.Printf("%s is not a valid operations.", operations)
		os.Exit(1)
	}
}
