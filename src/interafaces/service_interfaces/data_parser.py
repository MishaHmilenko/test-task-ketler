from abc import ABC, abstractmethod


class InterfaceDataParser(ABC):

    @abstractmethod
    async def parse(self) -> list[str]:
        ...
