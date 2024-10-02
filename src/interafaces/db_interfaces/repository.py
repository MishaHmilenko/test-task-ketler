from abc import ABC, abstractmethod
from typing import Any


class InterfaceRepository(ABC):

    @abstractmethod
    async def get_value(self, **kwargs: Any) -> str | list[str]:
        ...

    @abstractmethod
    async def add_value(self, **kwargs: Any) -> None:
        ...
