package main

import "fmt"

type Notifier interface {
	Send(msg string)
}

type EmailSender struct {
	AdminEmail string
}

func (e EmailSender) Send(msg string) {
	fmt.Printf("Sending Email: %s\n", msg)
}

type SlackSender struct {
	Notification string
}

func (s SlackSender) Send(msg string) {
	fmt.Printf("Sending Notification: %s\n", msg)
}

func Notify(n Notifier, msg string) {
	n.Send(msg)
}

func main() {
	mail := EmailSender{AdminEmail: "admin@company.com"}
	slack := SlackSender{Notification: "#alerts-critical"}
	Notify(mail, "Server is down!")
	Notify(slack, "wake up quick!")
}
