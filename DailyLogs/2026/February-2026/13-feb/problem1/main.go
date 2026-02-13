package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
)

type Provisioner interface {
	Provision() string
}

type Database struct {
	Name string
}

type Server struct {
	ID int
}

type ProvisionRequest struct {
	User       string   `json:"user"`
	Components []string `json:"components"`
}

func (d Database) Provision() string {
	return fmt.Sprintf("Provisioning Database: %s\n", d.Name)
}

func (s Server) Provision() string {
	return fmt.Sprintf("Provisioning Server: %d\n", s.ID)
}

func PostHandler(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "Only POST allowed", http.StatusMethodNotAllowed)
		return
	}

	defer r.Body.Close()

	// create an empty struct
	var req ProvisionRequest

	// decode the r.Body and fill the empty struct value
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		http.Error(w, "Bad JSON", http.StatusBadRequest)
		return
	}

	// provision iteams based on the request
	var items []Provisioner

	// check if the user filed is empty
	if req.User == "" {
		http.Error(w, "Field 'user' is required", http.StatusBadRequest)
		return
	}

	// check user demands and create object based on that
	for _, comp := range req.Components {
		switch comp {
		case "database":
			items = append(items, Database{Name: "Production_DB"})
		case "server":
			items = append(items, Server{ID: 101})
		}
	}

	var wg sync.WaitGroup                    // counter
	reports := make(chan string, len(items)) // channel to stream the data

	// provision the object in concurrency
	for _, item := range items {
		wg.Add(1)
		go func(prov Provisioner) {
			defer wg.Done()
			reports <- prov.Provision()
		}(item)
	}

	// close the channel
	wg.Wait()
	close(reports)

	fmt.Printf("User %s wants to provision: %v\n", req.User, req.Components)
	fmt.Fprint(w, "JSON Received!\n")
	fmt.Fprint(w, "=== Provisioning Components ===\n")
	for msg := range reports {
		fmt.Fprintf(w, "Reports: %s", msg)
	}
}

func main() {
	http.HandleFunc("/provision", PostHandler)
	fmt.Println("Platform API listening on :8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
