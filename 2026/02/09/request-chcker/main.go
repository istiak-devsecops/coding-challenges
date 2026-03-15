package main

import (
	"errors"
	"fmt"
)

type RequestError struct {
	StatusCode int
	Err        error
}

func (r RequestError) Error() string {
	return fmt.Sprintf("Status %d: %v", r.StatusCode, r.Err)
}

func FetchResource(id string) error {
	if id == "valid" {
		return nil
	}

	if id == "missing" {
		return RequestError{StatusCode: 404, Err: errors.New("Not found")}
	}

	return errors.New("unknown id")
}

func main() {
	err := FetchResource("missing")

	if err != nil {
		var reqErr RequestError // creating a empty object with RequestError struct
		// errors.As looking inside err variable
		// &reqErr points to the location of the data err variable got
		if errors.As(err, &reqErr) {
			fmt.Printf("Detected API Error! Code: %d\n", reqErr.StatusCode)
		} else {
			fmt.Println("Generic Error:", err)
		}
	}
}
