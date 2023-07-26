# database.py - Database Module

class Database:
    def __init__(self):
        self.data = {}

    def insert_data(self, key, value):
        # Placeholder for inserting data into the database
        self.data[key] = value
        print(f"Data with key '{key}' has been inserted into the database.")

    def retrieve_data(self, key):
        # Placeholder for retrieving data from the database
        if key in self.data:
            print(f"Retrieving data with key '{key}': {self.data[key]}")
            return self.data[key]
        else:
            print(f"Error: Data with key '{key}' not found.")
            return None

    def delete_data(self, key):
        # Placeholder for deleting data from the database
        if key in self.data:
            del self.data[key]
            print(f"Data with key '{key}' has been deleted from the database.")
        else:
            print(f"Error: Data with key '{key}' not found.")

# Example usage:
if __name__ == "__main__":
    database = Database()

    # Insert data into the database
    database.insert_data("name", "TALON Project")
    database.insert_data("version", "1.0")
    database.insert_data("status", "active")

    # Retrieve data from the database
    name = database.retrieve_data("name")
    version = database.retrieve_data("version")

    # Delete data from the database
    database.delete_data("status")
