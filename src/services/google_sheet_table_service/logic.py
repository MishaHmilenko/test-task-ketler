import asyncio
import string

from src.interafaces.db_interfaces.repository import InterfaceRepository
from src.interafaces.external_api_interfaces.api_client import InterfaceAPIClient
from src.interafaces.service_interfaces.table import InterfaceTable


class GoogleSheetTableService(InterfaceTable):

    def __init__(self, table_repo: InterfaceRepository, api_client: InterfaceAPIClient):
        super().__init__(table_repo)
        self.api_client = api_client

    def column_number_to_letter(sel, n: int) -> str:
        result = []
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            result.append(string.ascii_uppercase[remainder])
        return ''.join(reversed(result))

    async def get_letter_by_column_name(self, column_name: str) -> str:
        columns = await self.table_repo.get_value(
            url=self.api_client.get_url(
                range_name=f'A1:1'
            ),
            headers=self.api_client.get_headers()
        )
        index_of_cell = columns.index(column_name) + 1
        return self.column_number_to_letter(index_of_cell)

    async def get_index_by_username(self, username: str) -> str:

        letter_of_cell = await self.get_letter_by_column_name(column_name='username')
        list_of_usernames = await self.table_repo.get_value(
            url=self.api_client.get_url(
                range_name=f'{letter_of_cell}:{letter_of_cell}'
            ),
            headers=self.api_client.get_headers()
        )

        return str(list_of_usernames.index(username) + 1)

    async def get_free_index_for_username(self) -> str:

        letter = await self.get_letter_by_column_name(column_name='username')
        list_of_usernames = await self.table_repo.get_value(
            url=self.api_client.get_url(
                range_name=f'{letter}:{letter}'
            ),
            headers=self.api_client.get_headers()
        )

        return str(len(list_of_usernames) + 1)

    async def check_value_in_table(self, value: str, column_name: str) -> bool:

        letter = await self.get_letter_by_column_name(column_name=column_name)
        values_of_range = await self.table_repo.get_value(
            url=self.api_client.get_url(
                range_name=f'{letter}:{letter}'
            ),
            headers=self.api_client.get_headers()
        )

        return value in values_of_range

    async def add_username_to_table(self, username: str) -> None:
        if not await self.check_value_in_table(value=username, column_name='username'):
            letter_of_cell = await self.get_letter_by_column_name(column_name='username')
            index_of_cell = await self.get_free_index_for_username()

            await self.table_repo.add_value(
                url=self.api_client.get_url(
                    range_name=f'{letter_of_cell}{index_of_cell}'
                ),
                headers=self.api_client.get_headers(),
                body=self.api_client.get_body(
                    range_name=f'{letter_of_cell}{index_of_cell}',
                    values=username,
                )
            )

    async def add_record_to_table(self, values: str | list[str], **kwargs) -> None:
        column_name = kwargs.get('column_name')

        letter_of_cell = await self.get_letter_by_column_name(column_name=column_name)

        if column_name == 'username':
            await self.add_username_to_table(username=values)
            return

        username = kwargs.get('username')

        index_of_cell = await self.get_index_by_username(username)
        await self.table_repo.add_value(
            url=self.api_client.get_url(
                range_name=f'{letter_of_cell}{index_of_cell}'
            ),
            headers=self.api_client.get_headers(),
            body=self.api_client.get_body(
                range_name=f'{letter_of_cell}{index_of_cell}',
                values=values,
            )
        )
