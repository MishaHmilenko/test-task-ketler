import asyncio

from src.api.comment_generator.api_client import CommentGeneratorAPIClient
from src.api.comment_generator.comment_generator import CommentGeneratorAPI
from src.api.google_sheet.api_client import GoogleSheetTableAPIClient
from src.api.google_sheet.google_sheet import GoogleSheetTableAPI
from src.data.data_source import FileDataSource
from src.data.profile_data_collector import ProfileDataCollector
from src.services.comment_generation_service.logic import CommentGeneratorService
from src.services.data_parser_service.logic import DataParserService
from src.services.data_processor_service.logic import DataProcessorService
from src.services.external_data_source_service.logic import ExternalDataSourceService, ExternalDataSourceServiceExample
from src.services.google_sheet_table_service.logic import GoogleSheetTableService
from src.services.image_caption_generation_service.logic import ImageCaptionGenerationService


def initialize_services() -> DataProcessorService:
    data_source = FileDataSource('logins')
    data_parser = DataParserService(data=data_source)
    profile_data_collector = ProfileDataCollector()
    external_data = ExternalDataSourceServiceExample()

    repository = GoogleSheetTableAPI()
    comment_api_generator = CommentGeneratorAPI()

    table_api_client = GoogleSheetTableAPIClient()
    comment_generator_api_client = CommentGeneratorAPIClient()

    table = GoogleSheetTableService(table_repo=repository, api_client=table_api_client)
    caption_service = ImageCaptionGenerationService()
    comment_service = CommentGeneratorService(
        api_generator=comment_api_generator, api_client=comment_generator_api_client
    )

    return DataProcessorService(
        table_service=table,
        caption_service=caption_service,
        comment_service=comment_service,
        data=external_data
    )


async def start_script():
    data_processor = initialize_services()
    await data_processor.data_processing()

if __name__ == '__main__':
    asyncio.run(start_script())
