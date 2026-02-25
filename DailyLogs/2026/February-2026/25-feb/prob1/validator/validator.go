package validator

import "fmt"

func CheckName(name string) bool {
	if name == "" {
		fmt.Println("Name can not be empty")
		return false
	}

	if len(name) < 3 {
		fmt.Println("Name should be at least 3 character long.")
		return false
	}

	if len(name) > 20 {
		fmt.Println("Name can not be more than 20 char long.")
		return false
	}
	return true

}
