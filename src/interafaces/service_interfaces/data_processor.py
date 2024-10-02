from abc import ABC, abstractmethod

from src.interafaces.service_interfaces.external_data_source import InterfaceExternalDataSource


class InterfaceDataProcessor(ABC):

    def __init__(self, data: InterfaceExternalDataSource) -> None:
        self.data = data

    @abstractmethod
    async def data_processing(self) -> None:
        ...
