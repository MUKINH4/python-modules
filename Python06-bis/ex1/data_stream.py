from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union


class DataProcessor(ABC):

    def __init__(self):
        self._storage: list[Any] = []
        self._rank_counter: int = 0
        self._total_processed: int = 0

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
                self._total_processed += 1
        else:
            self._storage.append(str(data))
            self._total_processed += 1


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
                self._total_processed += 1
        else:
            self._storage.append(str(data))
            self._total_processed += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_valid_dict(value: Any) -> bool:
            return isinstance(value, dict) and all(
                isinstance(key, str) and isinstance(item, str)
                for key, item in value.items()
            )

        if is_valid_dict(data):
            return True
        return isinstance(data, list) and all(
            is_valid_dict(item) for item in data
        )

    def ingest(
        self, data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict) -> str:
            level = d.get('log_level', '')
            msg = d.get('log_message', '')
            return f"{level}: {msg}"

        if isinstance(data, list):
            for item in data:
                self._storage.append(format_log(item))
                self._total_processed += 1
        else:
            self._storage.append(format_log(data))
            self._total_processed += 1


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            processor_name = processor.__class__.__name__.replace(
                "Processor", " Processor"
            )
            print(
                f"{processor_name}: total {processor._total_processed} "
                f"items processed, remaining {len(processor._storage)} "
                "on processor"
            )


if __name__ == "__main__":
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream = DataStream()

    stream_data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    data_stream.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    data_stream.register_processor(numeric_processor)
    print()
    print(f"Send first batch of data on stream: {stream_data}")
    data_stream.process_stream(stream_data)
    print()
    data_stream.print_processors_stats()

    print()
    print("Registering other data processors")
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    print("Send the same batch again")
    data_stream.process_stream(stream_data)
    print()
    data_stream.print_processors_stats()

    print()
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric_processor.output()
    for _ in range(2):
        text_processor.output()
    log_processor.output()
    print()
    data_stream.print_processors_stats()
