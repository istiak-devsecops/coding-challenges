package main

import "fmt"

type Logger interface {
	Log(message string)
}

// Consol logger
type ConsoleLogger struct {
	// empty for now
}

func (c ConsoleLogger) Log(message string) {
	fmt.Println("[CONSOLE]: " + message)
}

// File Logger
type FileLogger struct {
	Filename string
}

func (f FileLogger) Log(message string) {
	fmt.Printf("[FILE: %s]: %s\n", f.Filename, message)
}

// The manager
func NotifyUser(l Logger, msg string) {
	l.Log(msg)
}

func main() {
	clog := ConsoleLogger{}
	flog := FileLogger{Filename: "system.log"}

	NotifyUser(clog, "Server started on port 8080")
	NotifyUser(flog, "Database connection lost!")
}
