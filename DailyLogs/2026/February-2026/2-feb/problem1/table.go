package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	// Arguments validation
	if len(os.Args) < 2 {
		fmt.Println("ERROR: Usage: <table.go> <num>.")
		os.Exit(1)
	}

	// check if a valid num is given
	num, errN := strconv.Atoi(os.Args[1])
	if errN != nil {
		fmt.Println("Provide a valid number.")
		os.Exit(1)
	}

	// conditions to multiply
	for i := 1; i <= 12; i++ {
		fmt.Printf("%d x %d = %d\n", num, i, num*i)
	}

}
