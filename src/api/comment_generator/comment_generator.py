import aiohttp
from src.interafaces.external_api_interfaces.api_comment_generator import InterfaceCommentGeneratorAPI


class CommentGeneratorAPI(InterfaceCommentGeneratorAPI):

    async def get_comment_query(self, api_url: str, headers: dict, body: dict) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, headers=headers, json=body) as response:
                if response.status == 200:
                    try:
                        return await response.json()
                    except aiohttp.ContentTypeError:
                        text = await response.text()
                        raise Exception(f'JSON was expected, but a different content type came in: {text}')
                else:
                    error_message = await response.text()
                    raise Exception(f'Error {response.status}: {error_message}')
