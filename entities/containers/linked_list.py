from typing import Optional
from unicodedata import category
from entities.record import EntityRecord

class NodeRecord:
    def __init__(self, value: EntityRecord, next = None) -> None:
        self.value = value
        self.next: NodeRecord = next # type: ignore

class LinkedListRecord:
    def __init__(self) -> None:
        self.__length: int = 0
        self.__head = None
        self.__tail = None

    def insert_first(
        self,
        amount: float,
        category: str,
        date: str,
        description: str,
    ) -> None:
        record = EntityRecord(amount, category, date, description)

        node = NodeRecord(record)
        
        node.next = self.__head # type: ignore
        self.__head = node

        if self.__tail is None:
            self.__tail = node

        self.__length += 1

    def insert_last(
        self,
        amount: float,
        category: str,
        date: str,
        description: str,
    ) -> None:
        record = EntityRecord(amount, category, date, description)

        node = NodeRecord(record)

        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node # type: ignore
            self.__tail = node
        
        self.__length += 1

    @property
    def length(self) -> int:
        return self.__length

    def get(self) -> NodeRecord:
        return self.__head # type: ignore

    def get_by_amount(self, value: float) -> dict[int, EntityRecord]:
        """
        Retrieve all records from the linked list that match the given amount.

        Args:
            value (float): The amount to search for in the linked list.

        Returns:
            dict[int, EntityRecord]: A dictionary where the keys are the index positions of the matching records and the values are the matching `EntityRecord` instances.
        """
        record = EntityRecord(amount=value)

        index: int = 0
        result: dict[int, EntityRecord] = {}
        current = self.__head
        
        while current is not None:
            if current.value.amount == record.amount:
                result[index] = current.value
            
            index += 1
            current = current.next
        
        return result
    
    def get_by_category(self, value: str) -> dict[int, EntityRecord]:
        """
        Retrieve all records from the linked list that match the given category.

        Args:
            value (str): The category to search for in the linked list.

        Returns:
            dict[int, EntityRecord]: A dictionary where the keys are the index positions of the matching records and the values are the matching `EntityRecord` instances.
        """
        record = EntityRecord(category=value)

        index: int = 0
        result: dict[int, EntityRecord] = {}
        current = self.__head
        
        while current is not None:
            if current.value.category == record.category:
                result[index] = current.value
            
            index += 1
            current = current.next
        
        return result
    
    def get_by_date(self, value: str) -> dict[int, EntityRecord]:
        """
        Retrieve all records from the linked list that match the given date.

        Args:
            value (str): The date to search for in the linked list.

        Returns:
            dict[int, EntityRecord]: A dictionary where the keys are the index positions of the matching records and the values are the matching `EntityRecord` instances.
        """
        record = EntityRecord(date=value)

        index: int = 0
        result: dict[int, EntityRecord] = {}
        current = self.__head
        
        while current is not None:
            if current.value.date == record.date:
                result[index] = current.value
            
            index += 1
            current = current.next
        
        return result

    def remove_by_index(self, index: int) -> bool:
        if index < 0:
            return False

        if self.__head is None:
            return False

        if index == 0:
            self.__head = self.__head.next
            if self.__head is None:
                self.__tail = None
            self.__length -= 1
            return True

        current = self.__head
        prev = None
        count = 0

        while current is not None and count < index:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return False

        prev.next = current.next # type: ignore

        if prev.next is None: # type: ignore
            self.__tail = prev

        self.__length -= 1
        return True
    
    def update_by_index(
        self,
        index: int,
        new_amount: Optional[float] = None,
        new_category: Optional[str] = None,
        new_date: Optional[str] = None,
        new_description: Optional[str] = None
    ) -> bool:
        if index < 0:
            return False

        current = self.__head
        count = 0

        while current is not None and count < index:
            current = current.next
            count += 1

        if current is None:
            return False

        if new_amount:
            current.value.amount = new_amount
        if new_category:
            current.value.category = new_category
        if new_date:
            current.value.date = new_date
        if new_description:
            current.value.description = new_description

        return True