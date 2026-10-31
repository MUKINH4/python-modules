from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict


class DataProcessor(ABC):

    def __init__(self):
        self._storage: list[Any] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")
        self._rank_counter += 1
        item = self._storage.pop(0)
        return (self._rank_counter, item)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (float, int)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_valid_dict(d: Any) -> bool:
            if isinstance(d, dict):
                for k, v in d.items():
                    return all(isinstance(k, str)) and all(isinstance(v, str))
        if is_valid_dict(data):
            return True
        if isinstance(data, dict):
            return all(is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict) -> str:
            level = d.get('log_level', '')
            msg = d.get('log_message', '')
            return f"{level}: {msg}"

        if isinstance(data, list):
            for item in data:
                self._storage.append(format_log(item))
        else:
            self._storage.append(format_log(data))