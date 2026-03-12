from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Compute the result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if the data is valid"""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatting"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid numeric data"
        count = len(data)
        sum_data = sum(data)
        avg_data = sum_data / count
        return f"Processed {count} numeric values, sum={sum_data}, avg={avg_data}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data) and len(data) > 0

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid text data"
        chars = len(data)
        words = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid log data"
        str1, str2 = data.split(":")
        str2 = str2.strip()
        if str1 == "ERROR":
            return f"[ALERT] {str1} level detected: {str2}"
        else:
            return f"[INFO] {str1} level detected: {str2}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, result: str) -> str:
        return super().format_output(result)


# === MAIN PROGRAM ===
if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric Processor
    print("Initializing Numeric Processor...")
    numeric_data = [1, 2, 3, 4, 5]
    processor = NumericProcessor()
    print(f"Processing data: {numeric_data}")
    if processor.validate(numeric_data):
        print("Validation: Numeric data verified")
        result = processor.process(numeric_data)
        print(processor.format_output(result))
    print()

    # Text Processor
    print("Initializing Text Processor...")
    text_data = "Hello Nexus World"
    processor = TextProcessor()
    print(f'Processing data: "{text_data}"')
    if processor.validate(text_data):
        print("Validation: Text data verified")
        result = processor.process(text_data)
        print(processor.format_output(result))
    print()

    # Log Processor
    print("Initializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    processor = LogProcessor()
    print(f'Processing data: "{log_data}"')
    if processor.validate(log_data):
        print("Validation: Log entry verified")
        result = processor.process(log_data)
        print(processor.format_output(result))
    print()

    # Polymorphic
    print("=== Polymorphic Processing Demo ===\n")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data_test = [[1, 2, 3], "Hello World!", "INFO: System ready"]


    for i in range(len(processors)):
        proc = processors[i]
        data = data_test[i]
        if proc.validate(data):
            result = proc.process(data)
            print(proc.format_output(result))

    print("\nFoundation systems online. Nexus ready for advanced streams.")
