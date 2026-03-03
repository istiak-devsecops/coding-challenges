package main

import (
	"net/http"
	"sync"
	"time"
)

type Result struct {
	URL     []string
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
