package main

import (
	"fmt"
	"os"
	"strconv"
)

// Container struct
type Container struct {
	Name  string
	Image string
	Port  int
}

func main() {
	if len(os.Args) < 4 {
		fmt.Println("USAGE: go run <script> <container name> <container image> <port>")
		os.Exit(1)
	}

	cPort, _ := strconv.Atoi(os.Args[3]) //type conversion
	myContainer := Container{
		Name:  os.Args[1],
		Image: os.Args[2],
		Port:  cPort,
	}

	fmt.Printf("Deploying container image: %s\n", myContainer.Name)
	fmt.Printf("Using Image: %s and Port: %d\n", myContainer.Image, myContainer.Port)

}
