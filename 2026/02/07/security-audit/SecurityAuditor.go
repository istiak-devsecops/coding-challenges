package main

import "fmt"

// Interface with two methods
type Auditable interface {
	CheckSecurity() error
	GetName() string
}

type Database struct {
	Name     string
	IsPublic bool
}

type Firewall struct {
	Name      string
	OpenPorts int
}

// Database Method
func (d Database) GetName() string {
	return d.Name
}

func (d Database) CheckSecurity() error {
	if d.IsPublic {
		return fmt.Errorf("DATABASE IS PUBLIC - HIGH RISK")
	}
	return nil
}

// Firewall Methods
func (f Firewall) GetName() string {
	return f.Name
}

func (f Firewall) CheckSecurity() error {
	if f.OpenPorts > 3 {
		return fmt.Errorf("TOO MANY PORTS (%d) OPEN", f.OpenPorts)
	}
	return nil
}

// The Auditor
func RunAudit(a Auditable) {
	fmt.Printf("Auditing resource: [%s]\n", a.GetName())

	err := a.CheckSecurity()

	if err != nil {
		fmt.Printf("!Warning: %v\n", err)
	} else {
		fmt.Println("Security Check Passed.")
	}
	fmt.Println("-------------------")
}

func main() {
	db := Database{Name: "UserInventory", IsPublic: true}
	fw := Firewall{Name: "mainGateway", OpenPorts: 5}

	RunAudit(db)
	RunAudit(fw)
}
