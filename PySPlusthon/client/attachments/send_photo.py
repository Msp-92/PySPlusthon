from typing import Union, BinaryIO, Optional
import os

import PySPlusthon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


def _extract_filename_media(media) -> Optional[str]:
    if isinstance(media, InputMedia):
        return getattr(media.media, 'name', None) if hasattr(media.media, 'name') else None
    if isinstance(media, str):
        return os.path.basename(media)
    return None


class SendPhoto:

    async def send_photo(
            self: "PySPlusthon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        photo = resolve_media(photo)
        filename = _extract_filename_media(photo)

        if self.is_userbot():
            from ...proto import requests, structs, enums
            peer_id, peer_type = map(int, chat_id.split("|"))
            file = await self.upload_file(chat_id, photo, enums.SEND_TYPE_PHOTO)
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
                        ext=structs.DocumentEx(
                            document_ex_photo=structs.DocumentExPhoto(
                                w=100,
                                h=100
                            )
                        ),
                        caption=structs.TextMessage(text=caption)
                    )
                ),
                ex_peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                )
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        params = {"chat_id": chat_id, "photo": photo}
        if caption is not None:
            params["caption"] = caption
        if filename is not None:
            params["filename"] = filename
        return await self.auto_execute("sendPhoto", params)
