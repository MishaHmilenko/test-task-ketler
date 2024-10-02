from src.interafaces.external_api_interfaces.api_client import InterfaceAPIClient
from src.interafaces.external_api_interfaces.api_comment_generator import InterfaceCommentGeneratorAPI
from src.interafaces.service_interfaces.comment_generator import InterfaceCommentGenerator


class CommentGeneratorService(InterfaceCommentGenerator):

    def __init__(self, api_generator: InterfaceCommentGeneratorAPI, api_client: InterfaceAPIClient) -> None:
        super().__init__(api_generator)
        self.api_client = api_client

    def get_comment_from_response(self, response: dict) -> str:
        return response['data']['outputs'][0]['text']

    async def generation_comment(self, caption: str) -> str:
        response = await self.api_generator.get_comment_query(
            self.api_client.get_url(),
            headers=self.api_client.get_headers(),
            body=self.api_client.get_body(caption=caption)
        )
        return self.get_comment_from_response(response)
