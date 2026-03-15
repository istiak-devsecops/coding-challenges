package main

import (
	"fmt"
	"net/http"
	"sync"
)

type Provisioner interface {
	Provision() string
}

// Database struct and methods
type Database struct {
	Name string
}

func (d Database) Provision() string {
	return fmt.Sprintf("Provisioning %s", d.Name)
}

// Server Struct and methods
type Server struct {
	Name string
}

func (s Server) Provision() string {
	return fmt.Sprintf("Deploying server: %s", s.Name)
}

// The Handler
func ProvisionHandler(w http.ResponseWriter, r *http.Request) {
	var wg sync.WaitGroup
	results := make(chan string, 2)

	// create out iteams to provision
	items := []Provisioner{
		Database{Name: "Postgres-Main"},
		Server{Name: "API-Gateway"},
	}

	// launch the workers
	for _, item := range items {
		wg.Add(1)
		go func(p Provisioner) {
			defer wg.Done()

			msg := p.Provision()
			results <- msg
		}(item)
	}

	// The cleaner code
	go func() {
		wg.Wait()
		close(results)
	}()

	fmt.Fprintf(w, "== IDP Provisioning Report ===")
	for res := range results {
		fmt.Fprintln(w, "-", res)
	}

}
