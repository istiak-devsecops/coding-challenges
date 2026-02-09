package main

import "fmt"

// Interface
type Starter interface {
	Start() error
}

type Checker interface {
	Check() bool
}

type Resource interface {
	Starter
	Checker
}

// K8sApp Structs and Methods
type K8sApp struct {
	PodName string
}

func (k K8sApp) Start() error {
	fmt.Printf("Scaling up pods for [%s]\n", k.PodName)
	return nil
}

func (k K8sApp) Check() bool {
	return true
}

// Database Structs and Methods
type Database struct {
	ConnString string
}

func (d Database) Start() error {
	fmt.Printf("Opening connection to [%s]\n", d.ConnString)
	return nil
}

func (d Database) Check() bool {
	return false
}

// The Orchestrator(manager)
func Reconcile(r Resource) {
	err := r.Start()

	if err != nil {
		fmt.Printf("ERROR: %s\n", err)
		return
	}

	if r.Check() {
		fmt.Println("Resource is stable")
	} else {
		fmt.Println("CRITICAL: Resource is unhealthy!")
	}
}

// main logic
func main() {
	kApp := K8sApp{PodName: "Test Pod1"}
	dataB := Database{ConnString: "Test Database"}

	Reconcile(kApp)
	Reconcile(dataB)
}
