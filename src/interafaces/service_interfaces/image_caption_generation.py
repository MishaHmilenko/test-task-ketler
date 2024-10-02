from abc import ABC, abstractmethod


class InterfaceImageCaptionGeneration(ABC):

    @abstractmethod
    async def get_caption(self, image_url: str) -> str:
        ...
