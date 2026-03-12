from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria == None:
            return data_batch
        else:
            return [item for item in data_batch if criteria in str(item)]
    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            "total_items": self.total_items
        }


class SensorStream(DataStream):

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
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
        temporator = []
        for data in data_batch:
            key, value = data.split(":")
            if key == "temp":
                temporator.append(float(value))
        if temporator:
            avg = sum(temporator) / len(temporator)
        else:
            avg = 0
        return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg:.1f}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

class TransactionStream(DataStream):

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered_data = []
        for data in data_batch:
            try:
                action, cost = data.split(":")
                if float(cost) >= float(criteria):
                    filtered_data.append(data)
            except (ValueError, TypeError):
                continue
        return filtered_data

    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow = 0
        for data in data_batch:
            action, cost = data.split(":")
            cost = float(cost)
            if action == "buy":
                net_flow += cost
            elif action == "sell":
                net_flow -= cost
        return f"Transaction analysis: {len(data_batch)} operations, net flow: {net_flow:+.0f} units"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

class EventStream(DataStream):

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
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
        total_errors = 0
        for data in data_batch:
            if data == "error":
                total_errors += 1
        return f"Event analysis: {len(data_batch)} events, {total_errors} error detected"
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
class StreamProcessor:

    def __init__(self):
        self.streams = []
    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)
    def process_streams(self, batches: List[List[Any]]) -> None:
        i = 0
        for stream in self.streams:
            try:
                batch = batches[i]
                result = stream.process_batch(batch)
                print(result)
            except Exception as error:
                print(f"Stream processing error: {error}")
            i += 1

