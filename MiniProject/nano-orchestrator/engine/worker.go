package engine

import (
	"fmt"
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
			results <- fmt.Sprintf("%s: Ready", n)
		}(name)
	}

	// === The Watcher ===
	go func() {
		wg.Wait()
		close(results)
	}()

	for msg := range results {
		var sName, sStatus string
		fmt.Sscanf(msg, "%s:%s", &sName, &sStatus)
		finalStatus[sName] = sStatus
	}
	return finalStatus
}
