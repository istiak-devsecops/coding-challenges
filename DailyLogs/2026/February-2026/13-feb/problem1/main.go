package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
)

// Blueprints
type Provisioner interface {
	Provision() string
}

type Database struct{ Name string }
type Server struct{ ID int }

func (d Database) Provision() string {
	return fmt.Sprintf("Provisioning Database: %s", d.Name)
}

func (s Server) Provision() string {
	return fmt.Sprintf("Provisioning Server: %d", s.ID)
}

// JSON mapping
type ProvisionRequest struct {
	User       string   `json:"user"`
	Components []string `json:"components"`
}

type ProvisionResponse struct {
	Status  string   `json:"status"`
	Message string   `json:"message"`
	Results []string `json:"results"`
}

// The Handler
func PostHandler(w http.ResponseWriter, r *http.Request) {
	// Guard Method
	if r.Method != http.MethodPost {
		http.Error(w, "Only POST allowed", http.StatusMethodNotAllowed)
		return
	}

	defer r.Body.Close()

	// Decode Input
	var req ProvisionRequest
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		http.Error(w, "Bad JSON", http.StatusBadRequest)
		return
	}

	// Mapping Logic
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

	// Execution
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

	// Collect Results into a slice
	var results []string
	for msg := range reports {
		results = append(results, msg)
	}

	// Encode output as JSON
	w.Header().Set("Content-Type", "application/json") // tell the client its a JSON
	resp := ProvisionResponse{
		Status:  "Success",
		Message: fmt.Sprintf("Tasks completed for user: %s", req.User),
		Results: results,
	}

	json.NewEncoder(w).Encode(resp)
}

// Main function
func main() {
	http.HandleFunc("/provision", PostHandler)
	fmt.Println("Platform API listening on :8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
