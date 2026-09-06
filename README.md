<p align="center">
  <img src="assets/PySPlusthon.png" alt="PySPlusthon" width="200">
</p>

# PySPlusthon
A Python library for interacting with the Soroush Plus Bot API (Splus).

## Quick Start
```python

from PySPlusthon import Client

bot = Client("YOUR_BOT_TOKEN")

@bot.on_message()
async def on_message(message):
    print(f"Received: {message.text}")

if __name__ == "__main__":
    bot.run()
```

## Key Features

- **Full Bot API Support**: Send messages, photos, videos, documents, audio, voice, stickers, locations, contacts, and more
- **Update Handling**: Polling and webhook support with `start_polling()` and `set_webhook()`
- **Conditional Handlers**: Message filters using conditions (`text`, `command`, `document`, `photo`, `video`, `voice`, and more)
- **Event Handlers**: Connect, disconnect, initialize, shutdown, edited messages, callback queries, errors, and custom events
- **Object Model**: Comprehensive `Object` base class with `wrap()`/`unwrap()` for API response parsing
- **Inline Keyboards & Keyboards**: `InlineKeyboard` and `ReplyKeyboard` with button formatting
- **Media Groups**: Send photo/video/audio groups
- **Referral Links**: Create referral links with `create_referral_link()`
- **User/Chat Methods**: `get_me()`, `get_chat()`, `get_chat_member()`, `get_chat_members_count()`, and more
- **Inline Inline Buttons & Keyboards**: Full reply markup support
- **Protobuf & Userbot Support**: Optional userbot mode with WebSocket integration
- **Error Handling**: Custom RPC error types (`BadRequestError`, `FloodError`, `ForbiddenError`, `NotFoundError`, `UnauthorizedError`, `InternalError`, `TooManyRequestsError`)

## Installing

```bash
pip install PySPlusthon
```

## Links
- [**PyPI**](https://pypi.org/project/PySPlusthon/)
- [**GitHub**](https://github.com/Msp-92/PySPlusthon)
- [**Splus News Channel**](https://splus.ir/PySPlusthon)
- [**PySPlusthon Developers Group**](https://splus.ir/PySPlusthonDevelopers)