#!/usr/bin/env python3
"""
EX1: Polymorphic Streams

Implement a sophisticated data streaming system that demonstrates advanced
polymorphic behavior.

Classes:
    DataStream:
        Define the common stream interface.
    SensorStream:
        Handle sensor readings (e.g., temperature/pressure dicts).
    TransactionStream:
        Handle buy/sell operations and flow metrics.
    EventStream:
        Handle string events and detect errors.
    StreamProcessor:
        Select a concrete stream class from a stream_id.

Functions:
    polymorphic_stream_system:
        Run a single test case using a chosen stream class.
    polymorphic_stream_process:
        Run multiple test cases through StreamProcessor.
    main:
        Serve as entry point for demo execution.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Define an abstract base class.

    Subclasses must implement:
        process_batch: Process a batch of data

    Attributes:
        stream_id: Identifier for the data stream.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize DataStream.

        Args:
            stream_id: Identifier for the data stream.
        """
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a data batch and return a result string.

        Args:
            data_batch: Collection of raw stream records.

        Returns:
            A human-readable summary of the processed batch.
        """
        raise NotImplementedError

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Apply base filtering to a data batch.

        Args:
            data_batch: Raw batch to inspect.
            criteria: Optional filtering rule.

        Returns:
            Filtered list based on criteria.
        """
        if not isinstance(data_batch, list):
            return list()
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Report basic stream metadata.

        Returns:
            Dictionary containing the stream identifier.
        """
        return {
            "stream_id": self.stream_id
        }


class SensorStream(DataStream):
    """Process environmental sensor readings.

    Attributes:
        stream_id: Identifier for the sensor stream.
        processed: Number of processed data.
        avg: Average of the temperature.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize SensorStream.

        Args:
            stream_id: Identifier for the sensor stream.
        """
        super().__init__(stream_id)
        self.processed = 0
        self.avg = None

    def process_batch(self, data_batch: List[Any]) -> str:
        """Summarize sensor readings and compute average temperature.

        Args:
            data_batch: Collection of sensor readings.

        Returns:
            Summary string including count and optional average temperature.
        """
        data_batch = self.filter_data(data_batch)
        if not data_batch:
            return "0 readings processed"

        length = len(data_batch)
        res = f"{length} readings processed"
        self.processed = length
        avg = None

        try:
            temps = [temp for temp in data_batch
                     if len(temp) == 1 and "temp" in temp.keys()]
            if temps:
                avg = sum(value for temp in temps
                          for value in temp.values()) / len(temps)
        except (AttributeError, TypeError):
            pass

        if avg is not None:
            res += f", avg temp: {avg}°C"
            self.avg = avg
        return res

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor readings.

        Args:
            data_batch: Raw batch to inspect.
            criteria: Optional filtering rule.

        Returns:
            Filtered list based on criteria.
        """
        data_batch = super().filter_data(data_batch, criteria)

        if not criteria:
            return data_batch

        filtered = [data for data in data_batch
                    if isinstance(data, dict) and len(data) == 1]

        if criteria == "High-priority":
            filtered = [data for data in filtered
                        for key, value in data.items()
                        if key == "pressure"
                        and isinstance(value, (int, float))
                        and value > 1020]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return processed count and optional average temperature.

        Returns:
            Dictionary with processed count and optional average temp.
        """
        stats = super().get_stats()
        stats["processed"] = self.processed
        if self.avg is not None:
            stats["average"] = self.avg
        return stats


class TransactionStream(DataStream):
    """Process financial transactions.

    Attributes:
        stream_id: Identifier for the transaction stream.
        processed: Number of processed data.
        net_flow: Net flows of transactions.
        total_flow: Total flows of transactions.
        large: Number of large transactions.
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize TransactionStream.

        Args:
            stream_id: Identifier for the transaction stream.
        """
        super().__init__(stream_id)
        self.processed = 0
        self.net_flow = 0
        self.total_flow = 0
        self.large = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Compute net flow and count operations for a batch.

        Args:
            data_batch: Collection of transaction records.

        Returns:
            Summary string including processed count and net flow.
        """
        data_batch = self.filter_data(data_batch)
        if not data_batch:
            return "0 operations processed"

        self.net_flow = 0
        length = len(data_batch)
        res = f"{length} operations processed"
        self.processed = length

        try:
            self.net_flow += sum(value for data in data_batch
                                 if isinstance(data, dict)
                                 for key, value in data.items()
                                 if key == "buy")
            self.net_flow -= sum(value for data in data_batch
                                 if isinstance(data, dict)
                                 for key, value in data.items()
                                 if key == "sell")
            self.total_flow += self.net_flow
        except (AttributeError, TypeError):
            return res

        if self.net_flow == 0:
            return res

        res += ", net flow: "
        if self.net_flow > 0:
            res += f"+{self.net_flow} units"
        else:
            res += f"{self.net_flow} units"
        return res

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter large transactions if criteria demands.

        Args:
            data_batch: Raw batch to inspect.
            criteria: Optional filtering rule.

        Returns:
            Filtered list based on criteria.
        """
        data_batch = super().filter_data(data_batch, criteria)

        if not criteria:
            return data_batch

        filtered = [data for data in data_batch
                    if isinstance(data, dict) and len(data) == 1]

        if criteria == "High-priority":
            filtered = [data for data in filtered for value in data.values()
                        if isinstance(value, int) and value > 500]
            self.large = len(filtered)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return processed totals and large transaction count.

        Returns:
            Dictionary with counts, flows, and large transaction tally.
        """
        stats = super().get_stats()
        stats["processed"] = self.processed
        stats["net flow"] = self.net_flow
        stats["total flow"] = self.total_flow
        if self.large > 0:
            stats["large"] = self.large
        return stats


class EventStream(DataStream):
    """Process log/event messages.

    Attributes:
        stream_id: Identifier for the event stream.
        processed: Number of processed data.
        error: Number of errors
    """

    def __init__(self, stream_id: str) -> None:
        """Initialize EventStream.

        Args:
            stream_id: Identifier for the event stream.
        """
        super().__init__(stream_id)
        self.processed = 0
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Count events and detect number of error entries.

        Args:
            data_batch: Collection of event messages.

        Returns:
            Summary string including event count and any errors.
        """
        data_batch = self.filter_data(data_batch)
        if not data_batch:
            return "0 events processed"

        length = len(data_batch)
        res = f"{length} events processed"
        self.processed = length

        try:
            self.error = len([data for data in data_batch if data == "error"])
        except TypeError:
            return res

        if self.error > 0:
            res += f", {self.error} error detected"
        return res

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Return only string events, optionally only errors.

        Args:
            data_batch: Raw batch to inspect.
            criteria: Optional filtering rule.

        Returns:
            Filtered list based on criteria.
        """
        data_batch = super().filter_data(data_batch, criteria)

        if not criteria:
            return data_batch

        filtered = [data for data in data_batch if isinstance(data, str)]

        if criteria == "High-priority":
            filtered = [data for data in filtered if data == "error"]
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return processed count and error tally.

        Returns:
            Dictionary with processed count and error total.
        """
        stats = super().get_stats()
        stats["processed"] = self.processed
        stats["error"] = self.error
        return stats


class StreamProcessor:
    """Handle multiple stream types polymorphically.

    Attributes:
        stream_id: Identifier for the event stream.
        stream: Chosen DataStream
    """

    def __init__(self, stream_id: str) -> None:
        """Instantiate streams based on `stream_id` prefix.

        Args:
            stream_id: Identifier used to select concrete stream.
        """
        self.stream_id = stream_id
        streams = {
            "SENSOR": SensorStream,
            "TRANS": TransactionStream,
            "EVENT": EventStream
        }
        try:
            stream = self.stream_id[:-4]
            self.stream = streams[stream](self.stream_id)
        except KeyError:
            self.stream = None

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch through the selected stream, returning summary.

        Args:
            data_batch: Batch to process.

        Returns:
            Summary string or error message if stream not found.
        """
        if self.stream:
            return self.stream.process_batch(data_batch)
        return "ERROR: stream not found"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data batch using the stream-specific rules.

        Args:
            data_batch: Raw batch to inspect.
            criteria: Optional filtering rule.

        Returns:
            Filtered data or empty list if stream unavailable.
        """
        if self.stream:
            return self.stream.filter_data(data_batch, criteria)
        return list()

    def filter_data_test(self, data_batch: List[Any],
                         criteria: Optional[str] = None) -> str:
        """Test filter behavior and return formatted status.

        Args:
            data_batch: Batch to filter.
            criteria: Optional filtering rule.

        Returns:
            Formatted status string describing filtered results.
        """
        filtered = self.filter_data(data_batch, criteria)
        length = len(filtered)
        if length < 1:
            return ""
        results = {
            "SENSOR": f"{length} critical sensor alerts",
            "TRANS": f"{length} large transaction",
            "EVENT": f"{length} errors"
        }

        try:
            return results[self.stream_id[:-4]]
        except KeyError:
            return "ERROR: Invalid Stream ID"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stats from the underlying stream.

        Returns:
            Dictionary of stream statistics, or empty if none.
        """
        if self.stream:
            return self.stream.get_stats()
        return dict()


def polymorphic_stream_system(test_case: Dict) -> None:
    """Run a single stream test case and print analysis output.

    Args:
        test_case: Dictionary describing the stream and batch to process.
    """
    streams = {
        "SENSOR": SensorStream,
        "TRANS": TransactionStream,
        "EVENT": EventStream
    }
    try:
        stream = test_case["stream"]
        stream_id = test_case["stream_id"]
        stream_type = test_case["stream_type"]
        data_batch = test_case["batch"]
        processor = streams[stream_id[:-4]](stream_id)
    except KeyError:
        return
    processed_data = processor.process_batch(data_batch)

    data_batch_str = ""
    for s in str(data_batch):
        if s not in "{}'":
            data_batch_str += s

    print(f"Initializing {stream} Stream...\n"
          f"Stream ID: {stream_id}, Type: {stream_type}\n"
          f"Processing {stream} Batch: {data_batch_str}\n"
          f"{stream} Analysis: {processed_data}\n")


def polymorphic_stream_process(test_cases: List[Dict]) -> None:
    """Process multiple test cases through StreamProcessor.

    Args:
        test_cases: Collection of test case dictionaries to process.
    """
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    for test_case in test_cases:
        try:
            stream = test_case["stream"]
            stream_id = test_case["stream_id"]
            data_batch = test_case["batch"]
        except KeyError:
            continue
        processor = StreamProcessor(stream_id)
        processed_data = processor.process_batch(data_batch)
        print(f"- {stream} data: {processed_data}")
    print()

    criteria = "High-priority"
    print(f"Stream filtering active: {criteria} data only")
    results = ""
    for test_case in test_cases:
        try:
            stream = test_case["stream"]
            stream_id = test_case["stream_id"]
            data_batch = test_case["batch"]
        except KeyError:
            continue
        processor = StreamProcessor(stream_id)
        res = processor.filter_data_test(data_batch, criteria)
        if res != "" and results != "":
            results += ", "
        results += res
    print(f"Filtered results: {results}\n")


def main() -> None:
    """Run polymorphic stream system demo."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    test_cases1 = [
        {
            "stream": "Sensor",
            "stream_id": "SENSOR_001",
            "stream_type": "Environmental Data",
            "batch": [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}]
        },
        {
            "stream": "Transaction",
            "stream_id": "TRANS_001",
            "stream_type": "Financial Data",
            "batch": [{"buy": 100}, {"sell": 150}, {"buy": 75}]
        },
        {
            "stream": "Event",
            "stream_id": "EVENT_001",
            "stream_type": "System Events",
            "batch": ["login", "error", "logout"]
        }
    ]
    for test_case in test_cases1:
        polymorphic_stream_system(test_case)

    print("=== Polymorphic Stream Processing ===")
    test_cases2 = [
        {
            "stream": "Sensor",
            "stream_id": "SENSOR_001",
            "batch": [{"pressure": 3000}, {"pressure": 5000}]
        },
        {
            "stream": "Transaction",
            "stream_id": "TRANS_001",
            "batch": [
                {"buy": 300}, {"buy": 500}, {"buy": 300}, {"sell": 1100}
            ]
        },
        {
            "stream": "Event",
            "stream_id": "EVENT_001",
            "batch": ["login", "kill", "logout"]
        }
    ]
    polymorphic_stream_process(test_cases2)

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
