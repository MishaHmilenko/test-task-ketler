from abc import ABC

from src.interafaces.external_api_interfaces.api_comment_generator import InterfaceCommentGeneratorAPI


class InterfaceCommentGenerator(ABC):

    def __init__(self, api_generator: InterfaceCommentGeneratorAPI) -> None:
        self.api_generator = api_generator

    async def generation_comment(self, caption: str) -> str:
        ...



