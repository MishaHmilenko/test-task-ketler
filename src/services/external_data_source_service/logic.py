from src.interafaces.data_interfaces.data_collector import InterfaceDataCollector
from src.interafaces.service_interfaces.data_parser import InterfaceDataParser
from src.interafaces.service_interfaces.external_data_source import InterfaceExternalDataSource


class ExternalDataSourceService(InterfaceExternalDataSource):

    def __init__(self, data_parser: InterfaceDataParser, data_collector: InterfaceDataCollector):
        self.data_parser = data_parser
        self.data_collector = data_collector

    async def get_external_data(self) -> list[dict]:
        parsed_data = await self.data_parser.parse()
        return await self.data_collector.process_data_collecting(parsed_data)


class ExternalDataSourceServiceExample(InterfaceExternalDataSource):
    async def get_external_data(self) -> list[dict]:
        return [
            {
                'username': 'alice_wonder',
                'id': '456123789',
                'full_name': 'Alice Wonder',
                'is_private': '1',
                'latest_media_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi3vlT5dDAjGcfFMvv4WTu5P-go2UphNmvbQ&s'
            },
            {
                'username': 'jane_smith',
                'id': '987654321',
                'full_name': 'Jane Smith',
                'is_private': '0',
                'latest_media_url': 'https://img2.akspic.ru/previews/5/0/8/8/7/178805/178805-muzhchina-lazurnyj-solnechnye_ochki-purpur-rukav-500x.jpg'
            },
            {
                'username': 'john_doe',
                'id': '123456789',
                'full_name': 'John Doe',
                'is_private': '1',
                'latest_media_url': 'https://lemon.school/storage/2023/07/img_7017-780x258.png'
            }
        ]
