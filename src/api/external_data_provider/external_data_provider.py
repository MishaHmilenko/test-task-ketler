from src.interafaces.external_api_interfaces.external_data_provider import InterfaceExternalDataProvider


class ExternalDataProvider(InterfaceExternalDataProvider):

    def __init__(self, username: str) -> None:
        ...

    def get_username(self) -> str:
        ...

    def get_user_id(self) -> str:
        ...

    def get_user_full_name(self) -> str:
        ...

    def get_is_private(self) -> str:
        ...

    def get_last_post_url(self) -> str:
        ...
