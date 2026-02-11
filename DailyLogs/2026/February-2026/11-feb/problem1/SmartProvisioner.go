package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

type Provisioner interface {
	Provision() string
}

// Database
type Database struct {
	Name string
}

func (d Database) Provision() string {
	return fmt.Sprintf("Deploying Database: %s", d.Name)
}

// Server
type Server struct {
	ID int
}

func (s Server) Provision() string {
	return fmt.Sprintf("Deploying Server: %d", s.ID)
}

// Handler
func DynamicHandler(w http.ResponseWriter, r *http.Request) {
	comType := r.URL.Query().Get("type")

	var items []Provisioner // slice of interface

	// dynamic object creation by user request
	switch comType {
	case "database":
		items = append(items, Database{Name: "redis"})
	case "server":
		items = append(items, Server{ID: 7293028})
	case "":
		items = append(items, Database{Name: "redis"}, Server{ID: 7293028})
	default:
		http.Error(w, "Unknown component type", http.StatusNotFound)
		return
	}

	var wg sync.WaitGroup                   // the waitgroup and counter
	report := make(chan string, len(items)) // channel to stream data

	// The goroutine and channel logic
	for _, item := range items {
		wg.Add(1)
		go func(prov Provisioner) {
			defer wg.Done()
			report <- prov.Provision()
		}(item)
	}

	wg.Wait()
	close(report) // close the channel

	// repose back to the user
	fmt.Fprintf(w, "== Provisioning Comnonents == \n")
	for msg := range report {
		fmt.Fprintf(w, "Result: %s\n", msg)
	}
}

// The main logic
func main() {
	http.HandleFunc("/provision", DynamicHandler) // define the route
	fmt.Println("Type: http://localhost:8080/provision?type=<write the type here>")
	fmt.Println("only available type: database/server")
	//log.Fatal print the error and kill the program
	log.Fatal(http.ListenAndServe(":8080", nil))
}
