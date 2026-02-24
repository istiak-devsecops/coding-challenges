package main

import (
	"fmt"
	"nano-orchestrator/engine"
	"nano-orchestrator/registry"
)

func main() {
	myStore := registry.NewStore()
	podsToDeploy := []string{"api-server", "auth-db", "", "cache-node"}

	// 3. Deploy
	deployedPods := engine.Deploy(podsToDeploy)

	// 4. Persist (Corrected to match your Save(name, status) signature)
	for name, status := range deployedPods {
		myStore.Save(name, status)
	}

	// 5. Verify (Corrected to iterate over the returned map[string]string)
	allPods := myStore.List()
	for name, status := range allPods {
		// Using the %-12s formatting here
		fmt.Printf("Registry Record -> Pod: %-12s | Status: %s\n", name, status)
	}
}
