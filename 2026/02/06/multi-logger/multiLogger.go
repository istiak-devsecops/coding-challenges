package main

import (
	"fmt"
)

func startDeployment(region string, apps ...string) {
	fmt.Printf("Initiating deployment in [%s]\n", region)

	for _, name := range apps {
		fmt.Printf("Provisioning app: [%s]\n", name)
	}
}

func main() {

	service := []string{"api-gateway", "auth-service"}

	startDeployment("us-east-1", service...) //unpack the slice or it will throw error
	startDeployment("eu-west-1", "web-ui", "db-proxy", "cache")
}
