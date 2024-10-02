from abc import ABC, abstractmethod


class InterfaceExternalDataProvider(ABC):

    @abstractmethod
    def get_username(self) -> str:
        ...

    @abstractmethod
    def get_user_id(self) -> str:
        ...

    @abstractmethod
    def get_user_full_name(self) -> str:
        ...

    @abstractmethod
    def get_is_private(self) -> str:
        ...

    @abstractmethod
    def get_last_post_url(self) -> str:
        ...

