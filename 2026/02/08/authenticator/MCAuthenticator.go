package main

import (
	"fmt"
	"strings"
)

type CloudProvider interface {
	Login() error
}

// AWS methods
type AWS struct {
	AccessKey string
}

func (a AWS) Login() error {
	if a.AccessKey == "" {
		return fmt.Errorf("AWS Login Failed: No Access Key.")
	}
	fmt.Println("AWS Login Successful.")
	return nil

}

// GCP Methods
type GCP struct {
	ServiceAccountFile string
}

func (g GCP) Login() error {
	if !strings.HasSuffix(g.ServiceAccountFile, ".json") {
		return fmt.Errorf("Not a JSON file.")
	}
	return nil

}

// The Manager
func Connect(c CloudProvider) {
	err := c.Login()
	if err != nil {
		fmt.Printf("STOP: Platform cannot connect to cloud: %v\n", err)
		return
	}

	fmt.Println("Successfully connected!")
}

func main() {
	key := AWS{AccessKey: "HSJKDYJSKJDIW12JS78SJ8"}
	file := GCP{ServiceAccountFile: "gcp.json"}

	Connect(key)
	Connect(file)
}
