import PySPlusthon


class AnswerCallbackQuery:

    async def answer_callback_query(
            self: "PySPlusthon.Client",
            callback_query_id: str,
            text: str,
            show_alert: bool = False
    ) -> bool:
        return await self.auto_execute("answerCallbackQuery", locals())
