package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
	"time"
)

func httpHandler(w http.ResponseWriter, r *http.Request) {
	// === GUARD & DECODE ===
	if r.Method != http.MethodPost {
		http.Error(w, "Only POST allowed", http.StatusMethodNotAllowed)
		return
	}

	var req ProvisionRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Bad JSON data", http.StatusBadRequest)
		return
	}

	// === VALIDATE & MAP ===
	if req.User == "" {
		http.Error(w, "User required", http.StatusBadRequest)
		return
	}

	var items []Provisioner
	var finalResults []string // Start collecting results early (Partial Success)

	for _, comp := range req.Components {
		switch comp {
		case "database":
			items = append(items, &Database{Name: "redis"})
		case "server":
			items = append(items, &Server{ID: 721892})
		default:
			finalResults = append(finalResults, fmt.Sprintf("Error: %s not supported", comp))
		}
	}

	// === CONCURRENCY ENGINE ===
	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
	defer cancel()

	reports := make(chan string, len(items))
	var wg sync.WaitGroup

	for _, item := range items {
		wg.Add(1)
		go func(p Provisioner) {
			defer wg.Done()
			reports <- p.Provision()
		}(item)
	}

	// The "Watcher" Goroutine
	done := make(chan struct{})
	go func() {
		wg.Wait()
		close(done) // This tells the select block we are finished
	}()

	// === THE RACE (TIMEOUT vs SUCCESS) ===
	select {
	case <-ctx.Done():
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusGatewayTimeout)
		json.NewEncoder(w).Encode(ProvisionResponse{
			Status:  "Partial Timeout",
			Message: "Work took too long",
			Results: finalResults,
		})
		return

	case <-done:
		close(reports) // Safe to close now because wg.Wait() is done
		for msg := range reports {
			finalResults = append(finalResults, msg)
		}
	}

	// === FINAL RESPONSE ===
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(ProvisionResponse{
		Status:  "success",
		Message: fmt.Sprintf("Tasks handled for %s", req.User),
		Results: finalResults,
	})
}

// Main Logic
func main() {
	http.HandleFunc("/provision", httpHandler)
	log.Println("Platform API listening on :8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
