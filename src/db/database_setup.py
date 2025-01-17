import os
import sqlite3


class DatabaseSetup:
    def __init__(self):
        pass

    def execute_sql_script(self, connection: sqlite3.Connection, script_path: str):
        with open(script_path, "r") as sql_file:
            sql_script = sql_file.read()
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()

    def initialize_database(self, db_path: str, schema_path: str):

        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        connection = sqlite3.connect(db_path)

        try:

            print(f"Applying schema from {schema_path}...")
            self.execute_sql_script(connection, schema_path)
            print(f"Database initialized successfully at {db_path}.")

        except Exception as e:
            print(f"Error while initializing the database: {e}")

        finally:
            connection.close()
