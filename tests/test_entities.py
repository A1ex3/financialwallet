import random
import string
import unittest
from entities.record import EntityRecord

class TestEntityRecord(unittest.TestCase):
    """Unit tests for the EntityRecord class to ensure proper functionality and validation."""

    def test_amount(self):
        """Test that the 'amount' attribute is set correctly and raises errors for invalid values.

        Verifies that:
        - A valid amount is properly set.
        - TypeError is raised for non-float values.
        - ValueError is raised for negative values.
        """
        record = EntityRecord(amount=123.456)
        self.assertEqual(record.amount, 123.456)

        with self.assertRaises(TypeError):
            EntityRecord(amount=123)

        with self.assertRaises(ValueError):
            EntityRecord(amount=-12.0)

    def test_category(self):
        """Test the 'category' attribute for correct setting and validation.

        Verifies that:
        - A valid category is properly set ("income" or "expense").
        - ValueError is raised for invalid categories.
        """
        record = EntityRecord(category="income")
        self.assertEqual(record.category, "income")

        record = EntityRecord(category="expense")
        self.assertEqual(record.category, "expense")

        with self.assertRaises(ValueError):
            EntityRecord(category="none")

    def test_date(self):
        """Test the 'date' attribute for correct setting and validation.

        Verifies that:
        - Valid dates are properly set.
        - ValueError is raised for invalid date formats.
        """
        record = EntityRecord(date="2024-12-01")
        self.assertEqual(record.date, "2024-12-01")

        record = EntityRecord(date="2024-2-1")
        self.assertEqual(record.date, "2024-2-1")

        with self.assertRaises(ValueError):
            EntityRecord(date="24-2-1")
        
        with self.assertRaises(ValueError):
            EntityRecord(date="2/11/2024")

    def test_description(self):
        """Test the 'description' attribute for correct setting and validation.

        Verifies that:
        - Descriptions with valid lengths are accepted.
        - An empty description is allowed.
        - ValueError is raised for descriptions longer than 500 characters.
        """
        record = EntityRecord(description="That description doesn't make sense.")
        self.assertEqual(record.description, "That description doesn't make sense.")

        EntityRecord(description="")

        def generate_string(length):
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        with self.assertRaises(ValueError):
            EntityRecord(description=generate_string(501))