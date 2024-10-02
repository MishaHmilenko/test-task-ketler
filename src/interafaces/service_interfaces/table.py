from abc import ABC

from src.interafaces.db_interfaces.repository import InterfaceRepository


class InterfaceTable(ABC):

    def __init__(self, table_repo: InterfaceRepository) -> None:
        self.table_repo = table_repo

    async def add_record_to_table(self, values: str | list[str], **kwargs: str):
        ...
