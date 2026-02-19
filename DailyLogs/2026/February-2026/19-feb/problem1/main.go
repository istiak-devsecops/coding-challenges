// The silent watcher

package main

import (
	"fmt"
	"sync"
	"time"
)

// create a slice with items
func main() {
	items := []string{"server", "database", "cache", "message-queue"}
	var wg sync.WaitGroup       // counter
	done := make(chan struct{}) // done signal

	// loop through the slice and print a statement
	for _, item := range items {
		wg.Add(1)
		go func(name string) {
			defer wg.Done()
			time.Sleep(1 * time.Second)
			fmt.Printf("Provisioning: %s\n", name)
		}(item)
	}

	go func() {
		wg.Wait()
		close(done)
	}()

	fmt.Println("Waiting for all items to be provisioned...")
	<-done // wait for the done signal
	fmt.Println("All done!")
}
