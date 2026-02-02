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

	hostName := os.Args[1]
	fmt.Println("Generating hostnames:")

	// the main logic to generate hostname
	for i := startNum; i < startNum+countNum; i++ {
		fmt.Printf("%s-%d\n", hostName, i)
	}
}
