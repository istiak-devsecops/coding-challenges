package main

import (
	"fmt"
	"os"
)

// var name = "istiak"

func main() {

	argCount := len(os.Args)

	if argCount == 1 {
		fmt.Println("Error: No name provided.")
		fmt.Println("Usage: go run <filename.go> [FirstName] [LastName]")
		os.Exit(1)
	}

	if argCount == 2 {
		fmt.Printf("Hello, %s! You forgot your [LastName]\n", os.Args[1])
		fmt.Println("Usage: go run <filename.go> [FirstName] [LastName]")
		os.Exit(1)
	}

	firstName := os.Args[1]
	lastName := os.Args[2]
	fmt.Printf("Hello, %s %s! Welcome to Go.\n", firstName, lastName)
}
