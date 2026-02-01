package main

import (
	"fmt"
	"os"
)

var name = "istiak"

func main() {

	if len(os.Args) > 1 {
		name = os.Args[1]
	}

	fmt.Printf("Hello, %s! Welcome to Go.\n", name)
}