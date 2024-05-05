from typing import Any
import unittest
from entities.containers.linked_list import LinkedListRecord


class TestLinkedListRecord(unittest.TestCase):
    """Unit tests for the LinkedListRecord class to verify linked list operations."""

    def test_length(self):
        """Test the length property of the linked list.

        Verifies that:
        - Inserting elements into the linked list increases its length.
        - Removing elements decreases its length.
        - Attempting to remove an element from an empty list does not change its length.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.6785, "income", "2024-5-5", "That description doesn't make sense."],
            [31.0, "expense", "2024-1-6", ""],
            [210.75, "income", "2024-4-10", "Bonus payment for project completion."],
            [50.25, "expense", "2024-2-20", "Groceries and other household items."],
            [85.0, "expense", "2024-3-15", "Dinner with friends at a restaurant."],
            [500.0, "income", "2024-4-1", "Tax refund received."],
            [75.5, "expense", "2024-3-22", "Car fuel."],
            [300.0, "income", "2024-1-15", "Freelance gig payment."],
            [120.0, "expense", "2024-3-10", "Utility bills."],
            [250.0, "expense", "2024-5-3", "Car maintenance and repairs."],
            [400.0, "income", "2024-5-5", "Monthly salary."],
            [1042.52, "income", "2021-3-1", "Продукты"],
        ]  # amount, category, date, description

        
        for item in test_data:
            linked_list.insert_first(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that the length matches the number of elements inserted
        self.assertEqual(len(test_data), linked_list.length)

        # Remove the first three elements and check the new length
        ELEMENTS = 3
        for _ in range(ELEMENTS):
            linked_list.remove_by_index(0)

        self.assertEqual(linked_list.length, len(test_data) - ELEMENTS)

        # Check removal from an empty list
        linked_list = LinkedListRecord()
        self.assertEqual(linked_list.remove_by_index(0), False)  # Expect False for empty list
        self.assertEqual(linked_list.length, 0)

    def test_insert_first(self):
        """Test the insert_first method to ensure elements are inserted at the beginning of the linked list.

        Checks that:
        - New elements are inserted at the beginning of the list.
        - The order of elements is reversed when inserted at the beginning.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.6785, "income", "2024-5-5", "That description doesn't make sense."],
            [31.0, "expense", "2024-1-6", ""],
            [210.75, "income", "2024-4-10", "Bonus payment for project completion."],
            [50.25, "expense", "2024-2-20", "Groceries and other household items."],
            [85.0, "expense", "2024-3-15", "Dinner with friends at a restaurant."],
            [500.0, "income", "2024-4-1", "Tax refund received."],
            [75.5, "expense", "2024-3-22", "Car fuel."],
            [300.0, "income", "2024-1-15", "Freelance gig payment."],
            [120.0, "expense", "2024-3-10", "Utility bills."],
            [250.0, "expense", "2024-5-3", "Car maintenance and repairs."],
            [400.0, "income", "2024-5-5", "Monthly salary."],
            [1042.52, "income", "2021-3-1", "Продукты"],
        ]  # amount, category, date, description

        # Insert elements at the beginning of the linked list
        for item in test_data:
            linked_list.insert_first(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that elements are inserted in reverse order
        current = linked_list.get()
        for i, val in enumerate(reversed(test_data)):
            self.assertEqual(val[0], current.value.amount, f"The values at index {len(test_data) - 1 - i} do not match.")
            current = current.next

    def test_insert_last(self):
        """Test the insert_last method to ensure elements are inserted at the end of the linked list.

        Checks that:
        - New elements are inserted at the end of the list.
        - The order of elements remains unchanged when inserted at the end.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.6785, "income", "2024-5-5", "That description doesn't make sense."],
            [31.0, "expense", "2024-1-6", ""],
            [210.75, "income", "2024-4-10", "Bonus payment for project completion."],
            [50.25, "expense", "2024-2-20", "Groceries and other household items."],
            [85.0, "expense", "2024-3-15", "Dinner with friends at a restaurant."],
            [500.0, "income", "2024-4-1", "Tax refund received."],
            [75.5, "expense", "2024-3-22", "Car fuel."],
            [300.0, "income", "2024-1-15", "Freelance gig payment."],
            [120.0, "expense", "2024-3-10", "Utility bills."],
            [250.0, "expense", "2024-5-3", "Car maintenance and repairs."],
            [400.0, "income", "2024-5-5", "Monthly salary."],
            [1042.52, "income", "2021-3-1", "Продукты"],
        ]  # amount, category, date, description

        for item in test_data:
            linked_list.insert_last(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that elements are inserted in the same order as in test_data
        current = linked_list.get()
        for i, val in enumerate(test_data):
            self.assertEqual(val[0], current.value.amount, f"The values at index {i} do not match.")
            current = current.next

    def test_get(self):
        """Test the get method to ensure it retrieves the first node in the linked list.

        Checks that:
        - If the list is empty, it returns None.
        - If the list contains elements, it retrieves the first node.
        """
        linked_list = LinkedListRecord()
        self.assertEqual(linked_list.get(), None)  # Expect None for empty list
        linked_list.insert_first(123.0, "income", "2024-12-1", "")
        self.assertNotEqual(linked_list.get(), None)  # Expect a node if there's an element in the list

    def test_get_by_amount(self):
        """Test the get_by_amount method to find all nodes with a specified amount.

        Checks that:
        - It retrieves a list of nodes with the specified amount.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-6", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
        ]  # amount, category, date, description

        
        for item in test_data:
            linked_list.insert_last(amount=item[0], category=item[1], date=item[2], description=item[3])
        
        # Check that each specified amount retrieves the correct node
        for item in test_data:
            current = linked_list.get_by_amount(item[0])
            self.assertEqual(len(current), 1)

    def test_get_by_category(self):
        """Test the get_by_category method to find all nodes with a specified category.

        Checks that:
        - It retrieves a list of nodes with the specified category.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-6", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
        ]  # amount, category, date, description

        for item in test_data:
            linked_list.insert_last(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that each specified category retrieves the correct nodes
        for item in test_data:
            current = linked_list.get_by_category(item[1])
            self.assertEqual(len(current), 2)

    def test_get_by_date(self):
        """Test the get_by_date method to find all nodes with a specified date.

        Checks that:
        - It retrieves a list of nodes with the specified date.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
        ]  # amount, category, date, description

        for item in test_data:
            linked_list.insert_last(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that each specified date retrieves the correct node
        for item in test_data:
            current = linked_list.get_by_date(item[2])
            self.assertEqual(len(current), 1)

    def test_remove_by_index(self):
        """Test the remove_by_index method to ensure it removes a node at a specified index.

        Checks that:
        - Removing a node at a valid index works as expected.
        - Removing a node at an invalid index returns False.
        """
        linked_list = LinkedListRecord()
        test_data = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
        ]  # amount, category, date, description

        
        for item in test_data:
            linked_list.insert_last(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that removing an invalid index returns False
        self.assertEqual(linked_list.remove_by_index(10), False)

        # Check that removing the first node works and reduces the length
        self.assertEqual(linked_list.remove_by_index(0), True)
        self.assertEqual(linked_list.length, len(test_data) - 1)

        # Test removal from an empty list
        linked_list = LinkedListRecord()
        self.assertEqual(linked_list.remove_by_index(0), False)

    def test_update_by_index(self):
        """Test the update_by_index method to ensure nodes can be updated by their index.

        Checks that:
        - Nodes are updated correctly with new values.
        - Attempting to update a non-existent index returns False.
        """
        linked_list = LinkedListRecord()
        self.assertEqual(linked_list.update_by_index(0, 0.0, "", "", ""), False)  # Should return False for empty list

        test_data = [
            [134.4234, "income", "2024-5-5", "That description doesn't make sense."],
            [123.31, "expense", "2024-1-1", ""],
            [4234.424, "income", "2024-4-10", "Bonus payment for project completion."],
            [54234.31, "expense", "2024-1-6", "Продукты"],
            [84324.234, "expense", "2021-4-1", "Empty"],
        ]  # amount, category, date, description

        
        for item in test_data:
            linked_list.insert_last(amount=item[0], category=item[1], date=item[2], description=item[3])

        # Check that nodes can be updated with new values
        self.assertEqual(linked_list.update_by_index(0, new_amount=123.456, new_category="income", new_date="2021-4-4", new_description=""), True)
        self.assertEqual(linked_list.update_by_index(1, new_amount=535.535), True)
        self.assertEqual(linked_list.update_by_index(2, new_category="expense"), True)
        self.assertEqual(linked_list.update_by_index(3, new_date="2011-2-2"), True)
        self.assertEqual(linked_list.update_by_index(4, new_description="Not Empty"), True)