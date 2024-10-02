from abc import ABC, abstractmethod


class InterfaceDataCollector(ABC):

    @abstractmethod
    async def process_data_collecting(self, data: list[str]) -> list[dict]:
        ...
