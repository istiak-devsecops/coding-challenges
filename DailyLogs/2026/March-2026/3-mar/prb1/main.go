package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

type Result struct {
	URL     string
	Status  int
	Latency time.Duration
	Err     error
}

func checkService(url string, wg *sync.WaitGroup, results chan<- Result) {
	defer wg.Done()

	start := time.Now()
	resp, err := http.Get(url)

	results <- Result{
		URL:     url,
		Latency: time.Since(start),
		Status: func() int {
			if resp != nil {
				return resp.StatusCode
			}
			return 0
		}(),
		Err: err,
	}
}

func main() {
	urls := []string{
		"https://google.com",
		"https://github.com",
		"http://localhost:8080",
	}

	var wg sync.WaitGroup
	results := make(chan Result, len(urls))

	for _, u := range urls {
		wg.Add(1)
		go checkService(u, &wg, results)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for res := range results {
		if res.Err != nil {
			fmt.Printf("%s | Error: %v\n", res.URL, res.Err)

		} else {
			fmt.Printf("%s | Status: %d | Latency: %v\n", res.URL, res.Status, res.Latency)
		}
	}
}
