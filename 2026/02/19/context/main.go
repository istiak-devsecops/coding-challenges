package main

import (
	"context"
	"fmt"
	"time"
)

func worker(ctx context.Context) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println("Worker: Stopping Safely!")
			return
		case <-time.After(500 * time.Millisecond):
			fmt.Println("Worker: Still working...")
		}
	}
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	go worker(ctx)
	time.Sleep(3 * time.Second)
	cancel()
	time.Sleep(100 * time.Millisecond)
}
