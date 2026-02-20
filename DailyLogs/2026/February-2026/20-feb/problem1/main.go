package main

import (
	"fmt"
	"problem1/notifier"
)

func main() {
	notification := notifier.Message{Body: "Hello"}
	fmt.Println("Created Message:", notification.Body)

	err := notifier.Send("")
	if err != nil {
		wrapperErr := fmt.Errorf("Platform alert subsystem: %w", err)
		fmt.Println(wrapperErr)
		return
	}
}
