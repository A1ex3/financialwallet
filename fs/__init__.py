import json
import os
from typing import Any

class File:
    def __init__(self) -> None:
        self.FILENAME: str = "data.json"
        self.__ensure_file_exists()

    def __ensure_file_exists(self) -> None:
        if not os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'w', encoding='utf-8') as f:
                json.dump({
                    "list": []
                }, f, ensure_ascii=False)

    def write_json(self, data: dict[str, list[dict[str, Any]]], encoding='utf-8') -> None:
        with open(self.FILENAME, 'w', encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False)

    def read_json(self) -> dict[str, list[dict[str, Any]]]:
        with open(self.FILENAME, 'r', encoding='utf-8') as f:
            data: dict[str, list[dict[str, Any]]] = json.load(f)

        return data
