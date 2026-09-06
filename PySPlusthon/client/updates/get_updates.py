from typing import List

import PySPlusthon
from ...objects import Update


class GetUpdates:

    async def get_updates(
            self: "PySPlusthon.Client",
            offset: int = None,
            limit: int = None
    ) -> List[Update]:
        return await self.auto_execute("getUpdates", locals())
