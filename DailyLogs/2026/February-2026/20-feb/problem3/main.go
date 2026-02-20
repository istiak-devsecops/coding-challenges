package main

import (
	"fmt"
	"problem3/auth"
)

func main() {
	newAcc := auth.NewAccount("intern_dev", false)

	err := newAcc.DeleteSystem()
	if err != nil {
		wrapp := fmt.Errorf("Security_violation_at_layer_1: %w", err)
		fmt.Println(wrapp)
	}
}
