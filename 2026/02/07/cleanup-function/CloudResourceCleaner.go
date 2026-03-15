package main

import "fmt"

type Resource interface {
	Delete() error
}

type S3Bucket struct {
	BucketName string
	IsLocker   bool
}

func (s S3Bucket) Delete() error {
	fmt.Printf("Emptying and deleting bucket: %s\n", s.BucketName)
	return nil
}

type ComputeInstance struct {
	InstanceID string
}

func (c ComputeInstance) Delete() error {
	fmt.Printf("Terminating instance: %s\n", c.InstanceID)
	return nil
}

func CleanUp(r Resource) {
	_ = r.Delete()
}

func main() {
	bucket1 := S3Bucket{BucketName: "user-photos-prod"}
	bucket2 := S3Bucket{BucketName: "temp-logs"}
	server1 := ComputeInstance{InstanceID: "i-099abc123"}

	resources1 := []Resource{bucket1, server1, bucket2}

	for _, res := range resources1 {
		CleanUp(res)
	}
}
