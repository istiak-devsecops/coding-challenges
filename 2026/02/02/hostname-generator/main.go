// hostname generator

package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Println("Usage: <hostname-prefix> <start num> <counts>")
		os.Exit(1)
	}

	startNum, errS := strconv.Atoi(os.Args[2])
	countNum, errC := strconv.Atoi(os.Args[3])

	if errS != nil {
		fmt.Println("Please provide a valid starting number.")
		os.Exit(1)
	}

	if errC != nil {
		fmt.Println("Please write how many names you want.")
		os.Exit(1)
	}

	var hostNames []string // declaring the slice
	name := os.Args[1]
	fmt.Println("Generating hostnames:")

	// the main logic to generate hostname
	for i := startNum; i < startNum+countNum; i++ {
		newName := fmt.Sprintf("%s-%d\n", name, i)
		hostNames = append(hostNames, newName)
	}

	fmt.Printf("First hostname: %s\n", hostNames[0])
	fmt.Printf("Last hostname: %s\n", hostNames[len(hostNames)-1])
	fmt.Println("Hostname excluding the first: ")
	fmt.Printf("%s", hostNames[1:])
}
