import aiohttp
import asyncio

from src.interafaces.db_interfaces.repository import InterfaceRepository


class GoogleSheetTableAPI(InterfaceRepository):

    async def get_value(self, **kwargs: str) -> list[str]:
        url = kwargs.get('url')
        headers = kwargs.get('headers')

        async with aiohttp.ClientSession() as session:
            for attempt in range(5):
                try:
                    async with session.get(url, headers=headers) as response:
                        response.raise_for_status()
                        lines = (await response.json())['values']
                        return [cell for line in lines for cell in line]

                except aiohttp.ClientResponseError as e:
                    if e.status == 429:
                        wait_time = 2 ** attempt
                        print(f'Rate limit exceeded. Waiting for {wait_time} seconds before retrying.')
                        await asyncio.sleep(wait_time)
                    else:
                        raise

                except aiohttp.ClientError:
                    raise

    async def add_value(self, **kwargs: str) -> None:
        url = kwargs.get('url')
        headers = kwargs.get('headers')
        body = kwargs.get('body')

        async with aiohttp.ClientSession() as session:
            for attempt in range(5):
                try:
                    url += '?valueInputOption=USER_ENTERED'

                    async with session.put(url, json=body, headers=headers) as response:
                        response.raise_for_status()
                        return

                except aiohttp.ClientResponseError as e:
                    if e.status == 429:
                        wait_time = 2 ** attempt
                        print(f'Rate limit exceeded. Waiting for {wait_time} seconds before retrying.')
                        await asyncio.sleep(wait_time)
                    else:
                        raise

                except aiohttp.ClientError:
                    raise
