from src.interafaces.data_interfaces.data_source import InterfaceDataSource
from src.interafaces.service_interfaces.data_parser import InterfaceDataParser


class DataParserService(InterfaceDataParser):

    def __init__(self, data: InterfaceDataSource):
        self.data = data

    async def parse(self) -> list[str]:
        return [record.strip() for record in await self.data.read_data()]
