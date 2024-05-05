from typing import Any, Optional, Callable, Type

class EntityTypeInteger:
    def __init__(
        self,
        validate_function: Optional[Callable[[int], None]] = None,
        min_val: Optional[int] = None,
        max_val: Optional[int] = None
    ):
        """
        Args:
            validate_function (Optional[Callable[[int], None]]): A custom validation function that is called to validate the integer value. It takes an integer and raises an exception if validation fails.
            min_val (Optional[int]): The minimum allowable value for the integer. If None, there is no minimum constraint.
            max_val (Optional[int]): The maximum allowable value for the integer. If None, there is no maximum constraint.
        """

        self.__value: Optional[int] = None
        self.__min: Optional[int] = min_val
        self.__max: Optional[int] = max_val
        self.__validate_function: Optional[Callable[[int], None]] = validate_function

    def _is_valid(self, value: int) -> bool:
        if not isinstance(value, int):
            raise TypeError(f"Value must be an integer, got {type(value)}.")

        if self.__min is not None and value < self.__min:
            raise ValueError(f"Value {value} is less than the minimum {self.__min}.")
        
        if self.__max is not None and value > self.__max:
            raise ValueError(f"Value {value} is greater than the maximum {self.__max}.")

        if self.__validate_function is not None:
            self.__validate_function(value)

        return True

    @property
    def value(self) -> int:
        if self.__value is None:
            raise AttributeError("Value is not initialized.")
        return self.__value

    @value.setter
    def value(self, new_value: int) -> None:
        if self._is_valid(new_value):
            self.__value = new_value

class EntityTypeFloat:
    def __init__(
        self,
        validate_function: Optional[Callable[[float], None]] = None,
        min_val: Optional[float] = None,
        max_val: Optional[float] = None
    ):
        """
        Args:
            validate_function (Optional[Callable[[float], None]]): A custom validation function that takes a float and raises an exception if validation fails.
            min_val (Optional[float]): The minimum allowable value for the float. If None, there is no minimum constraint.
            max_val (Optional[float]): The maximum allowable value for the float. If None, there is no maximum constraint.
        """

        self.__value: Optional[float] = None
        self.__min: Optional[float] = min_val
        self.__max: Optional[float] = max_val
        self.__validate_function: Optional[Callable[[float], None]] = validate_function

    def _is_valid(self, value: float) -> bool:
        if not isinstance(value, float):
            raise TypeError(f"Value must be a float, got {type(value)}.")

        if self.__min is not None and value < self.__min:
            raise ValueError(f"Value {value} is less than the minimum {self.__min}.")
        
        if self.__max is not None and value > self.__max:
            raise ValueError(f"Value {value} is greater than the maximum {self.__max}.")

        if self.__validate_function is not None:
            self.__validate_function(value)

        return True

    @property
    def value(self) -> float:
        if self.__value is None:
            raise AttributeError("Value is not initialized.")
        return self.__value

    @value.setter
    def value(self, new_value: float) -> None:
        if self._is_valid(new_value):
            self.__value = new_value

class EntityTypeString:
    def __init__(
        self,
        validate_function: Optional[Callable[[str], None]] = None,
        allowed_values: Optional[list[str]] = None,
        pattern: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None
    ):
        """
        Initializes the EntityTypeString with optional validation, allowed values, pattern, and length constraints.

        Args:
            validate_function (Optional[Callable[[str], None]]): A custom validation function that takes a string and raises an exception if validation fails.
            allowed_values (Optional[List[str]]): A list of allowed string values. If None,  any value is allowed.
            pattern (Optional[str]): A regex pattern that the string must match. If None, no pattern constraint is enforced.
            min_length (Optional[int]): The minimum length for the string. If None, there is no minimum length constraint.
            max_length (Optional[int]): The maximum length for the string. If None, there is no maximum length constraint.
        """

        self.__value: Optional[str] = None
        self.__allowed_values: Optional[list[str]] = allowed_values
        self.__pattern: Optional[str] = pattern
        self.__min_length: Optional[int] = min_length
        self.__max_length: Optional[int] = max_length
        self.__validate_function: Optional[Callable[[str], None]] = validate_function

    def _is_valid(self, value: str) -> bool:
        if not isinstance(value, str):
            raise TypeError(f"Value must be a string, got {type(value)}.")

        if self.__min_length is not None:
            if self.__min_length < 0:
                raise AttributeError(f"The minimum length cannot be less than 0, the current value is {self.__min_length}")
            elif len(value) < self.__min_length:
                raise ValueError(f"Length of the value ({len(value)}) is shorter than the minimum length ({self.__min_length}).")

        if self.__max_length is not None:
            if self.__max_length < 0:
                raise AttributeError(f"The maximum length cannot be less than 0, the current value is {self.__max_length}")
            elif len(value) > self.__max_length:
                raise ValueError(f"Length of the value ({len(value)}) exceeds the maximum length ({self.__max_length}).")


        if self.__allowed_values is not None and value not in self.__allowed_values:
            raise ValueError(f"Value '{value}' is not in the allowed values.")

        if self.__pattern is not None:
            import re
            if not re.match(self.__pattern, value):
                raise ValueError(f"Value '{value}' does not match the pattern.")

        if self.__validate_function is not None:
            self.__validate_function(value)

        return True

    @property
    def value(self) -> str:
        if self.__value is None:
            raise AttributeError("Value is not initialized.")
        return self.__value

    @value.setter
    def value(self, new_value: str) -> None:
        if self._is_valid(new_value):
            self.__value = new_value

class EntityTypeList:
    def __init__(
        self,
        validate_function: Optional[Callable[[list[Any]], None]] = None,
        allowed_type: Optional[Type] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None
    ):
        """
        Args:
            validate_function (Optional[Callable[[list[Any]], None]]): A custom validation function that takes a list and raises an exception if validation fails.
            allowed_type (Optional[Type]): The expected type of elements in the list. If None, any type is allowed.
            min_length (Optional[int]): The minimum number of elements in the list. If None, there is no minimum length constraint.
            max_length (Optional[int]): The maximum number of elements in the list. If None, there is no maximum length constraint.
        """

        self.__value: Optional[list[Any]] = None
        self.__allowed_type: Optional[Type] = allowed_type
        self.__min_length: Optional[int] = min_length
        self.__max_length: Optional[int] = max_length
        self.__validate_function: Optional[Callable[[list[Any]], None]] = validate_function

    def _is_valid(self, value: list[Any]) -> bool:
        if not isinstance(value, list):
            raise TypeError(f"Value must be a list, got {type(value)}.")

        if self.__min_length is not None:
            if self.__min_length < 0:
                raise AttributeError(f"The minimum length cannot be less than 0, the current value is {self.__min_length}")
            else:
                if len(value) < self.__min_length:
                    raise ValueError(f"Length of the list is less than the minimum {self.__min_length}.")

        if self.__max_length is not None:
            if self.__max_length < 0:
                raise AttributeError(f"The maximum length cannot be less than 0, the current value is {self.__max_length}")
            else:
                if len(value) > self.__max_length:
                    raise ValueError(f"Length of the list exceeds the maximum {self.__max_length}.")

        if self.__allowed_type is not None:
            for item in value:
                if not isinstance(item, self.__allowed_type):
                    raise TypeError(f"Item {item} in list is not of the allowed type {self.__allowed_type}.")

        if self.__validate_function is not None:
            self.__validate_function(value)

        return True

    @property
    def value(self) -> list[Any]:
        if self.__value is None:
            raise AttributeError("Value is not initialized.")
        return self.__value

    @value.setter
    def value(self, new_value: list[Any]) -> None:
        if self._is_valid(new_value):
            self.__value = new_value

class EntityTypeDict:
    def __init__(
        self,
        validate_function: Optional[Callable[[dict], None]] = None,
        allowed_key_type: Optional[Type] = None,
        allowed_value_type: Optional[Type] = None,
        min_keys: Optional[int] = None,
        max_keys: Optional[int] = None,
        required_keys: Optional[list[Any]] = None,
    ):
        """
        Args:
            validate_function (Optional[Callable[[dict], None]]): A custom validation function that takes a dictionary and raises an exception if validation fails.
            allowed_key_type (Optional[Type]): The expected type for dictionary keys. If None, any type is allowed.
            allowed_value_type (Optional[Type]): The expected type for dictionary values. If None, any type is allowed.
            min_keys (Optional[int]): The minimum number of keys required in the dictionary. If None, no minimum constraint.
            max_keys (Optional[int]): The maximum number of keys allowed in the dictionary. If None, no maximum constraint.
            required_keys (Optional[List[Any]]): A list of required key names. If None, no specific keys are required.
        """

        self.__value: Optional[dict[Any, Any]] = None
        self.__allowed_key_type: Optional[Type] = allowed_key_type
        self.__allowed_value_type: Optional[Type] = allowed_value_type
        self.__min_keys: Optional[int] = min_keys
        self.__max_keys: Optional[int] = max_keys
        self.__required_keys: Optional[list[Any]] = required_keys
        self.__validate_function: Optional[Callable[[dict], None]] = validate_function

    def _is_valid(self, value: dict[Any, Any]) -> bool:
        if not isinstance(value, dict):
            raise TypeError(f"Value must be a dictionary, got {type(value)}.")

        if self.__min_keys is not None:
            if self.__min_keys < 0:
                raise AttributeError(f"The minimum number of keys cannot be less than 0, the current value is {self.__min_keys}")
            else:
                if len(value) < self.__min_keys:
                    raise ValueError(f"Dictionary has fewer keys than the minimum {self.__min_keys}.")

        if self.__max_keys is not None:
            if self.__max_keys < 0:
                raise AttributeError(f"The maximum number of keys cannot be less than 0, the current value is {self.__max_keys}")
            else:
                if len(value) > self.__max_keys:
                    raise ValueError(f"Dictionary has more keys than the maximum {self.__max_keys}.")

        if self.__allowed_key_type is not None:
            for key in value.keys():
                if not isinstance(key, self.__allowed_key_type):
                    raise TypeError(f"Key '{key}' is not of the allowed type {self.__allowed_key_type}. Current type {type(key)}.")

        if self.__allowed_value_type is not None:
            for key, val in value.items():
                if not isinstance(val, self.__allowed_value_type):
                    raise TypeError(f"Value for key '{key}' is not of the allowed type {self.__allowed_value_type}. Current type {type(val)}.")

        if self.__required_keys is not None:
            for required_key in self.__required_keys:
                if required_key not in value:
                    raise KeyError(f"Missing required key '{required_key}'.")

        if self.__validate_function is not None:
            self.__validate_function(value)

        return True

    @property
    def value(self) -> dict[Any, Any]:
        if self.__value is None:
            raise AttributeError("Value is not initialized.")
        return self.__value

    @value.setter
    def value(self, new_value: dict[Any, Any]) -> None:
        if self._is_valid(new_value):
            self.__value = new_value

class EntityTypeBool:
    def __init__(
        self,
        validate_function: Optional[Callable[[bool], None]] = None,
    ):
        """
        Args:
            validate_function (Optional[Callable[[bool], None]]): A custom validation function that takes a boolean and raises an exception if validation fails.
        """

        self.__value: Optional[bool] = None
        self.__validate_function: Optional[Callable[[bool], None]] = validate_function

    def _is_valid(self, value: bool) -> bool:
        if not isinstance(value, bool):
            raise TypeError(f"Value must be a boolean, got {type(value)}.")

        if self.__validate_function is not None:
            self.__validate_function(value)

        return True

    @property
    def value(self) -> bool:
        if self.__value is None:
            raise AttributeError("Value is not initialized.")
        return self.__value

    @value.setter
    def value(self, new_value: bool) -> None:
        if self._is_valid(new_value):
            self.__value = new_value