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

func CheckPort(port int) bool {
	if port < 1024 {
		fmt.Println("standard non privileged ports.")
		return false
	}

	if port > 65535 {
		fmt.Println("standard non-privilaged ports.")
		return false
	}

	if port == 8080 {
		fmt.Println("Note: 8080 is common, ensuring non conflicts...")
		return true
	}
	return true
}
