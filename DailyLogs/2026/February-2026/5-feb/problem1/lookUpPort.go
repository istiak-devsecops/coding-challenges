package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("USAGE: go run <script> <port>")
		os.Exit(1)
	}

	//port mapping
	ports := map[int]string{
		80:  "HTTP",
		443: "HTTPS",
		22:  "SSH",
	}

	lookUpPort, _ := strconv.Atoi(os.Args[1]) //type conversion
	val, ok := ports[lookUpPort]              //Command Ok idioms

	if ok {
		fmt.Printf("The %d port found.\n", lookUpPort)
		fmt.Printf("Service: %s", val)
	} else {
		fmt.Printf("Your port %d is missing from the list.\n", lookUpPort)
		fmt.Println("Service: Unknown")
	}

}
