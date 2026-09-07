from typing import Union
from copy import deepcopy

from . import Object
from PySPlusthon import objects


class InlineKeyboardButton(Object):

    def __init__(
            self,
            text: str = None,
            callback_data: str = None,
            url: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.callback_data: str = callback_data
        self.url: str = url

    def format(self, *args, **kwargs):
        button = deepcopy(self)
        if button.text:
            button.text = button.text.format(*args, **kwargs)
        if button.callback_data:
            button.callback_data = button.callback_data.format(*args, **kwargs)
        if button.url:
            button.url = button.url.format(*args, **kwargs)
        return button
