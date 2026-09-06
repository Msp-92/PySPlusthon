from typing import Union, List

import PySPlusthon
from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str]
    ) -> List[ChatMember]:
        if self.is_userbot():
            result = await self.get_chat_members(chat_id)
            return [member for member in result.members if member.is_admin.value]

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("getChatAdministrators", locals())
