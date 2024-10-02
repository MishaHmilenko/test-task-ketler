from abc import ABC, abstractmethod


class InterfaceAPIClient(ABC):
    @abstractmethod
    def get_headers(self) -> dict:
        ...

    @abstractmethod
    def get_url(self, **kwargs) -> str:
        ...

    @abstractmethod
    def get_body(self, **kwargs) -> dict:
        ...