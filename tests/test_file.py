import os
from typing import Any
import unittest
from fs import File

class TestFile(unittest.TestCase):
    def file_exists(self, filename: str) -> bool:
        """Check if a file exists.

        Args:
            filename (str): The name of the file to check.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(filename)

    def delete_file(self, filename: str) -> bool:
        """Delete a file.

        Args:
            filename (str): The name of the file to delete.

        Returns:
            bool: True if the file was successfully deleted, False otherwise.
        """
        if os.path.isfile(filename):
            os.remove(filename)
            return True
        return False

    def test_read_json(self):
        """Test the functionality of reading a JSON file."""
        self.__fs = File()
        # Ensure the file is not empty after reading
        self.assertNotEqual(len(self.__fs.read_json()), 0)
        self.assertEqual(self.file_exists(self.__fs.FILENAME), True)
        # Delete the file and check if the deletion was successful
        self.assertEqual(self.delete_file(self.__fs.FILENAME), True)

    def test_write_json(self):
        """Test the functionality of writing data to a JSON file."""
        self.__fs = File()
        data: dict[str, list[dict[str, Any]]] = {
            "list": [
                {
                    "array1": "value1"
                },
                {
                    "array2": "value2"
                }
            ]
        }
        
        self.__fs.write_json(data)
        # Read the data back from the file and check if it matches the original
        data_from_file: dict[str, list[dict[str, Any]]] = self.__fs.read_json()
        self.assertEqual(data, data_from_file, f"The data from the file does not match the original data. Expected: {data}. Found: {data_from_file}")
        # Delete the file and check if the deletion was successful
        self.assertEqual(self.delete_file(self.__fs.FILENAME), True)
