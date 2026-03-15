package main

import (
	"math"
	"strings"
)

type PaymentProcessor interface {
	Process(amount float64)
}

type CreditCard struct {
	balance float64
}

type PayPal struct {
	email   string
	balance float64
}

func NewCreditCard(amount float64) *CreditCard {

	if amount < 0 {
		amount = 0
	}

	return &CreditCard{
		math.Max(0, amount),
	}
}

func NewPayPal(email string, amount float64) *PayPal {

	safeAmount := math.Max(0, amount)

	if !strings.Contains(email, "@") {
		email = "invalid-email@example.com"
	}

	return &PayPal{
		email:   email,
		balance: safeAmount,
	}
}
