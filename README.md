# Password Validation Program (Python)

A **Python-based password validation program** that checks whether a password meets basic strength requirements.
This project is ideal for beginners to understand **string handling, loops, and conditional logic** in Python.

---

## Project Description

This program takes a password as input from the user and validates it based on predefined rules such as:

* Password length
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of digits

The program then informs the user whether the password is **valid or needs to be strengthened**.

---

## Validation Rules

A password is considered **valid** if it satisfies all the following conditions:

* Length must be **greater than 8 and less than 15 characters**
* Must contain **at least one uppercase letter**
* Must contain **at least one lowercase letter**
* Must contain **at least one digit**

---

## Features

* User-friendly input prompt
* Real-time password validation
* Uses built-in string methods
* Simple and readable logic
* Beginner-friendly implementation

---

## Concepts Used

### Data Types

* Strings
* Integers
* Booleans

### Control Statements

* `for` loop
* `if` conditions

### Python Concepts

* String traversal
* Built-in string methods:

  * `isupper()`
  * `islower()`
  * `isdigit()`
* Logical operators
* Input and output handling

---

## Project Structure

```
password-validator/
│
├── PasswordValidator.py   # Main program file
└── README.md              # Project documentation
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on your system

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the program using:

```bash
python PasswordValidator.py
```

---

## Sample Output

### Valid Password

```
Enter Your Password: Strong123
Password is valid
```

### Invalid Password

```
Enter Your Password: weak
Password is invalid! Need to Make More Strong Password
```

---

## Edge Cases Handled

* Password too short or too long
* Missing uppercase letter
* Missing lowercase letter
* Missing digit

---

## Future Improvements

* Add special character validation
* Mask password input
* Show specific error messages for failed conditions
* Convert into reusable function

---

## Author

**Meet Tailor**
Python Programming Learner
GitHub: [https://github.com/MeetTailor-Data](https://github.com/MeetTailor-Data)

---

## License

This project is created for learning and educational purposes.

---

## Status

* Project Status: Completed
* Last Updated:
