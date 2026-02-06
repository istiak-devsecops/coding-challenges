package main

import (
	"fmt"
	"os"
)

// function to check hard coded server status
func checkServer(name string) (status string, err error) {
	if name == "web-server" {
		return "Online", nil
	}

	return "", fmt.Errorf("%s is missing.", name)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide at least one arguments.")
		os.Exit(1)
	}
	servers := os.Args[1:] //take multiple arguments

	for _, server := range servers {
		status, err := checkServer(server)

		if err != nil {
			// if db-server is missing then exit the program
			if server == "db-server" {
				fmt.Println("CRITICAL ERROR: db-server is missing.")
				return
			}
			fmt.Printf("Alert: %v\n", err)
			continue
		}
		fmt.Printf("Health check: %s is %s\n", server, status)
	}
}
