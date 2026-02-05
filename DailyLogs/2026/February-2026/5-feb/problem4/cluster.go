package main

import (
	"fmt"
	"os"
)

type Container struct {
	Name  string
	Image string
	Port  int
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("USAGE: go run <script> <container name>")
		os.Exit(1)
	}
	//define an empty cluster
	//adding info to the slice
	cluster := []Container{
		{Name: "redis-cache", Image: "redis", Port: 6379},
		{Name: "web-server", Image: "nginx", Port: 80},
	}

	lookUpImg := os.Args[1] //user input
	found := false          //bool flag

	for _, c := range cluster {
		if c.Name == lookUpImg {
			fmt.Printf("FOUND: Using image %s\n", c.Image)
			found = true
			break
		}
	}

	if !found {
		fmt.Println("Container not found in inventory.")
	}
}
