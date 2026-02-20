package main

import (
	"fmt"
	"problem2/calculator"
)

func main() {
	price1 := calculator.Resource{Price: -11}
	fmt.Println("Costing Price: ", +price1.Price)

	err := calculator.Calculator(price1)

	if err != nil {
		wrapperErr := fmt.Errorf("billing_service_failure: %w", err)
		fmt.Println(wrapperErr)
		return
	}

}
