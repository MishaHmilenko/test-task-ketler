from abc import ABC, abstractmethod


class InterfaceExternalDataSource(ABC):

    @abstractmethod
    async def get_external_data(self) -> list[dict]:
        ...
