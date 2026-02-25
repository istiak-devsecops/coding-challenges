package main

import (
	"bufio"
	"fmt"
	"os"
	"prob1/validator"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter your name to validate: ")
	scanner.Scan()
	var name string
	name = scanner.Text()

	if validator.CheckName(name) == true {
		fmt.Printf("Name Accepted: %s", name)
	} else {
		fmt.Println("Access Denied")
	}

}
