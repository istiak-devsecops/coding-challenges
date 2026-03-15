package main

import (
	"context"
	"fmt"
	"problem4/cloud"
	"sync"
	"time"
)

func main() {
	resources := []cloud.Uploader{
		cloud.NewS3("istiak", "HSHJ7900"),
		cloud.NewAzure("azure", "HJSU7298"),
	}

	// context
	ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
	defer cancel()

	// go routine
	var wg sync.WaitGroup
	reports := make(chan string, len(resources))

	for _, res := range resources {
		wg.Add(1)
		go func(u cloud.Uploader) {
			defer wg.Done()
			select {
			case reports <- u.Upload():
			case <-ctx.Done():
				return
			}
		}(res)
	}

	// Watcher
	done := make(chan struct{})

	go func() {
		wg.Wait()
		close(done)
	}()

	select {
	case <-done:
		close(reports)
		for msg := range reports {
			fmt.Println("Successfully done!", msg)
		}
	case <-ctx.Done():
		fmt.Println("Processing takes too long!")
	}
}
