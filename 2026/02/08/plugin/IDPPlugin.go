package main

import "fmt"

type Provider interface {
	Provision(id string) error
	GetStatus() string
}

// K8s methods
type K8sCluster struct {
	Namespace string
}

func (k K8sCluster) Provision(id string) error {
	fmt.Printf("Creating Pods in [%s] for ID [%s]\n", k.Namespace, id)
	return nil
}

func (k K8sCluster) GetStatus() string {
	return "Pods are Running."
}

//Blob Storage Methods
type BlobStorage struct {
	Region string
}

func (b BlobStorage) Provision(id string) error {
	fmt.Printf("Allocating bucket in region [%s] for ID [%s]\n", b.Region, id)
	return nil
}

func (b BlobStorage) GetStatus() string {
	return fmt.Sprintf("Storage is Active in [%s]\n", b.Region)
}

func RunPipeline(p Provider, id string) {
	err := p.Provision(id)

	if err != nil {
		fmt.Printf("Provisioning failed: %v\n", err)
		return
	}

	status := p.GetStatus()
	fmt.Println("Status:" + status)

}

func main() {
	inventory := map[string]Provider{
		"web-app": K8sCluster{Namespace: "prod"},
		"backups": BlobStorage{Region: "us-east-1"},
	}

	for id, provider := range inventory {
		fmt.Printf("Starting pipeline for %s\n", id)
		RunPipeline(provider, id)
	}
}
