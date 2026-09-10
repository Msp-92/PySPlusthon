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
            reply_to_message_id: int = None,
            parse_mode: str = None
    ) -> Message:
        photo = resolve_media(photo)
        filename = _extract_filename_media(photo)
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        if filename is not None:
            data["filename"] = filename
        return await self.auto_execute("sendPhoto", data)
