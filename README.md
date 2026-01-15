# Password Validator (Python)

This is a simple Python program that validates a user-entered password based on basic security rules.
The project is designed using core Python concepts and is ideal for beginners who want to understand string handling and validation logic.

---

## Project Description

The Password Validator checks whether a password is strong enough by validating its length and character composition.
It ensures that the password contains:

* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* A valid length range

Based on these conditions, the program displays whether the password is valid or invalid.

---

## Features

* Accepts password input from the user
* Checks password length
* Validates uppercase letters
* Validates lowercase letters
* Validates numeric digits
* Displays clear validation result
* Simple and readable logic

---

## Validation Rules

A password is considered **valid** if:

* Length is greater than 8 and less than 15 characters
* Contains at least one uppercase character
* Contains at least one lowercase character
* Contains at least one digit

If any of these conditions fail, the password is marked as invalid.

---

## Concepts Used

This project is built using fundamental Python concepts:

### Data Types

* Strings
* Integers
* Booleans

### Control Statements

* for loop
* if / else

### String Methods

* isupper()
* islower()
* isdigit()
* len()

### Programming Concepts

* User input handling
* Conditional logic
* Boolean flags
* Character-wise string traversal

---

## Sample Execution

Enter Your Password: Hello1234
Password is valid

Enter Your Password: hello
Password is invalid! Need to Make More Strong Password

---

## Project Structure

Password_Validator.py

---

## Possible Improvements

* Add special character validation
* Show exact reason why password is invalid
* Allow user to retry until valid password is entered
* Mask password input
* Convert into a reusable function

---

## Author

Meet Tailor
Python Programming Learner
GitHub: [https://github.com/MeetTailor-Data](https://github.com/MeetTailor-Data)

---

## License

This project is created for learning and educational purposes.

---

## Status

Project Status: Completed
Last Updated: 2026
