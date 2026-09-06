from typing import Union

import PySPlusthon


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str]
    ) -> int:
        if self.is_userbot():
            from PySPlusthon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            response = await self.execute(requests.GetGroupMembersCount(
                group=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
            ))
            return response.members_count
        
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("getChatMembersCount", locals())
