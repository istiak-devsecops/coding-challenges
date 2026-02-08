package main

import "fmt"

type Downloader interface {
	Download(url string)
}

type Uploader interface {
	Upload(file string)
}

type CloudTool interface {
	Downloader
	Uploader
}

type S3Manager struct {
	// empty
}

func (s S3Manager) Download(url string) {
	fmt.Printf("Downloading from: %s\n", url)
}

func (s S3Manager) Upload(file string) {
	fmt.Printf("Uploading file: %s\n", file)
}

func SyncData(tool CloudTool) {
	tool.Download("s3://my-bucket/config.json")
	tool.Upload("local-backup.zip")
}

func main() {
	manager := S3Manager{}
	SyncData(manager)
}
