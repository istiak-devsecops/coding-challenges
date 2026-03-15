package main

import "fmt"

type Container struct {
	Name  string
	Image string
}

func main() {
	myC := Container{Name: "old-name", Image: "nginx"}

	ptr := &myC //define a pointer
	ptr.Name = "new-name"
	fmt.Println(myC)
}
