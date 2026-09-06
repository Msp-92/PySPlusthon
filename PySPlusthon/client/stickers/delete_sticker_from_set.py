import PySPlusthon


class DeleteStickerFromSet:

    async def delete_sticker_from_set(
            self: "PySPlusthon.Client",
            sticker: str
    ) -> bool:
        return await self.auto_execute("deleteStickerToSet", locals())
