from typing import Union

import PySPlusthon


class AskReview:

    async def ask_review(
            self: "PySPlusthon.Client",
            user_id: Union[int, str],
            delay_seconds: int = 0
    ) -> bool:
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("askReview", locals())
