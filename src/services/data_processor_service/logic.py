from src.interafaces.service_interfaces.comment_generator import InterfaceCommentGenerator
from src.interafaces.service_interfaces.data_processor import InterfaceDataProcessor
from src.interafaces.service_interfaces.external_data_source import InterfaceExternalDataSource
from src.interafaces.service_interfaces.image_caption_generation import InterfaceImageCaptionGeneration
from src.interafaces.service_interfaces.table import InterfaceTable


class DataProcessorService(InterfaceDataProcessor):

    def __init__(
            self,
            data: InterfaceExternalDataSource,
            caption_service: InterfaceImageCaptionGeneration,
            comment_service: InterfaceCommentGenerator,
            table_service: InterfaceTable,
    ) -> None:
        super().__init__(data)
        self.caption_service = caption_service
        self.comment_service = comment_service
        self.table_service = table_service

    async def data_processing(self) -> None:
        external_data = await self.data.get_external_data()

        for record in external_data:
            username = record.pop('username')
            await self.table_service.add_record_to_table(username, column_name='username')
            for key, val in record.items():

                if key == 'latest_media_url':
                    image_caption = await self.caption_service.get_caption(val)

                    await self.table_service.add_record_to_table(
                        values=await self.comment_service.generation_comment(image_caption),
                        column_name='personalized_message',
                        username=username
                    )
                    await self.table_service.add_record_to_table(
                        values=image_caption,
                        column_name='qualification_reason',
                        username=username
                    )

                await self.table_service.add_record_to_table(
                    values=val, column_name=key, username=username
                )
