import os
from typing import Any
import unittest
from fs import File
from record import Record

class TestRecord(unittest.TestCase):
    """Unit tests for the Record class to test data manipulation and file-based storage."""

    def delete_file(self, filename: str = "data.json") -> bool:
        """Delete a file if it exists.

        Args:
            filename (str): The name of the file to delete (default is 'data.json').

        Returns:
            bool: True if the file was deleted, False if it didn't exist.
        """
        if os.path.isfile(filename):
            os.remove(filename)
            return True
        return False

    def test_add(self):
        """Test the 'add' method to ensure records are added and stored correctly.

        Verifies that:
        - Records are added to the internal storage.
        - The total count of added records is correct.
        """
        test_data: list[list[Any]] = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
            [84324.234, "expense", "2021-4-1", "Empty"],
        ]  # amount, category, date, description
        record = Record()

        for item in test_data:
            record.add(amount=item[0], category=item[1], date=item[2], description=item[3])
        
        # Check that the number of added records is as expected
        self.assertEqual(len(record.get()), len(test_data))

        self.delete_file()

    def test_update(self):
        """Test the 'update' method to ensure records can be updated correctly.

        Verifies that:
        - Records can be updated by index.
        - Updated records are saved correctly to the file.
        """
        test_data: list[list[Any]] = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
            [84324.234, "expense", "2021-4-1", "Empty"],
        ]  # amount, category, date, description
        record = Record()

        for item in test_data:
            record.add(amount=item[0], category=item[1], date=item[2], description=item[3])

        expected_test_data: dict[str, list[dict[str, Any]]] = {
            "list": [
                {
                    "amount": 42434.4234,
                    "category": "expense",
                    "date": "2024-05-01",
                    "description": "That description doesn't make sense."
                },
                {
                    "amount": 123.31,
                    "category": "expense",
                    "date": "2024-01-12",
                    "description": ""
                },
                {
                    "amount": 8234.424,
                    "category": "income",
                    "date": "2024-04-10",
                    "description": "Bonus payment for project completion."
                },
                {
                    "amount": 5234.31,
                    "category": "expense",
                    "date": "2024-01-04",
                    "description": "Продукты"
                },
                {
                    "amount": 844.2343,
                    "category": "expense",
                    "date": "2021-04-07",
                    "description": "Empty"
                },
            ]
        }
        
        # Update records with the new values
        for i, val in enumerate(expected_test_data["list"]):
            record.update(i, val["amount"], val["category"], val["date"], val["description"])

        fs = File()
        data_from_file: dict[str, list[dict[str, Any]]] = fs.read_json()
        
        # Check if the updates are correctly reflected in the stored data
        self.assertDictEqual(data_from_file, expected_test_data)

        self.delete_file()

    def test_get(self):
        """Test the 'get' method to ensure it retrieves all stored records.

        Verifies that:
        - All records are retrieved.
        - The count of retrieved records matches the expected count.
        """
        test_data: list[list[Any]] = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
            [84324.234, "expense", "2021-4-1", "Empty"],
        ]  # amount, category, date, description
        record = Record()

        for item in test_data:
            record.add(amount=item[0], category=item[1], date=item[2], description=item[3])
        
        self.assertEqual(len(record.get()), len(test_data))

        self.delete_file()

    def test_get_by_key(self):
        """Test the 'get_by_key' method to retrieve records by a specified key and value.

        Verifies that:
        - Records can be retrieved based on specific key-value pairs.
        - Invalid keys return an error message (as a string).
        """
        test_data: list[list[Any]] = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
            [84324.234, "expense", "2021-4-1", "Empty"],
        ]  # amount, category, date, description
        record = Record()

        for item in test_data:
            record.add(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Test retrieving records by key and value
        self.assertEqual(len(record.get_by_key("amount", 134.4234)), 1)
        self.assertEqual(type(record.get_by_key("amount", 134.4234)), list)
        self.assertEqual(len(record.get_by_key("category", "expense")), 3)
        self.assertEqual(type(record.get_by_key("category", "expense")), list)
        self.assertEqual(len(record.get_by_key("date", "2024-1-6")), 1)
        self.assertEqual(type(record.get_by_key("date", "2024-1-6")), list)

        # Test invalid keys
        self.assertEqual(type(record.get_by_key("", "")), str)
        self.assertEqual(type(record.get_by_key("None", "123")), str)
        self.assertEqual(type(record.get_by_key("None", 123.0)), str)

        self.delete_file()