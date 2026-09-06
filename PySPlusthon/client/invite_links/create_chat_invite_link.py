from typing import Union

import PySPlusthon
from ...objects import InviteLink


class CreateChatInviteLink:

    async def create_chat_invite_link(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str]
    ) -> InviteLink:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("createChatInviteLink", locals())
