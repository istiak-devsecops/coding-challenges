package main

import (
	"fmt"
	"sync"
	"time"
)

// interface
type Deployer interface {
	Deploy(wg *sync.WaitGroup, results chan string)
}

// Component methods
type Component struct {
	Name     string
	Duration time.Duration
}

func (c *Component) Deploy(wg *sync.WaitGroup, results chan string) {
	defer wg.Done()
	fmt.Printf("Provisioning %s\n", c.Name)
	time.Sleep(c.Duration)

	if c.Name == "Storage" {
		results <- fmt.Sprintf("Failed to deploy %s", c.Name)
		return
	}

	results <- fmt.Sprintf("%s Deployed in %v", c.Name, c.Duration)
}

func main() {
	components := []Component{
		{Name: "Network", Duration: 1 * time.Second},
		{Name: "Storage", Duration: 2 * time.Second},
		{Name: "Compute", Duration: 3 * time.Second},
	}

	var wg sync.WaitGroup // counter
	results := make(chan string, len(components))

	//start the worker
	for _, comp := range components {
		wg.Add(1) // increment the counter by 1
		go comp.Deploy(&wg, results)
	}

	// wait for everyone to finish
	wg.Wait()
	close(results)

	for res := range results {
		fmt.Println(res)
	}
}
