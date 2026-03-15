package notifier

import "errors"

// === notification Struct and Function ===
type Message struct {
	Body string
}

func Send(msg string) error {
	if msg == "" {
		return errors.New("empty message")
	}
	return nil
}
