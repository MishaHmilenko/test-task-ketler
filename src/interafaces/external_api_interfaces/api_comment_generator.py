from abc import ABC, abstractmethod

from aiohttp import ClientResponse


class InterfaceCommentGeneratorAPI(ABC):

    @abstractmethod
    async def get_comment_query(self, api_url: str, headers: dict, body: dict) -> dict:
        ...
