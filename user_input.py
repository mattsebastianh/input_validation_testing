import re

def get_username(username):
    if re.match("^[a-zA-Z0-9_]*$", username):
        return username
    else:
        raise ValueError("Invalid username. Only alphanumeric characters and underscores are allowed.")

def get_password(password):
    if len(password) >= 8:
        return password
    else:
        raise ValueError("Invalid password. It must be at least 8 characters long.")

def get_email(email):
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return email
    else:
        raise ValueError("Invalid email address format.")

def get_sql_query(query):
    if "DROP" not in query.upper() and "DELETE" not in query.upper():
        return query
    else:
        raise ValueError("Invalid query. Destructive operations are not allowed.")
