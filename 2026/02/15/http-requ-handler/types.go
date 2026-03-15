package main

import (
	"fmt"
)

type Provisioner interface {
	Provision() string
}

// bluetprint for struct
type Database struct{ Name string }
type Server struct{ ID int }

func (d Database) Provision() string { return fmt.Sprintf("Provisioning Database: %s", d.Name) }
func (s Server) Provision() string   { return fmt.Sprintf("Provisioning Server: %d", s.ID) }

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
