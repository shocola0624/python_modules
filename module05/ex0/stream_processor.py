#!/usr/bin/env python3
"""
EX0: Data Processor Foundation

Demonstrate a simple polymorphic processing system using an abstract base
class (ABC). Use multiple concrete processors that share the same interface
(`process`, `validate`, and `format_output`) interchangeably.

Classes:
    DataProcessor:
        Define the processing interface.
    NumericProcessor:
        Process a list of numbers (count, sum, average).
    TextProcessor:
        Process a string (character count, word count).
    LogProcessor:
        Process a log line and tag severity (INFO/ERROR).

Functions:
    data_processor_foundation:
        Select a processor by name in a factory-style demo.
    polymorphic_demo:
        Run several processors through the same interface.
    main:
        Serve as entry point for demo execution.
"""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Define the common processing interface.

    Subclasses must implement:
        process: Convert raw input into a result string
        validate: Return True if `data` is acceptable for that processor
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process `data` and return a result string.

        Args:
            data: Any input to be processed.

        Returns:
            Return a result string describing the processed data,
            or an error string starting with "[ERROR]"
            if processing is not possible.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether `data` is valid input for this processor.

        Args:
            data: Any input to be processed.

        Returns:
            Return True if `data` can be processed by this processor,
            otherwise False.
        """
        raise NotImplementedError

    def format_output(self, result: str) -> str:
        """Return the output string.

        Args:
            result: The raw result string.

        Returns:
            If `result` starts with "[ERROR]", return it unchanged.
            Otherwise, return "Processed " + result.
        """
        if result[:7] == "[ERROR]":
            return result
        return "Processed " + result


class NumericProcessor(DataProcessor):
    """Process numeric lists."""

    def process(self, data: Any) -> str:
        """Process the data and return the result string.

        Args:
            data: A list of numbers.

        Returns:
            (str) The result string including...
            - The number of processed numeric values
            - Sum of the numbers
            - Average of the numbers
            If `data` is not a list of numbers, return an error message.
        """
        if not self.validate(data):
            return "[ERROR] Validation failed: expected a list of numbers"
        total = sum(data)
        length = len(data)
        average = total / length
        return f"{length} numeric values, sum={total}, avg={average:.1f}"

    def validate(self, data: Any) -> bool:
        """Check whether `data` is numeric.

        Args:
            data: Any input to be processed.

        Returns:
            Return True if `data` is numeric, otherwise False.
        """
        try:
            total = 0
            length = 0
            for i in data:
                total += i
                length += 1
            if length == 0:
                return False
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        """Use the base formatting rule for numeric results."""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    """Process plain text strings."""

    def process(self, data: Any) -> str:
        """Process the data and return the result string.

        Args:
            data: A string.

        Returns:
            (str) The result string including...
            - The number of letters
            - The number of words
            If `data` is not a string, return an error message.
        """
        if not self.validate(data):
            return "[ERROR] Validation failed: expected a string"
        total = 0
        words = 0
        countable = True
        for i in data:
            total += 1
            if i == " ":
                countable = True
            elif countable:
                words += 1
                countable = False
        return f"text: {total} characters, {words} words"

    def validate(self, data: Any) -> bool:
        """Validate that input behaves like a string.

        Args:
            data: Any value.

        Returns:
            Return True if `data` can be concatenated with a string,
            otherwise False.
        """
        try:
            _ = data + "a"
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        """Use the base formatting rule for text results."""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    """Process log messages."""

    def process(self, data: Any) -> str:
        """Process the data and return the result string.

        Args:
            data: A log message.

        Returns:
            (str) The result string added tags depending on prefix.
            If `data` is not a string, return an error message.
        """
        if not self.validate(data):
            return "[ERROR] Validation failed: expected a string"
        if data[:5] == "ERROR":
            return "[ALERT] ERROR level detected" + data[5:]
        elif data[:4] == "INFO":
            return "[INFO] INFO level detected" + data[4:]
        else:
            return data

    def validate(self, data: Any) -> bool:
        """Validate that input behaves like a string.

        Args:
            data: Any value.

        Returns:
            Return True if `data` can be concatenated with a string,
            otherwise False.
        """
        try:
            _ = data + "a"
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        """Return log results unchanged (no base prefixing)."""
        return result


def data_processor_foundation(name: str, data: Any) -> None:
    """Run a single processor by name and print the full demo output.

    Args:
        name: Processor name ("Numeric", "Text", or "Log").
        data: Input data for that processor.
    """

    processors = {
        "Numeric": NumericProcessor,
        "Text": TextProcessor,
        "Log": LogProcessor
    }
    try:
        prcs = processors[name]()
    except KeyError:
        print(f"[ERROR] Unknown processor name: {name}")
        return

    print(f"Initializing {name} Processor...")
    shown = f"{data}" if name == "Numeric" else f"\"{data}\""
    print(f"Processing data: {shown}")
    print(f"Validation: {name} data "
          f"{'verified' if prcs.validate(data) else 'not verified'}")

    output = prcs.format_output(prcs.process(data))
    print(f"Output: {output}\n")


def polymorphic_demo() -> None:
    """Demonstrate polymorphism by running different processors."""
    processors = [NumericProcessor, TextProcessor, LogProcessor]
    data = [[1, 2, 3], "Hello  World", "INFO: System ready"]
    for i in range(3):
        prcs = processors[i]()
        output = prcs.format_output(prcs.process(data[i]))
        print(f"Result {i + 1}: {output}")


def main() -> None:
    """Run data processor demo.

    Executes:
        - a named-processor demo for Numeric/Text/Log
        - a polymorphic demo showing uniform handling via the base interface
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    data_processor_foundation("Numeric", [1, 2, 3, 4, 5])
    data_processor_foundation("Text", "Hello Nexus World")
    data_processor_foundation("Log", "ERROR: Connection timeout")

    print("=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...")
    polymorphic_demo()
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
