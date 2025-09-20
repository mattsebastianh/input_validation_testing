import unittest
from user_input import get_username, get_password, get_email, get_sql_query  # Update with your actual module name

class TestInputValidation(unittest.TestCase):

    def test_get_username_valid(self):
        self.assertEqual(get_username("valid_username"), "valid_username")

    def test_get_username_invalid(self):
        with self.assertRaises(ValueError):
            get_username("invalid username!")  # space and special character

    def test_get_password_valid(self):
        self.assertEqual(get_password("validpassword"), "validpassword")

    def test_get_password_invalid(self):
        with self.assertRaises(ValueError):
            get_password("short")  # less than 8 characters

    def test_get_email_valid(self):
        self.assertEqual(get_email("test@example.com"), "test@example.com")

    def test_get_email_invalid(self):
        with self.assertRaises(ValueError):
            get_email("invalid-email")  # not a valid email format

    def test_get_sql_query_valid(self):
        self.assertEqual(get_sql_query("SELECT * FROM users"), "SELECT * FROM users")

    def test_get_sql_query_invalid(self):
        with self.assertRaises(ValueError):
            get_sql_query("DROP TABLE users")  # destructive operation

if __name__ == "__main__":
    unittest.main()
