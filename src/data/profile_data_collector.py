from src.api.external_data_provider.external_data_provider import ExternalDataProvider
from src.data.profile_data_processor import ProfileDataProcessor
from src.interafaces.data_interfaces.data_collector import InterfaceDataCollector


class ProfileDataCollector(InterfaceDataCollector):

    async def process_data_collecting(self, data: list[str]) -> list[dict]:
        collected_profile_data = []

        for record in data:
            profile_data: dict = await ProfileDataProcessor(ExternalDataProvider(record)).process_data()
            collected_profile_data.append(profile_data)

        return collected_profile_data


