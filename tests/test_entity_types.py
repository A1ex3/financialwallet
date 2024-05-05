import unittest
from entities.types import EntityTypeBool, EntityTypeDict, EntityTypeFloat, EntityTypeInteger, EntityTypeList, EntityTypeString

class TestEntityTypes(unittest.TestCase):
    """
    Unit tests for various entity types to ensure that
    they behave according to expected specifications.
    """
    def test_type_integer(self):
        """
        Tests the behavior of the `EntityTypeInteger` class.
        
        Verifies:
            - Type enforcement.
            - Boundary conditions.
            - Custom validation functions for integer values.
        """
        type_integer = EntityTypeInteger()

        with self.assertRaises(TypeError):
            type_integer.value = 1.0

        type_integer.value = -54
        self.assertEqual(type_integer.value, -54)

        type_integer.value = 142344055
        self.assertEqual(type_integer.value, 142344055)

        type_integer = EntityTypeInteger(min_val=-1, max_val=1)

        type_integer.value = -1
        type_integer.value = 0
        type_integer.value = 1

        with self.assertRaises(ValueError):
            type_integer.value = -2

        with self.assertRaises(ValueError):
            type_integer.value = 2

        type_integer = EntityTypeInteger(min_val=0, max_val=0)
        type_integer.value = 0

        with self.assertRaises(ValueError):
            type_integer.value = 1

        def validate_function(value: int) -> None:
            if value != 5:
                raise ValueError("The value must be equal to 5.")

        type_integer = EntityTypeInteger(validate_function=validate_function)

        type_integer.value = 5

        with self.assertRaises(ValueError):
            type_integer.value = 1

    def test_type_float(self):
        """
        Tests the behavior of the `EntityTypeFloat` class.
        
        Verifies:
            - Type enforcement.
            - Boundary conditions.
            - Custom validation functions for floating-point values.
        """
        type_float = EntityTypeFloat()

        with self.assertRaises(TypeError):
            type_float.value = 1

        type_float.value = -54.5
        self.assertEqual(type_float.value, -54.5)

        type_float.value = 142344055.4234234
        self.assertEqual(type_float.value, 142344055.4234234)

        # Test boundaries
        type_float = EntityTypeFloat(min_val=-1.2, max_val=1.0)

        type_float.value = -1.2
        type_float.value = 0.0
        type_float.value = 1.0

        with self.assertRaises(ValueError):
            type_float.value = -1.3

        with self.assertRaises(ValueError):
            type_float.value = 1.4

        type_float = EntityTypeFloat(min_val=0.0, max_val=0.0)
        type_float.value = 0.0
        with self.assertRaises(ValueError):
            type_float.value = 0.1

        def validate_function(value: float) -> None:
            if value != 5.5:
                raise ValueError("The value must be equal to 5.0.")

        type_float = EntityTypeFloat(validate_function=validate_function)

        type_float.value = 5.5

        with self.assertRaises(ValueError):
            type_float.value = 1.0

    def test_type_string(self):
        """
        Tests the behavior of the `EntityTypeString` class.
        
        Verifies:
            - Type enforcement.
            - Boundary conditions.
            - Pattern matching.
            - Custom validation functions for strings.
        """
        type_string = EntityTypeString()

        # Ensure only strings are allowed
        with self.assertRaises(TypeError):
            type_string.value = 1

        ALPHABET: str = "a, B, c, d, e, f, g, h, i, j, k, l, m, n, O, p, q, R, s, t, u, v, w, x, y, z,"
        type_string.value = ALPHABET
        self.assertEqual(type_string.value, ALPHABET)

        type_string.value = ALPHABET.lower()
        self.assertNotEqual(type_string.value, ALPHABET)
        
        with self.assertRaises(AttributeError):
            type_string = EntityTypeString(min_length=-1)
            type_string.value = "1"

        with self.assertRaises(AttributeError):
            type_string = EntityTypeString(max_length=-1)
            type_string.value = "1"

        # Test boundary conditions for string length
        type_string = EntityTypeString(min_length=3, max_length=6)

        type_string.value = "QWE"
        type_string.value = "QWERTY"
        
        with self.assertRaises(ValueError):
            type_string.value = "QW" # Too short

        with self.assertRaises(ValueError):
            type_string.value = "QWERTYU" # Too long

        type_string = EntityTypeString(min_length=0, max_length=0)
        type_string.value = ""
        with self.assertRaises(ValueError):
            type_string.value = "Q"

        # Test allowed values
        type_string = EntityTypeString(allowed_values=["HI", "HeLlO", "привет"])
        
        type_string.value = "HI"
        type_string.value = "HeLlO"
        type_string.value = "привет"

        with self.assertRaises(ValueError):
            type_string.value = "1" # Not allowed

        with self.assertRaises(ValueError):
            type_string.value = "hi" # Not allowed

        with self.assertRaises(ValueError):
            type_string.value = "hElLo" # Not allowed

        with self.assertRaises(ValueError):
            type_string.value = "ПривеТ" # Not allowed

        # Test pattern matching
        type_string = EntityTypeString(pattern=r"\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b") # Regular expression pattern to match IPv4 addresses.

        # Valid IP addresses
        type_string.value = "127.0.0.1"
        type_string.value = "192.168.1.0"
        type_string.value = "0.0.0.0"
        type_string.value = "255.255.255.255"

        with self.assertRaises(ValueError):
            type_string.value = "255.251.254.256" # Invalid IP

        with self.assertRaises(ValueError):
            type_string.value = "Hello"

        def validate_function(value: str) -> None:
            if value != "Bye":
                raise ValueError("The variable value, must have the value 'Bye'.")

        type_string = EntityTypeString(validate_function=validate_function)

        type_string.value = "Bye"

        with self.assertRaises(ValueError):
            type_string.value = "Hi"

    def test_type_list(self):
        """
        Tests the behavior of the `EntityTypeList` class.
        
        Verifies:
            - Type enforcement.
            - Boundary conditions.
            - Allowed types within lists.
            - Custom validation functions for lists.
        """
        type_list = EntityTypeList()

        with self.assertRaises(TypeError):
            type_list.value = 1

        with self.assertRaises(TypeError):
            type_list.value = {}

        type_list.value = [1, 2, 3, 4]
        self.assertListEqual(type_list.value, [1, 2, 3, 4])

        type_list.value = ["one", "two", "three", "four"]
        self.assertListEqual(type_list.value, ["one", "two", "three", "four"])

        type_list.value = [1, "two", 3, "four"]
        self.assertListEqual(type_list.value, [1, "two", 3, "four"])

        self.assertNotEqual(type_list.value, ["one", "two", "three", "four", "five"])

        # Test boundary conditions for list length
        with self.assertRaises(AttributeError):
            type_list = EntityTypeList(min_length=-1)
            type_list.value = [1]

        with self.assertRaises(AttributeError):
            type_list = EntityTypeList(max_length=-1)
            type_list.value = [1]

        type_list = EntityTypeList(allowed_type=bool)

        type_list.value = [True, False, False, True]

        with self.assertRaises(TypeError):
            type_list.value = ["True", False, "False", True, 5]

        type_list = EntityTypeList(min_length=0, max_length=0)
        type_list.value = []
        with self.assertRaises(ValueError):
            type_list.value = [1]

        type_list = EntityTypeList(min_length=3, max_length=5)
        
        type_list.value = [1, "two", "three"]
        type_list.value = [1, "two", "three", "four", "five"]

        with self.assertRaises(ValueError):
            type_list.value = [1, "two"]

        with self.assertRaises(ValueError):
            type_list.value = [1, "two", "three", "four", "five", True]  # Too long

        def validate_function(value: list[int]) -> None:
            required_elements = [1, 2, 3, 4]
            if not all(element in value for element in required_elements):
                raise ValueError(f"Expected all elements {required_elements}, but some are missing in {value}.")

        type_list = EntityTypeList(validate_function=validate_function)

        type_list.value = [1, 2, 3, 4]

        with self.assertRaises(ValueError):
            type_list.value = [1, 2, 3]

    def test_type_dict(self):
        """
        Tests the behavior of the `EntityTypeDict` class.
        Verifies:
            - Type enforcement.
            - Boundary conditions.
            - Allowed key and value types.
            - Custom validation functions for dictionaries.
        """
        type_dict = EntityTypeDict()

        with self.assertRaises(TypeError):
            type_dict.value = []

        with self.assertRaises(TypeError):
            type_dict.value = 0

        with self.assertRaises(TypeError):
            type_dict.value = "{}"

        type_dict = EntityTypeDict(allowed_key_type=str)
        type_dict.value = {"key1": "value1"}
        with self.assertRaises(TypeError):
            type_dict.value = {0: "value1"}

        type_dict = EntityTypeDict(allowed_value_type=int)
        type_dict.value = {0: 1}
        with self.assertRaises(TypeError):
            type_dict.value = {0: "1"}

        with self.assertRaises(AttributeError):
            type_dict = EntityTypeDict(min_keys=-1)
            type_dict.value = {0: "1"}

        with self.assertRaises(AttributeError):
            type_dict = EntityTypeDict(max_keys=-1)
            type_dict.value = {0: "1"}

        type_dict = EntityTypeDict(min_keys=0, max_keys=0)
        type_dict.value = {}
        with self.assertRaises(ValueError):
            type_dict.value = {0: "1"}

        type_dict = EntityTypeDict(min_keys=3, max_keys=5)
        type_dict.value = {0: "1", 2: "3", 4: "5"}
        type_dict.value = {0: "1", 2: "3", 4: "5", 6: "7", 8: "9"}

        with self.assertRaises(ValueError):
            type_dict.value = {0: "1", 2: "3"}
        
        with self.assertRaises(ValueError):
            type_dict.value = {0: "1", 2: "3", 4: "5", 6: "7", 8: "9", 10: "11"}

        # Test required keys
        type_dict = EntityTypeDict(required_keys=["key1", "key2"])
        type_dict.value = {"key1": "value1", "key2": "value2"}

        with self.assertRaises(KeyError):
            type_dict.value = {"key1": "value1"} # Missing required key

        def validate_function(value: dict[str, int]) -> None:
            EXPECTED_RESULT: int = 3
            result: int = 0

            for _, val in value.items():
                result += val

            if result != EXPECTED_RESULT:
                raise ValueError(f"The sum of values is not equal to {EXPECTED_RESULT}")
            
        type_dict = EntityTypeDict(validate_function=validate_function)
        type_dict.value = {"0": 1, "1": 2}
        with self.assertRaises(ValueError):
            type_dict.value = {"0": 1, "1": 1}

    def test_type_bool(self):
        """
        Tests the behavior of the `EntityTypeBool` class.
        
        Verifies:
        - Type enforcement.
        - Allowed boolean values.
        - Custom validation functions for boolean types
        """
        type_bool = EntityTypeBool()

        with self.assertRaises(TypeError):
            type_bool.value = 0

        with self.assertRaises(TypeError):
            type_bool.value = 1

        with self.assertRaises(TypeError):
            type_bool.value = "True"

        with self.assertRaises(TypeError):
            type_bool.value = "False"

        type_bool.value = True
        self.assertEqual(type_bool.value, True)
        type_bool.value = False
        self.assertEqual(type_bool.value, False)

        def validate_function(value: bool) -> None:
            if value != False:
                raise ValueError("The value must be False")
            
        type_bool = EntityTypeBool(validate_function=validate_function)
        type_bool.value = False
        with self.assertRaises(ValueError):
            type_bool.value = True