from abc import ABC, abstractmethod

from src.interafaces.external_api_interfaces.external_data_provider import InterfaceExternalDataProvider


class InterfaceDataProcessor(ABC):

    def __init__(self, data_provider: InterfaceExternalDataProvider) -> None:
        self.data_provider = data_provider

    @abstractmethod
    async def process_data(self) -> dict:
        ...
