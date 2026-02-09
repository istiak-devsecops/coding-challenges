package main

import (
	"fmt"
	"sync"
	"time"
)

func deploy(name string, wg *sync.WaitGroup) {
	// 1. The Exit Signal: Ensure we click "Done" when finished
	defer wg.Done()

	fmt.Printf("Deploying %s...\n", name)
	time.Sleep(2 * time.Second)
	fmt.Printf("%s is live!\n", name)
}

func main() {
	// 2. The Counter: Create it once in the Manager function
	var wg sync.WaitGroup

	// 3. The Instruction: Tell the counter we are starting 2 tasks
	wg.Add(2)

	// 4. The Execution: Start them in the background with "go"
	// Use "&" so they all talk to the SAME counter
	go deploy("Database", &wg)
	go deploy("API-Gateway", &wg)

	fmt.Println("Manager: Waiting for deployments...")

	// 5. The Barrier: Stop here until the counter reaches 0
	wg.Wait()

	fmt.Println("All systems are GO. IDP is ready.")
}
