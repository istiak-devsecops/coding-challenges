package main

import (
	"fmt"
	"problem2/plugins"
)

func main() {
	myPlugin := plugins.New("provider")
	fmt.Println("Plugin has been Disabled.")
	fmt.Println("Enabling the plugin...")
	myPlugin.Start()
	fmt.Printf("Plugin has been enabled. Status:  %v\n", myPlugin.IsActive())
}
