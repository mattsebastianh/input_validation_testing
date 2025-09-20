# Input Validation Testing Project

A Python project demonstrating secure input validation techniques with comprehensive unit testing.

## Table of Contents

- [Input Validation Testing Project](#input-validation-testing-project)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Features](#features)
  - [Files](#files)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Security Benefits](#security-benefits)
  - [License](#license)

## Purpose

This project serves as a comprehensive guide for implementing secure input validation in Python applications. It demonstrates how to protect against common security vulnerabilities while maintaining user-friendly input handling.


## Features

- **Username Validation**: Accepts only alphanumeric characters and underscores
- **Password Validation**: Enforces minimum 8-character length requirement
- **Email Validation**: Uses regex pattern matching for proper email format
- **SQL Query Validation**: Blocks potentially destructive operations (DROP, DELETE)

## Files

- `user_input.py`: Core validation functions
- `test_validation.py`: Comprehensive unit tests for all validation functions

## Usage

```python
from user_input import get_username, get_password, get_email, get_sql_query

# Example usage
username = get_username("john_doe123")  # Valid
password = get_password("securepass123")  # Valid
email = get_email("user@example.com")  # Valid
query = get_sql_query("SELECT * FROM users")  # Valid
```

## Running Tests

Execute the test suite to verify all validation functions:

```bash
python test_validation.py
```

## Security Benefits

- Prevents SQL injection attacks
- Enforces strong password policies
- Validates email format integrity
- Sanitizes username input to prevent special character exploits

## License

This project is licensed under the terms of the LICENSE file in this repository. See [LICENSE](LICENSE) for details.
