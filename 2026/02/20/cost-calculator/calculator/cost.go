package calculator

import "errors"

type Resource struct{ Price int }

func Calculator(r Resource) error {
	if r.Price < 0 {
		return errors.New("Price can not be less than zero.")
	}
	return nil
}
