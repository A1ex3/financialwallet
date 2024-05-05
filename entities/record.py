from typing import Any, Optional
from entities.base import BaseEntity
from entities.types import EntityTypeFloat, EntityTypeString

class EntityRecord(BaseEntity):
    def __init__(
        self,
        amount: Optional[float] = None,
        category: Optional[str] = None,
        date: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.__amount = EntityTypeFloat(min_val=0.0)
        self.__date = EntityTypeString(validate_function=self._validator_record.is_date) 
        self.__category = EntityTypeString(validate_function=self._validator_record.is_category)
        self.__description = EntityTypeString(min_length=0, max_length=500)

        if amount is not None:
            self.__amount.value = amount
        if category is not None:
            self.__category.value = category
        if date is not None:
            self.__date.value = date
        if description is not None:
            self.__description.value = description

    @property
    def amount(self) -> float:
        return self.__amount.value
    
    @amount.setter
    def amount(self, value: float) -> None:
        self.__amount.value = value

    @property
    def date(self) -> str:
        return self.__date.value
    
    @date.setter
    def date(self, value: str) -> None:
        self.__date.value = value

    @property
    def category(self) -> str:
        return self.__category.value
    
    @category.setter
    def category(self, value: str) -> None:
        self.__category.value = value

    @property
    def description(self) -> str:
        return self.__description.value
    
    @description.setter
    def description(self, value: str) -> None:
        self.__description.value = value

    def to_json(self) -> dict[str, Any]:
        """
        Example:
            {
                "amount": 150.75,
                "date": "2024-05-03",
                "category": "expense",
                "description": "Office supplies"
            }
        """
        return {
            "amount": self.__amount.value,
            "date": self.__date.value,
            "category": self.__category.value,
            "description": self.__description.value
        }