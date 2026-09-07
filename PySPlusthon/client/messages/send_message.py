from typing import Union

import PySPlusthon
from ...objects import Message
from PySPlusthon import objects


class SendMessage:

    async def send_message(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str],
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None,
            parse_mode:str=None
    ) -> Message:
        if self.is_userbot():
            from PySPlusthon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    text_message=structs.TextMessage(
                        text=text
                    )
                ),
                ex_peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                )
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("sendMessage", locals())
