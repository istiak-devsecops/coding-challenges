package main

import (
	"fmt"
	"os"
)

func checkServer(name string) (status string, err error) {

	if name == os.Args[1] {
		return "Online", nil
	}

	return "", fmt.Errorf("%s is missing", name)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide an arguments.")
		os.Exit(1)
	}

	//slice of severs
	servers := []string{"web-server", "db-server", "mail-server"}

	//check if the arguments matches items from slice
	for _, ser := range servers {
		status, err := checkServer(ser)
		if err != nil {
			fmt.Printf("Alert: %v\n", err)
			continue
		}
		fmt.Printf("Health Check: %s is %s\n", ser, status)
	}
}
