package main

import "fmt"

type Service struct {
	Name       string
	ErrorCount int
}

// error recorder method
func (s *Service) RecordError() {
	s.ErrorCount++
}

// bool method
func (s Service) IsHealthy() bool {
	if s.ErrorCount > 0 {
		return false
	}
	return true
}

func main() {
	authApi := Service{Name: "Auth-API", ErrorCount: 0}
	paymentGateway := Service{Name: "Payment-Gateway", ErrorCount: 0}

	// Checking Auth API
	fmt.Println("Before Error Increment.")
	if authApi.IsHealthy() {
		fmt.Printf("Initial health for %s: is good.\n", authApi.Name)
	} else {
		fmt.Printf("Service %s is Down\n", authApi.Name)
	}

	authApi.RecordError() // increment the error

	// Checking Auth API
	fmt.Println("After Error Increment.")
	if authApi.IsHealthy() {
		fmt.Printf("Initial health for %s: is good\n", authApi.Name)
	} else {
		fmt.Printf("Service %s is Down\n", authApi.Name)
	}

	// Checking Payment Gateway
	if paymentGateway.IsHealthy() {
		fmt.Printf("Service %s is Running\n", paymentGateway.Name)
	} else {
		fmt.Printf("Service %s is CRITICAL\n", paymentGateway.Name)
	}
}
