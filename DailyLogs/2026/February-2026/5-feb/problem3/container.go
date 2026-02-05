package main

import (
	"fmt"
)

type Container struct {
	Name  string
	Image string
	Port  int
}

func main() {
	var cluster []Container                                         // an empty slice
	c1 := Container{Name: "Nginx", Image: "nginx:latest", Port: 80} // struct instance
	cluster = append(cluster, c1)                                   // append it to the list
	cluster = append(cluster, Container{
		Name:  "db-server",
		Image: "postgres",
		Port:  5432,
	})

	fmt.Println("Starting cluster deployment...")
	fmt.Println("-------------------------")

	// loop through the slice
	for _, c := range cluster {
		fmt.Printf("deploying Logic: %+v\n", c)
		fmt.Printf("Action: Starting %s on port %d...\n\n", c.Name, c.Port)
	}
}
