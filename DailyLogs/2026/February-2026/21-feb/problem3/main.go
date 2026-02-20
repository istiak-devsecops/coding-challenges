package main

import (
	"context"
	"fmt"
	"problem3/logger"
	"sync"
	"time"
)

func main() {
	logs := []logger.Processor{
		logger.NewSecurityLog("Firewall", "Unauthorized"),
		logger.NewBuildLog("Compiler", "Success"),
	}

	// context
	ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
	defer cancel()

	var wg sync.WaitGroup                   // counter
	reports := make(chan string, len(logs)) // channel

	// launch worker
	for _, log := range logs {
		wg.Add(1)
		go func(p logger.Processor) {
			defer wg.Done()

			select {
			case reports <- p.Process():
			case <-ctx.Done():
				return
			}
		}(log)
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
			fmt.Println("Results:", msg)
		}
	case <-ctx.Done():
		fmt.Println("Error: Processing took too long!")
	}

}
