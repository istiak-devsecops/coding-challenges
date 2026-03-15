package main

import (
	"bufio"
	"fmt"
	"os"
	"prob1/validator"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter your name: ")
	scanner.Scan()
	name := scanner.Text()

	fmt.Print("Enter a port: ")
	scanner.Scan()
	input := scanner.Text()
	port, err := strconv.Atoi(input)

	if err != nil {
		fmt.Println("Not a valid port number.")
		return
	}

	if validator.CheckName(name) == true && validator.CheckPort(port) == true {
		fmt.Printf("Name %s approved | Port %d approved.", name, port)
	} else {
		fmt.Print("Name and port is not approved.")
	}
}
