package engine

import (
	"fmt"
	"strings"
	"sync"
	"time"
)

func Deploy(names []string) map[string]string {

	finalStatus := make(map[string]string)
	var wg sync.WaitGroup        // Counter
	results := make(chan string) // channel

	for _, name := range names {
		wg.Add(1)
		go func(n string) {
			defer wg.Done()
			time.Sleep(100 * time.Millisecond)
			if n == "" {
				fmt.Println("[ENGINE ERROR] Skipping empty pod name.")
				return
			}
			results <- fmt.Sprintf("%s: Ready", n)
		}(name)
	}

	// === The Watcher ===
	go func() {
		wg.Wait()
		close(results)
	}()

	for msg := range results {
		parts := strings.Split(msg, ":")
		if len(parts) == 2 {
			finalStatus[parts[0]] = parts[1]
		}
	}
	return finalStatus
}
