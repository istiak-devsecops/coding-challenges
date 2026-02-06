package main

import (
	"fmt"
	"os"
)

func checkServer(name string) (string, error) {

	if name == "web-server" {
		return "Online", nil
	}

	return "", fmt.Errorf("server %s is missing", name)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide an arguments.")
		os.Exit(1)
	}

	status, err := checkServer(os.Args[1]) // call the function and pass the arguments

	// check if there is an error
	if err != nil {
		fmt.Println("Error occured:", err)
		return // Exit the function early
	}

	fmt.Println("Status is:", status)
}
