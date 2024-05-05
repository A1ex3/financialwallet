from abc import ABC, abstractmethod
from typing import Any
from validator.record import ValidatorRecord

class BaseEntity(ABC):
    def __init__(self) -> None:
        self._validator_record = ValidatorRecord()

    @abstractmethod
    def to_json(self) -> dict[str, Any]:...