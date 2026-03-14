from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0
        self.total_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        else:
            return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            "total_items": self.total_items,
        }


class SensorStream(DataStream):

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_data = []

        for data in data_batch:
            try:
                key, value = data.split(":")
                if float(value) >= float(criteria):
                    filtered_data.append(data)
            except (ValueError, TypeError):
                continue
        return filtered_data

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += 1
        self.total_items += len(data_batch)
        temporator = []
        for data in data_batch:
            try:
                key, value = data.split(":")
                if key == "temp":
                    temporator.append(float(value))
            except (ValueError, IndexError, AttributeError):
                continue
        if temporator:
            avg = sum(temporator) / len(temporator)
        else:
            avg = 0
        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg:.1f}°C"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = "sensor"
        return stats


class TransactionStream(DataStream):

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered_data = []
        for data in data_batch:
            try:
                action, cost = data.split(":")
                if float(cost) >= float(criteria):
                    filtered_data.append(data)
            except (ValueError, TypeError, AttributeError):
                continue
        return filtered_data

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += 1
        self.total_items += len(data_batch)
        net_flow = 0
        for data in data_batch:
            try:
                action, cost = data.split(":")
                cost = float(cost)
                if action == "buy":
                    net_flow += cost
                elif action == "sell":
                    net_flow -= cost
            except (ValueError, IndexError):
                continue
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {net_flow:+.0f} units"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = "transaction"
        return stats


class EventStream(DataStream):

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        filtered_data = []
        for event in data_batch:
            try:
                if criteria.lower() in str(event).lower():
                    filtered_data.append(event)
            except Exception:
                continue
        return filtered_data

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += 1
        self.total_items += len(data_batch)
        total_errors = 0
        for data in data_batch:
            if data == "error":
                total_errors += 1
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{total_errors} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["stream_type"] = "event"
        return stats


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, batches: List[List[Any]]) -> None:
        i = 0
        all_batches = len(batches)
        for stream in self.streams:
            if i < all_batches:
                try:
                    batch = batches[i]
                    result = stream.process_batch(batch)
                    print(result)
                except Exception as error:
                    print(
                        "Stream processing error in "
                        f"{stream.stream_id}: {error}"
                    )
            i += 1


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # 1. Initializing specific streams with the output style
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    print(sensor.process_batch(sensor_batch))
    print()
    print("Initializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")

    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(trans_batch)}]")
    print(transaction.process_batch(trans_batch))
    print()
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")

    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    print(event.process_batch(event_batch))

    # 2. Demonstrating Subtype Polymorphism (Mixed types in one list)
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    mixed_batches = [
        ["temp:24.0", "temp:25.0"],
        ["buy:500", "buy:200", "sell:100", "buy:50"],
        ["login", "error", "logout"],
    ]

    print("Batch 1 Results:")
    i = 0
    for stream in processor.streams:
        stream.process_batch(mixed_batches[i])
        if isinstance(stream, SensorStream):
            print(f"- Sensor data: {len(mixed_batches[i])} readings processed")
        elif isinstance(stream, TransactionStream):
            print(
                "- Transaction data: "
                f"{len(mixed_batches[i])} operations processed"
            )
        elif isinstance(stream, EventStream):
            print(f"- Event data: {len(mixed_batches[i])} events processed")
        i += 1

    # 3. Filtering Logic
    print("\nStream filtering active: High-priority data only")
    filtered_sensors = sensor.filter_data(["temp:24.0", "temp:25.0", "error"], "24")
    filtered_transaction = transaction.filter_data(["buy:500", None], "22")

    print(
        f"Filtered results: {len(filtered_sensors)} critical sensor alerts, "
        f"{len(filtered_transaction)} large transaction\n"
    )
    print("All streams processed successfully. Nexus throughput optimal.")
