package main

import (
	"fmt"
	"sync"
	"time"
)

func checkHealth(serviceName string, wg *sync.WaitGroup) {
	defer wg.Done() // will execute before exiting the function

	fmt.Printf("Checking [%s]...\n", serviceName)
	time.Sleep(time.Second * 2)
	fmt.Printf("%s is HEALTHY!\n", serviceName)
}

func main() {
	var wg sync.WaitGroup // the counter

	wg.Add(3) // added 3 task to the counter

	go checkHealth("Database", &wg)
	go checkHealth("Redis-Cache", &wg)
	go checkHealth("Auth-Server", &wg)

	wg.Wait()

	fmt.Println("All the services ready. Starting IDP deployment...")
}
