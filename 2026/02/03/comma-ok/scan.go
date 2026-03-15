package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run <script> <port>")
		os.Exit(1)
	}

	lookupPort, _ := strconv.Atoi(os.Args[1])
	services := map[int]string{
		80:  "HTTP",
		443: "HTTPS",
		22:  "SSH",
	}

	//comma, ok idioms
	val, ok := services[lookupPort]

	if ok {
		fmt.Printf("Port %d is %s\n", lookupPort, val)
	} else {
		fmt.Printf("Port %d is an unknown service\n", lookupPort)
	}
}
