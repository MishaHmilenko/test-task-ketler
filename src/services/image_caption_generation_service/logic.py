from io import BytesIO

import aiohttp
import requests
from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor

from src.interafaces.service_interfaces.image_caption_generation import InterfaceImageCaptionGeneration


class ImageCaptionGenerationService(InterfaceImageCaptionGeneration):

    def __init__(self) -> None:
        self.processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
        self.model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')

    async def get_caption(self, image_url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                image = Image.open(BytesIO(await response.read()))
        inputs = self.processor(images=image, return_tensors='pt')
        caption = self.model.generate(**inputs)
        return self.processor.decode(caption[0], skip_special_tokens=True)
