package main

import "fmt"

type FileLogger struct {
	Filename string
}

func TagData(data any) {
	fmt.Printf("[TAGGED] Type: %T | Value: %v\n", data, data)
}

func main() {
	TagData("Production-Cluster")
	TagData(8080)
	logConfig := FileLogger{Filename: "audit.log"}
	TagData(logConfig)
}
