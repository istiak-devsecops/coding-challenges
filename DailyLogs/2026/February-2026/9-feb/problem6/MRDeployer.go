package main

import (
	"fmt"
	"sync"
	"time"
)

func deployRegion(region string, wg *sync.WaitGroup, report chan string) {
	defer wg.Done()
	time.Sleep(time.Second * 1)
	report <- fmt.Sprintf("Region [%s] is LIVE.", region)
}

func main() {
	var wg sync.WaitGroup // counter
	result := make(chan string, 3)

	wg.Add(3) // counter start with 3 worker
	go deployRegion("US-East", &wg, result)
	go deployRegion("EU-West", &wg, result)
	go deployRegion("AP-South", &wg, result)

	wg.Wait() // wait till the counter hits zero

	close(result) // close the channel

	fmt.Println("=== Deploying to Region ===")
	for r := range result {
		fmt.Printf("Message: %s\n", r)
	}

}
