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

// bluetprint for struct
type Database struct{ Name string }
type Server struct{ ID int }

func (d Database) Provision() string { return fmt.Sprintf("Provisioning Database: %s\n", d.Name) }
func (s Server) Provision() string   { return fmt.Sprintf("Provisioning Server: %d\n", s.ID) }

// Data Transfer object
type ProvisionRequest struct {
	User       string   `json:"user"`
	Components []string `json:"components"`
}

type ProvisionResponse struct {
	Status  string   `json:"status"`
	Message string   `json:"message"`
	Results []string `json:"results"`
}

// The Logic Handler
func httpHandler(w http.ResponseWriter, r *http.Request) {
	// The gurad clause to check if the method is POST
	if r.Method != http.MethodPost {
		http.Error(w, "Only Post Allowed", http.StatusMethodNotAllowed)
		return
	}

	// Parse the incoming JSON body into your ProvisionRequest struct.
	defer r.Body.Close()                        // close the body
	var req ProvisionRequest                    // define an empty struct
	err := json.NewDecoder(r.Body).Decode(&req) // decode the json data and assing it to req
	if err != nil {
		http.Error(w, "Bad JSON data.", http.StatusBadRequest) // define error status
	}

	// Validator. Ensure required fields (like User) aren't empty.
	var items []Provisioner // define an empty struct
	if req.User == "" {
		http.Error(w, "User required", http.StatusBadRequest)
		return
	}

	// Factory/Mapper. Loop through the string slice from the request
	// "convert" those strings into a slice of your Provisioner interface.
	for _, comp := range req.Components {
		switch comp {
		case "database":
			items = append(items, Database{Name: "redis"})
		case "server":
			items = append(items, Server{ID: 721892})
		}
	}

	// Concurrency Logic
	var wg sync.WaitGroup                    // counter to track the active task
	reports := make(chan string, len(items)) // pipe to collect results from different thread

	// Provision the object in concurrency
	for _, item := range items {
		wg.Add(1)
		go func(p Provisioner) {
			defer wg.Done()
			reports <- p.Provision()
		}(item)

	}

	// close the channel
	wg.Wait()
	close(reports)

	// loop through the reports and put them into a slice
	var results []string
	for msg := range reports {
		results = append(results, msg)
	}

	// Encode response to JSON format
	w.Header().Set("Content-Type", "application/json")
	resp := ProvisionResponse{
		Status:  "success",
		Message: fmt.Sprintf("Task Completed for user: %s", req.User),
		Results: results,
	}

	json.NewEncoder(w).Encode(resp)
}

// Main function
func main() {
	http.HandleFunc("/provision", httpHandler)
	fmt.Println("Platform API listening on :8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
