"""
This script imports necessary modules for database interactions.

Modules imported:
    - database: A custom module providing database functionality.
"""

from dataclasses import dataclass

from yoshi import database


@dataclass
class Account:
    """Represents a login account."""

    uuid: str
    application: str
    username: str
    password: str
    url: str

    def display_account(self) -> None:
        """Print the account details."""
        print("ID:", self.uuid)
        print("Application:", self.application)
        print("Username:", self.username)
        print("Password:", self.password)
        print("URL:", self.url)

    def save_account(self) -> None:
        """Save the account details to the database."""
        database.add_account(
            self.uuid, self.application, self.username, self.password, self.url
        )

    def delete_account(self) -> bool:
        """Delete the account from the database.

        Returns:
            bool: True if the deletion was successful.
        """
        database.delete_account(self.uuid)
        return True
