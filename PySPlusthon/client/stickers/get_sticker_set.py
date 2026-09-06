import PySPlusthon
from ...objects import StickerSet


class GetStickerSet:

    async def get_sticker_set(
            self: "PySPlusthon.Client",
            name: str
    ) -> StickerSet:
        return await self.auto_execute("getStickerSet", locals())
