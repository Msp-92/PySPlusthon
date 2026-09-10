from typing import Union, BinaryIO, Optional
import os

import PySPlusthon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


def _extract_filename(document) -> Optional[str]:
    if isinstance(document, InputMedia):
        return getattr(document.media, 'name', None) if hasattr(document.media, 'name') else None
    if isinstance(document, str):
        return os.path.basename(document)
    if document is not None:
        return getattr(document, 'name', None)
    return None


class SendDocument:

    async def send_document(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str],
            document: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None,
            parse_mode: str = None
    ) -> Message:
        document = resolve_media(document)
        filename = _extract_filename(document)

        if self.is_userbot():
            from ...proto import requests, structs, enums
            peer_id, peer_type = map(int, chat_id.split("|"))
            file = await self.upload_file(chat_id, document, enums.SEND_TYPE_DOCUMENT)
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                ),
                rid=self.ws_connection.create_rid(),
                message=structs.Message(
                    document_message=structs.DocumentMessage(
                        file_id=file.id,
                        access_hash=peer_id,
                        file_size=file.size,
                        name=file.name,
                        mime_type=file.mime_type,
                        caption=structs.TextMessage(text=caption)
                    )
                ),
                ex_peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                )
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        params = {"chat_id": chat_id, "document": document}
        if caption is not None:
            params["caption"] = caption
        if filename is not None:
            params["filename"] = filename
        return await self.auto_execute("sendDocument", params)
