package main

import (
	"context"
	"fmt"
	"time"
)

// The race against time

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	reports := make(chan string, 1)

	go func() {
		time.Sleep(3 * time.Second)
		reports <- fmt.Sprintf("Report: %s", time.Now().Format(time.RFC3339))
	}()

	select {
	case report := <-reports:
		fmt.Println("win" + report)
	case <-ctx.Done():
		fmt.Println("Timeout!")
	}
}
