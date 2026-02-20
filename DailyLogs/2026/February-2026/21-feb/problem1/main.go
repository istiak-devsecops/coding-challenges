package main

import (
	"fmt"
	"problem1/monitor"
)

func main() {

	serv := monitor.NewService("Database", false)
	serv.Toggle()
	fmt.Println("Online status 1:", serv.Status())
	serv.Toggle()
	fmt.Println("Online status 2:", serv.Status())
}
