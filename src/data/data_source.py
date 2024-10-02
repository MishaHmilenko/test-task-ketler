import aiofiles

from src.interafaces.data_interfaces.data_source import InterfaceDataSource


class FileDataSource(InterfaceDataSource):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    async def read_data(self) -> list[str]:
        async with aiofiles.open(self.file_path, mode='r', encoding='utf-8') as file:
            return await file.readlines()