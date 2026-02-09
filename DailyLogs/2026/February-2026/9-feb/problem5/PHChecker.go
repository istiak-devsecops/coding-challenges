package main

import (
	"fmt"
	"sync"
	"time"
)

func checkHealth(serviceName string, wg *sync.WaitGroup, c chan string) {
	defer wg.Done() // will execute before exiting the function

	fmt.Printf("Checking [%s]...\n", serviceName)
	time.Sleep(time.Second * 2)
	c <- fmt.Sprintf("%s is HEALTHY!", serviceName)
}

func main() {
	var wg sync.WaitGroup // the counter

	results := make(chan string, 3)

	wg.Add(3) // added 3 task to the counter

	go checkHealth("Database", &wg, results)
	go checkHealth("Redis-Cache", &wg, results)
	go checkHealth("Auth-Server", &wg, results)

	wg.Wait()
	close(results) // close the channel so the range loop knows it

	fmt.Println("---Report Received---")
	for msg := range results {
		fmt.Println("Manager received:", msg)
	}

	fmt.Println("All the services ready. Starting IDP deployment...")
}
