import PySPlusthon


class DeleteWebhook:

    async def delete_webhook(
            self: "PySPlusthon.Client"
    ) -> bool:
        return await self.auto_execute("deleteWebhook", locals())
