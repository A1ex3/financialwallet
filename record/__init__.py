from typing import Any, Optional
from entities.containers.linked_list import LinkedListRecord
from entities.record_attributes import EntityRecordAttributes
from fs import File

class Record:
    """
    Class to manage financial records, allowing for addition, update, and retrieval of record data.
    """

    def __init__(self) -> None:
        self.__fs = File()

    def add(
        self,
        amount: float,
        category: str,
        date: str,
        description: str
    ) -> str:
        """
        Adds a new financial record with the specified details.

        Args:
            amount (float): The monetary amount of the record.
            category (str): The category of the record (e.g., income or expense).
            date (str): The date of the record.
            description (str): A description or note for the record.

        Returns:
            str: A success message if the record was added, or an error message if an exception occurred.
        """
        try:
            current_data: dict[str, list[dict[str, Any]]] = self.__fs.read_json()

            if current_data is None or "list" not in current_data:
                current_data = {"list": []}

            linked_list = LinkedListRecord()
            linked_list.insert_first(amount, category, date, description)
            
            current = linked_list.get()

            while current is not None:
                current_data["list"].append(current.value.to_json())
                current = current.next

            self.__fs.write_json(current_data)

            return "The record was successfully added."
        except ValueError as e:
            return str(e)

    def update(
        self,
        index: int,
        new_amount: Optional[float] = None,
        new_category: Optional[str] = None,
        new_date: Optional[str] = None,
        new_description: Optional[str] = None
    ) -> str:
        """
        Updates an existing record at the specified index with new details.

        Args:
            index (int): The index of the record to update.
            new_amount (Optional[float]): The new amount, if updating.
            new_category (Optional[str]): The new category, if updating.
            new_date (Optional[str]): The new date, if updating.
            new_description (Optional[str]): The new description, if updating.

        Returns:
            str: A success message if the record was updated, or an error message if an exception occurred.
        """
        try:
            current_data: dict[str, list[dict[str, Any]]] = self.__fs.read_json()

            if current_data is None or len(current_data["list"]) == 0:
                return "No records found."

            if index < 0 or index >= len(current_data["list"]):
                return "Invalid index."

            linked_list = LinkedListRecord()

            for i in current_data["list"]:
                linked_list.insert_last(i["amount"], i["category"], i["date"], i["description"])

            if linked_list.update_by_index(index, new_amount, new_category, new_date, new_description):
                current_data["list"].clear()

                current = linked_list.get()

                while current is not None:
                    current_data["list"].append(current.value.to_json())
                    current = current.next

                self.__fs.write_json(current_data)

                return "The record was successfully updated."
            else:
                return "Failed to update the record."
        except ValueError as e:
            return str(e)

    def get_balance(self) -> list[str]:
        """
        Calculates the total balance, income, and expense from the current records.

        Returns:
            list[str]: A list containing the balance, income, and expense in string format.
        """
        balance: str = "Balance: "
        income: str = "Income: "
        expense: str = "Expense: "
        result: list[str] = []

        current_data: dict[str, list[dict[str, Any]]] = self.__fs.read_json()
        
        if len(current_data["list"]) == 0:
            balance += "0"
            income += "0"
            expense += "0"
        else:
            record_attributes = EntityRecordAttributes()

            balance_: float = 0.0
            income_: float = 0.0
            expense_: float = 0.0
            for i in current_data["list"]:
                if i["category"] == record_attributes.categories[0]:  # income
                    balance_ += i["amount"]
                    income_ += i["amount"]
                elif i["category"] == record_attributes.categories[1]:  # expense
                    balance_ -= i["amount"]
                    expense_ += i["amount"]
            
            balance += str(round(balance_, 2))
            income += str(round(income_, 2))
            expense += str(round(expense_, 2))
            
        result.append(balance)
        result.append(income)
        result.append(expense)
        return result

    def get(self) -> list[str]:
        """
        Retrieves all records and formats them into a list of strings for easy display.

        Returns:
            list[str]: A list containing the string representation of all records.
        """
        result: list[str] = []

        current_data: dict[str, list[dict[str, Any]]] = self.__fs.read_json()
        
        if len(current_data["list"]) == 0:
            return []
        else:
            for idx, val in enumerate(current_data["list"]):
                result.append(f"[{idx}]\nAmount: {round(val['amount'], 2)}.\nCategory: {val['category']}.\nDate: {val['date']}.\nDescription: {val['description']}.")

        return result

    def get_by_key(self, by: str, value: float | str) -> list[str] | str:
        """
        Retrieves records based on a specified key and value.

        Args:
            by (str): The key by which to search ('amount', 'category', 'date').
            value (float | str): The value to search for.

        Returns:
            list[str] | str: A list of records matching the search criteria, or a message if the key is invalid.
        """
        result: list[str] = []

        current_data: dict[str, list[dict[str, Any]]] = self.__fs.read_json()
        
        if len(current_data["list"]) == 0:
            return "No records found."
        else:
            try:
                linked_list = LinkedListRecord()

                for i in current_data["list"]:
                    linked_list.insert_last(i["amount"], i["category"], i["date"], i["description"])
                
                if by == "amount" and isinstance(value, float):
                    for idx, val in linked_list.get_by_amount(value).items():
                        result.append(f"[{idx}]\nAmount: {round(val.amount, 2)}.\nCategory: {val.category}.\nDate: {val.date}.\nDescription: {val.description}.")
                elif by == "category" and isinstance(value, str):
                    for idx, val in linked_list.get_by_category(value).items():
                        result.append(f"[{idx}]\nAmount: {round(val.amount, 2)}.\nCategory: {val.category}.\nDate: {val.date}.\nDescription: {val.description}.")
                elif by == "date" and isinstance(value, str):
                    for idx, val in linked_list.get_by_date(value).items():
                        result.append(f"[{idx}]\nAmount: {round(val.amount, 2)}.\nCategory: {val.category}.\nDate: {val.date}.\nDescription: {val.description}.")
                else:
                    return f"The '{by}' key cannot be searched, the available search keys are 'amount', 'category', 'date'."
            except ValueError as e:
                return str(e)
        
        return result
