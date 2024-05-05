import datetime
import re
from entities.record_attributes import EntityRecordAttributes

class ValidatorRecord:
    def __init__(self) -> None:
        self.__record_attributes = EntityRecordAttributes()

    def is_date(self, value: str) -> None:
        pattern = r'^\d{4}-\d{1,2}-\d{1,2}$'

        if not re.match(pattern, value):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD or YYYY-M-D.")

        try:
            year, month, day = map(int, value.split('-'))
            datetime.datetime(year, month, day)
        except ValueError:
            raise ValueError("Invalid date: unable to create a valid datetime object.")


    def is_category(self, value: str) -> None:
        if value not in self.__record_attributes.categories:
            raise ValueError(f"Category '{value}' was not found. Available categories: {self.__record_attributes.categories}.")