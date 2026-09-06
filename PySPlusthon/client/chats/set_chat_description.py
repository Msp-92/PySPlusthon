from typing import Union

import PySPlusthon


class SetChatDescription:

    async def set_chat_description(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str],
            description: str
    ) -> bool:
        if self.is_userbot():
            from PySPlusthon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.execute(requests.EditGroupAbout(
                group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                rid=self.ws_connection.create_rid(),
                about=description
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatDescription", locals())
