import os

from dotenv import load_dotenv

from src.interafaces.external_api_interfaces.api_client import InterfaceAPIClient

load_dotenv()


class CommentGeneratorAPIClient(InterfaceAPIClient):

    def get_headers(self) -> dict:
        return {'Authorization': f'Bearer {os.getenv("COMMENT_GENERATOR_API_TOKEN")}'}

    def get_url(self, **kwargs) -> str:
        return 'https://api.textcortex.com/v1/texts/blogs'

    def get_body(self, **kwargs) -> dict:
        caption = kwargs.get('caption')

        if caption is None:
            raise ValueError('Parameter \'caption\' must be provided.')

        return {
            'context': 'string',
            'formality': 'default',
            'keywords': [
                'string'
            ],
            'max_tokens': 2048,
            'model': 'claude-3-haiku',
            'n': 1,
            'source_lang': 'en',
            'target_lang': 'en',
            'temperature': None,
            'title': f'Write a casual, user-like comment from a third person reacting to the description: {caption} The comment should feel natural, like something you\'d see on social media, relatable, and under 10 words. Just the comment, nothing else.'
        }