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

// === Http Handler Logic ===
func httpHandler(w http.ResponseWriter, r *http.Request) {
	// === Guard Method ===
	if r.Method != http.MethodPost {
		http.Error(w, "Only POST method allowed", http.StatusMethodNotAllowed)
		return
	}

	// === Decode User Request ===
	var req ProvisionRequest
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil {
		http.Error(w, "Bad JSON Data", http.StatusBadRequest)
		return
	}

	// === User Validation ===
	if req.User == "" {
		http.Error(w, "User is missing", http.StatusBadRequest)
		return
	}

	// === Components slice ===
	var items []Provisioner
	var finalResults []string // store users unknow components request in a slice

	for _, comp := range req.Components {
		switch comp {
		case "database":
			items = append(items, &Database{Name: "redis"})
		case "server":
			items = append(items, &Server{ID: 719239})
		default:
			finalResults = append(finalResults, fmt.Sprintf("%s not supported", comp))
		}
	}

	// === TimeOut and Concurrency Logic ===
	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second) // Set the timeout Limit
	defer cancel()                                                 // stop the function when work is done

	var wg sync.WaitGroup                    // The counter
	reports := make(chan string, len(items)) // User response channel

	// concurrency
	for _, item := range items {
		wg.Add(1)
		go func(p Provisioner) {
			defer wg.Done()
			reports <- p.Provision()
		}(item)
	}

	// Watcher
	done := make(chan struct{}) // work as a signal to validate if all task done gracefully
	go func() {
		wg.Wait()
		close(done)
	}()

	// === TimeOut and Success Logic
	select {
	case <-ctx.Done():
		// hit the timeout logic
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusGatewayTimeout)
		json.NewEncoder(w).Encode(ProvisionResponse{
			Status:  "TimeOut",
			Message: "Taking too long",
			Results: finalResults,
		})
		return
	// success full execution
	case <-done:
		close(reports) // close the reports channel
		for msg := range reports {
			finalResults = append(finalResults, msg)
		}
	}

	// === Final Reports ===

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(ProvisionResponse{
		Status:  "success",
		Message: fmt.Sprintf("Task handled for %s", req.User),
		Results: finalResults,
	})
}

// Main Logic
func main() {
	http.HandleFunc("/provision", httpHandler)
	log.Println("Platform API listening on :9000")
	log.Fatal(http.ListenAndServe(":9000", nil))
}
