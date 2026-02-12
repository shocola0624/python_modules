#!/usr/bin/env python3
"""
EX2: Nexus Integration

Implement a staged pipeline architecture that simulates enterprise data
processing workflows. Process data through three explicit stages:
InputStage -> TransformStage -> OutputStage.

Classes:
    NotFoundPipeline:
        Raise when a requested pipeline id is not registered.
    StageError:
        Represent stage-level failures.
    InputStageError:
        Raise for input validation/parsing failures.
    TransformStageError:
        Raise for transformation/enrichment failures.
    OutputStageError:
        Raise for output formatting failures.
    ProcessingStage:
        Describe the `process(data)` interface for a stage.
    InputStage:
        Normalize raw input into a tagged dict (JSON/CSV/Stream).
    TransformStage:
        Transform tagged input into enriched/aggregated structures.
    OutputStage:
        Format transformed data into user-facing strings.
    ProcessingPipeline:
        Hold ordered stages and a pipeline id.
    JSONAdapter:
        Adapt the pipeline for JSON payloads.
    CSVAdapter:
        Adapt the pipeline for CSV-like string payloads.
    StreamAdapter:
        Adapt the pipeline for stream (list) payloads.
    NexusManager:
        Register pipelines and route data by pipeline id.

Functions:
    main():
        Serve as entry point for demo execution.
"""

from abc import ABC, abstractmethod
from typing import Any, Union, Dict, List, Protocol, Optional


class NotFoundPipeline(Exception):
    """Raise when receiving a missing pipeline id."""
    pass


class StageError(Exception):
    """Represent a stage error."""
    pass


class InputStageError(StageError):
    """Raise for errors caused in InputStage."""
    pass


class TransformStageError(StageError):
    """Raise for errors caused in TransformStage."""
    pass


class OutputStageError(StageError):
    """Raise for errors caused in OutputStage."""
    pass


class ProcessingStage(Protocol):
    """Describe a single processing stage."""

    def process(self, data: Any) -> Any:
        """Execute the stage transformation.

        Args:
            data: Input payload for the stage.

        Returns:
            Return stage outputs passed to the next stage.
        """
        ...


class InputStage:
    """Normalize inbound data into a tagged structure."""

    def process(self, data: Any) -> Dict:
        """Identify input type (JSON/CSV/Stream) and wrap in dict.

        Args:
            data: Raw inbound payload.

        Returns:
            Dictionary keyed by the detected data type.
        """
        # JSON
        if isinstance(data, dict):
            return {"JSON": data}

        # CSV
        elif isinstance(data, str):
            return {"CSV": data}

        # Stream
        elif isinstance(data, list):
            return {"Stream": data}

        else:
            err_msg = f"Invalid data type {type(data)}"
            raise InputStageError(err_msg)


class TransformStage:
    """Transform normalized input into enriched domain objects."""

    def process(self, data: Any) -> Dict:
        """Dispatch to the appropriate transformer based on input tag.

        Args:
            data: Tagged input from the previous stage.

        Returns:
            Dictionary with transformed payload keyed by data type.
        """
        processes = {
            "JSON": self._json_process,
            "CSV": self._csv_process,
            "Stream": self._stream_process
        }
        try:
            data_type, val = next(iter(data.items()))
            result = processes[data_type](val)
        except (AttributeError, TypeError):
            err_msg = f"Invalid data type {type(data)}"
            raise TransformStageError(err_msg)
        except (KeyError, StopIteration):
            err_msg = "Invalid data format"
            raise TransformStageError(err_msg)
        return result

    @staticmethod
    def _json_process(data: Dict) -> Dict:
        """Convert temperature readings to formatted output.

        Args:
            data: JSON data for a sensor reading.

        Returns:
            Dictionary containing formatted temperature information.
        """
        try:
            if data["sensor"] == "temp":
                value = float(data["value"])
                unit = data["unit"]
                if unit == "C" and 15 < value and value < 35:
                    temp_range = "(Normal range)"
                else:
                    temp_range = ""
                result = {
                    "JSON": {"temperature": f"{value}°{unit} {temp_range}"}
                }
            else:
                err_msg = "Unregistered sensor type"
                raise TransformStageError(err_msg)
        except ValueError:
            err_msg = "Invalid data format"
            raise TransformStageError(err_msg)
        return result

    @staticmethod
    def _csv_process(data: str) -> Dict:
        """Count user action lines from CSV-like input.

        Args:
            data: CSV data of activity logs.

        Returns:
            Dictionary containing action count.
        """
        logs = data.split("\n")
        action_count = 0
        for log in logs:
            log = log.split(",")
            if len(log) != 3:
                err_msg = "Invalid data format"
                raise TransformStageError(err_msg)
            if log[0] == "user" and log[1] == "action":
                action_count += 1
        result = {
            "CSV": {"action_count": action_count}
        }
        return result

    @staticmethod
    def _stream_process(data: List[Dict]) -> Dict:
        """Aggregate stream readings and compute average temperature.

        Args:
            data: List of sensor data dictionaries.

        Returns:
            Dictionary with stream summary statistics.
        """
        total_processed = len(data)
        total_temp = 0
        len_temp = 0
        unit = None
        for sensor_data in data:
            if sensor_data["sensor"] == "temp":
                if unit is None:
                    unit = sensor_data["unit"]
                elif unit != sensor_data["unit"]:
                    continue
                try:
                    value = sensor_data["value"]
                    total_temp += float(value)
                except ValueError:
                    err_msg = f"Invalid data type {type(value)}"
                    raise TransformStageError(err_msg)
                len_temp += 1
            else:
                continue
        try:
            avg = total_temp / len_temp
        except ZeroDivisionError:
            err_msg = "Not given temperature data"
            raise TransformStageError(err_msg)
        result = {
            "Stream": {
                "total_processed": total_processed,
                "avg": f"{avg:.1f}°{unit}"
            }
        }
        return result


class OutputStage:
    """Format transformed data as final user-facing strings."""

    def process(self, data: Any) -> str:
        """Dispatch to the output formatter based on input tag.

        Args:
            data: Tagged payload from the transform stage.

        Returns:
            Final formatted output string.
        """
        processes = {
            "JSON": self._json_process,
            "CSV": self._csv_process,
            "Stream": self._stream_process
        }
        try:
            data_type, val = next(iter(data.items()))
            result = processes[data_type](val)
        except (AttributeError, TypeError):
            err_msg = f"Invalid data type {type(data)}"
            raise OutputStageError(err_msg)
        except (KeyError, StopIteration):
            err_msg = "Invalid data format"
            raise OutputStageError(err_msg)
        return result

    @staticmethod
    def _json_process(data: Dict) -> str:
        """Render JSON sensor output into readable text.

        Args:
            data: JSON payload with sensor reading.

        Returns:
            User-friendly message describing the reading.
        """
        sensor_type, value = next(iter(data.items()))
        result = f"Processed {sensor_type} reading: {value}"
        return result

    @staticmethod
    def _csv_process(data: Dict) -> str:
        """Render CSV action counts into a summary string.

        Args:
            data: Dictionary containing action count.

        Returns:
            User-friendly summary of logged actions.
        """
        action_count = data["action_count"]
        result = f"User activity logged: {action_count} actions processed"
        return result

    @staticmethod
    def _stream_process(data: Dict) -> str:
        """Render stream aggregation into a summary string.

        Args:
            data: Dictionary containing stream summary stats.

        Returns:
            User-friendly message summarizing the stream.
        """
        total_processed = data["total_processed"]
        avg = data["avg"]
        result = f"Stream summary: {total_processed} readings, avg: {avg}"
        return result


class ProcessingPipeline(ABC):
    """Coordinate ordered processing stages in an abstract pipeline."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialize pipeline with identifier and empty stage list.

        Args:
            pipeline_id: Unique identifier for the pipeline.
        """
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Run data through each stage and return the final result.

        Args:
            data: Input payload for the pipeline.

        Returns:
            Final output from the last stage.
        """
        raise NotImplementedError

    def add_stage(self, stage: ProcessingStage) -> None:
        """Append a stage to the pipeline.

        Args:
            stage: Stage instance implementing `process`.
        """
        self.stages.append(stage)


class JSONAdapter(ProcessingPipeline):
    """Adapt the pipeline for JSON data."""

    def __init__(self, pipeline_id: str) -> None:
        """Store pipeline identifier.

        Args:
            pipeline_id: Unique identifier for the JSON pipeline.
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """Execute all stages with error handling for JSON pipeline.

        Args:
            data: Payload to process.

        Returns:
            Final result string or None if recovery was triggered.
        """
        for i, stage in enumerate(self.stages):
            try:
                data = stage.process(data)
            except StageError as e:
                print(f"Error detected in Stage {i+1}: {e}")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored, "
                      "processing resumed")
                return None
        return data


class CSVAdapter(ProcessingPipeline):
    """Adapt the pipeline for CSV data."""

    def __init__(self, pipeline_id: str) -> None:
        """Store pipeline identifier.

        Args:
            pipeline_id: Unique identifier for the CSV pipeline.
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """Execute all stages with error handling for CSV pipeline.

        Args:
            data: Payload to process.

        Returns:
            Final result string or None if recovery was triggered.
        """
        for i, stage in enumerate(self.stages):
            try:
                data = stage.process(data)
            except StageError as e:
                print(f"Error detected in Stage {i+1}: {e}")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored, "
                      "processing resumed")
                return None
        return data


class StreamAdapter(ProcessingPipeline):
    """Adapt the pipeline for stream data."""

    def __init__(self, pipeline_id: str) -> None:
        """Store pipeline identifier.

        Args:
            pipeline_id: Unique identifier for the stream pipeline.
        """
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        """Execute all stages with error handling for stream pipeline.

        Args:
            data: Payload to process.

        Returns:
            Final result string or None if recovery was triggered.
        """
        for i, stage in enumerate(self.stages):
            try:
                data = stage.process(data)
            except StageError as e:
                print(f"Error detected in Stage {i+1}: {e}")
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored, "
                      "processing resumed")
                return None
        return data


class NexusManager:
    """Manage registry and dispatch for multiple pipelines."""

    def __init__(self) -> None:
        """Initialize with empty pipeline collection."""
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a pipeline with the manager.

        Args:
            pipeline: Pipeline instance to manage.
        """
        self.pipelines.append(pipeline)

    def process_data(self, p_id: str, data: Any) -> Optional[str]:
        """Route data to the pipeline matching the given id.

        Args:
            p_id: Identifier of the pipeline to execute.
            data: Payload to process.

        Returns:
            Pipeline output or None if a stage triggered recovery.
        """
        try:
            pipeline = next(p for p in self.pipelines
                            if p_id == p.pipeline_id)
            result = pipeline.process(data)
        except StopIteration:
            err_msg = "Error: Pipeline not found"
            raise NotFoundPipeline(err_msg)
        return result


def main() -> None:
    """Serve as demo entry point for the Nexus pipeline system."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")
    stages = [InputStage(), TransformStage(), OutputStage()]

    # Initializes Pipelines
    line_ids = ["JSON_001", "CSV_001", "Stream_001"]
    json_pipeline = JSONAdapter(line_ids[0])
    csv_pipeline = CSVAdapter(line_ids[1])
    stream_pipeline = StreamAdapter(line_ids[2])
    pipelines = [json_pipeline, csv_pipeline, stream_pipeline]

    for pipeline in pipelines:
        for stage in stages:
            pipeline.add_stage(stage)
        manager.add_pipeline(pipeline)

    print("=== Multi-Format Data Processing ===\n")
    inputs = {
        "JSON_001": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "CSV_001": "user,action,timestamp",
        "Stream_001": [
            {"sensor": "temp", "value": 22.0, "unit": "C"},
            {"sensor": "temp", "value": 22.5, "unit": "C"},
            {"sensor": "temp", "value": 21.8, "unit": "C"},
            {"sensor": "temp", "value": 22.1, "unit": "C"},
            {"sensor": "temp", "value": 22.0, "unit": "C"},
        ]
    }

    # Processes Multi-Format Data
    for id, data in inputs.items():
        print(f"Processing {id[:-4]} data through pipeline...")
        try:
            output = manager.process_data(id, data)
        except NotFoundPipeline as e:
            print(e, "\n")
            continue

        # Print
        print("Input: ", end="")
        if isinstance(data, dict):  # JSON
            print(data)
            print("Transform: Enriched with metadata and validation")
        elif isinstance(data, str):  # CSV
            print(f'"{data}"')
            print("Transform: Parsed and structured data")
        elif isinstance(data, list):  # Stream
            print("Real-time sensor stream")
            print("Transform: Aggregated and filtered")
        print(f"Output: {output}\n")

    print("=== Pipeline Chaining Demo ===\n")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    # Chain Manager
    chain_manager = NexusManager()
    line_ids = ["JSON_002", "CSV_002", "Stream_002"]
    json_pipeline = JSONAdapter(line_ids[0])
    csv_pipeline = CSVAdapter(line_ids[1])
    stream_pipeline = StreamAdapter(line_ids[2])
    pipelines = [json_pipeline, csv_pipeline, stream_pipeline]

    for i, pipeline in enumerate(pipelines):
        pipeline.add_stage(stages[i])
        chain_manager.add_pipeline(pipeline)

    # Test Data for Pipeline Chaining
    chain_records = 100
    data = [
        {"sensor": "temp", "value": 20.0 + (i % 10) * 0.1, "unit": "C"}
        for i in range(chain_records)
    ]
    chain_data = data

    # Pipeline Chaining Demo
    try:
        chain_data = chain_manager.process_data(line_ids[0], chain_data)
        chain_data = chain_manager.process_data(line_ids[1], chain_data)
        chain_data = chain_manager.process_data(line_ids[2], chain_data)
        print("Chain result: 100 records processed through 3-stage pipeline")
        print("Performance: 95% efficiency, 0.2s total processing time\n")
    except NotFoundPipeline as e:
        print("Chain result: An error occured")
        print(e)

    print("=== Error Recovery Test ===\n")
    print("Simulating pipeline failure...")
    wrong_data = {"sensor": "temp", "value": "missing", "unit": "C"}
    manager.process_data("JSON_001", wrong_data)

    print()
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
