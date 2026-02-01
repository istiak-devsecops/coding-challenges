# see if the password contains at least one special character.

password_chars = set("DevOps123!")
required_chars = set("!@#$%^&*")

if password_chars & required_chars:
    print("Password contains a special character")
else:
    print("Password doesn't contains any special character!")


