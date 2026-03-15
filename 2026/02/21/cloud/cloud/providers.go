package cloud

import (
	"fmt"
	"time"
)

// === S3Bucket ===
type S3Bucket struct{ name, data string }

func NewS3(name, data string) *S3Bucket {
	return &S3Bucket{
		name: name,
		data: data,
	}
}

func (s *S3Bucket) Upload() string {
	time.Sleep(100 * time.Millisecond)
	return fmt.Sprintf("Provisioning %s S3Bucket | Data: %s", s.name, s.data)
}

// === AzureBlob ===
type AzureBlob struct{ name, data string }

func NewAzure(name, data string) *AzureBlob {
	return &AzureBlob{
		name: name,
		data: data,
	}
}

func (a *AzureBlob) Upload() string {
	time.Sleep(100 * time.Millisecond)
	return fmt.Sprintf("Provisioning %s AzureBlob | Data: %s", a.name, a.data)
}
