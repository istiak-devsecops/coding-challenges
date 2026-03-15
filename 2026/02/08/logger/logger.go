package main

import "fmt"

type Logger interface {
	Log(message string, level int)
}

// Consol logger
type ConsoleLogger struct {
	// empty for now
}

func (c ConsoleLogger) Log(message string, level int) {
	fmt.Printf("[CONSOLE]: %s [Level-%d]\n", message, level)
}

// File Logger
type FileLogger struct {
	Filename string
}

func (f FileLogger) Log(message string, level int) {
	fmt.Printf("[FILE: %s]: %s [level-%d]\n", f.Filename, message, level)
}

// The manager
func NotifyUser(l Logger, msg string, level int) {

	if level >= 2 {
		l.Log(msg, level)
	}

	if level < 2 {
		fmt.Println("Skipping log-level log")
	}
}

func main() {
	clog := ConsoleLogger{}
	flog := FileLogger{Filename: "system.log"}

	NotifyUser(clog, "Server started on port 8080", 1)
	NotifyUser(flog, "Database connection lost!", 2)
}
