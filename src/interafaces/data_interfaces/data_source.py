from abc import ABC, abstractmethod


class InterfaceDataSource(ABC):

    @abstractmethod
    async def read_data(self) -> list[str]:
        ...
