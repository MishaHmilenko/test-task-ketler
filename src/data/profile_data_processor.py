from src.interafaces.data_interfaces.data_processor import InterfaceDataProcessor


class ProfileDataProcessor(InterfaceDataProcessor):

    async def process_data(self) -> dict:
        return {
            'username': self.data_provider.get_username(),
            'id': self.data_provider.get_user_id(),
            'full_name': self.data_provider.get_user_full_name(),
            'is_private': self.data_provider.get_is_private(),
            'latest_media_url': self.data_provider.get_last_post_url()
        }
