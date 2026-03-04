package main

import (
	"context"
	"fmt"
	"log"
	"path/filepath"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"k8s.io/client-go/util/homedir"
)

func main() {
	// 1. Setup Kubeconfig Path
	var kubeconfig string
	if home := homedir.HomeDir(); home != "" {
		kubeconfig = filepath.Join(home, ".kube", "config")
	} else {
		log.Fatal("Could not find home directory")
	}

	// 2. Build Configuration
	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
	if err != nil {
		log.Fatalf("Error building kubeconfig: %v", err)
	}

	// 3. Create Clientset
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatalf("Error creating clientset: %v", err)
	}

	fmt.Println("🚀 Starting Namespace Audit...")
	namespaces, err := clientset.CoreV1().Namespaces().List(context.TODO(), metav1.ListOptions{})
	if err != nil {
		log.Fatalf("Failed to list namespaces: %v", err)
	}

	for _, ns := range namespaces.Items {

		isInactive := checkNamespaceInactivity(clientset, ns.Name)

		if isInactive {
			fmt.Printf("⚠️  Namespace [%s] appears inactive (No deployment updates in 30 days)\n", ns.Name)
		}
	}
}

func checkNamespaceInactivity(clientset *kubernetes.Clientset, nsName string) bool {

	return false
}
