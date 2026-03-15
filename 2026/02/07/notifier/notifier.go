package main

import "fmt"

// notifier
type Notifier interface {
	Send(message string) error
}

// slack employee struct
type Slack struct {
	WebhookURL string
}

// email employee struct
type Email struct {
	Address string
}

func (s Slack) Send(msg string) error {
	fmt.Printf("[Slack Alert] Sending to %s: %s\n", s.WebhookURL, msg)
	return nil
}

func (e Email) Send(msg string) error {
	fmt.Printf("[Email Alert] Sending to %s: %s\n", e.Address, msg)
	return nil
}

func NotifyUser(n Notifier, msg string) {
	n.Send(msg)
}

func main() {
	// Create our "employees"
	mySlack := Slack{WebhookURL: "https://hooks.slack.com/123"}
	myEmail := Email{Address: "admin@company.com"}

	// Which one will do the job? Whichever one we pass in!
	fmt.Println("--- Notification 1 ---")
	NotifyUser(mySlack, "Server is down!")

	fmt.Println("--- Notification 2 ---")
	NotifyUser(myEmail, "Database backup complete.")
}
