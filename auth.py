# auth.py - Authentication and Authorization Module

import hashlib
import secrets

class Authentication:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        # Placeholder for registering a new user
        if username in self.users:
            print(f"Error: User '{username}' already exists.")
        else:
            salt = secrets.token_hex(16)
            hashed_password = self._hash_password(password, salt)
            self.users[username] = {"hashed_password": hashed_password, "salt": salt}
            print(f"User '{username}' has been registered successfully.")

    def authenticate_user(self, username, password):
        # Placeholder for authenticating a user
        if username not in self.users:
            print(f"Error: User '{username}' not found.")
            return False

        stored_hashed_password = self.users[username]["hashed_password"]
        salt = self.users[username]["salt"]
        hashed_password = self._hash_password(password, salt)

        if stored_hashed_password == hashed_password:
            print(f"User '{username}' has been authenticated successfully.")
            return True
        else:
            print(f"Error: Authentication failed for user '{username}'.")
            return False

    def _hash_password(self, password, salt):
        # Helper method for hashing the password using SHA-256
        password_with_salt = f"{password}{salt}".encode('utf-8')
        hashed_password = hashlib.sha256(password_with_salt).hexdigest()
        return hashed_password

# Example usage:
if __name__ == "__main__":
    auth = Authentication()

    # Register new users
    auth.register_user("user1", "password123")
    auth.register_user("user2", "qwerty456")
    auth.register_user("user1", "p@ssw0rd")  # User1 already exists

    # Authenticate users
    auth.authenticate_user("user1", "password123")
    auth.authenticate_user("user2", "invalid_password")
