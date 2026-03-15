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

	return "", fmt.Errorf("server is unreachable.")
}

// function to deployment validation
func validateDeployment(name string) error {
	_, err := checkServer(name)
	if err != nil {
		return fmt.Errorf("security check failed for %s: %w", name, err)
	}
	return nil //if success return nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide at least one arguments.")
		os.Exit(1)
	}
	servers := os.Args[1:] //take multiple arguments

	for _, server := range servers {
		err := validateDeployment(server)

		if err != nil {
			// if db-server is missing then exit the program
			if server == "db-server" {
				fmt.Printf("CRITICAL: %v\n", err)
				return
			}
			fmt.Printf("Alert: %v\n", err)
			continue
		}
		fmt.Printf("Success: %s validated!\n", server)
	}
}
