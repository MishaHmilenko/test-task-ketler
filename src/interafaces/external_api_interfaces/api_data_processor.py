from abc import ABC, abstractmethod


class ApiConnector(ABC):

    @abstractmethod
    def connect(self) -> None:
        ...

    @abstractmethod
    def disconnect(self) -> None:
        ...


class InterfaceApiDataProcessor(ABC, ApiConnector):

    @abstractmethod
    async def data_processing(self) -> list[dict]:
        ...
