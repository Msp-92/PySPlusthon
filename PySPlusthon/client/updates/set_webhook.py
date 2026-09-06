import PySPlusthon


class SetWebhook:

    async def set_webhook(
            self: "PySPlusthon.Client",
            url: str
    ) -> bool:
        return await self.auto_execute("setWebhook", locals())
