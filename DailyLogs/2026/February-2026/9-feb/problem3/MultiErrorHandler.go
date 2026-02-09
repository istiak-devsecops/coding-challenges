package main

import (
	"errors"
	"fmt"
)

type RequestError struct {
	StatusCode int
	Err        error
}

type ValidationError struct {
	Field string
}

// Request method
func (r RequestError) Error() string {
	return fmt.Sprintf("Status %d: %v", r.StatusCode, r.Err)
}

// validation method
func (v ValidationError) Error() string {
	return fmt.Sprintf("Set %s ID", v.Field)
}

// The manager
func FetchResource(id string) error {
	if id == "missing" {
		return RequestError{StatusCode: 404, Err: errors.New("Not Found")}
	}

	if id == "" {
		return ValidationError{Field: "Field Name"}
	}

	return errors.New("unexpected error")
}

// Main logic
func main() {
	err := FetchResource("missing")

	if err != nil {
		var reqErr RequestError
		var valErr ValidationError

		if errors.As(err, &reqErr) {
			fmt.Printf("Status Code: %d\n", reqErr.StatusCode)
		} else if errors.As(err, &valErr) {
			fmt.Printf("Please check the field: [%s]\n", valErr.Field)
		} else {
			fmt.Printf("System Error: %v\n", err)
		}

	}
}
