package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	items := []string{"server", "database", "vpc"}

	var wg sync.WaitGroup
	done := make(chan struct{})

	for _, item := range items {
		wg.Add(1)
		go func(name string) {
			defer wg.Done()
			time.Sleep(1 * time.Second)
			fmt.Println("Provisioning: " + name)
		}(item)
	}

	go func() {
		wg.Wait()
		close(done)
	}()

	fmt.Println("Main: Waiting for workers...")
	<-done
	time.Sleep(1 * time.Second)
	fmt.Println("Main: All workers finished. Exiting.")
}
