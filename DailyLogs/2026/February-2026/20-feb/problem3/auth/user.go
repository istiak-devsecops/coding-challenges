package auth

import "errors"

type Account struct {
	Username string
	isAdmin  bool
}

func NewAccount(name string, admin bool) *Account {
	return &Account{
		Username: name,
		isAdmin:  admin,
	}
}

func (a *Account) DeleteSystem() error {
	if a.isAdmin == false {
		return errors.New("unauthorized!")
	}
	return nil
}
