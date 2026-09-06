import asyncio
from PySPlusthon import Client
from PySPlusthon.objects import User, Message, Chat
from PySPlusthon.conditions import text, command, equals, document, photo, video
from PySPlusthon.errors import RPCError
import config

bot = Client(config.TOKEN)

got = {}

@bot.on_message()
async def on_message(message):
    got["text"] = message.text

@bot.on_command("start")
async def on_start(message):
    got["command_start"] = True

@bot.on_message(text("Hello"))
async def on_hello(message):
    got["hello"] = True

@bot.on_edited_message()
async def on_edited(message):
    got["edited"] = True

user = User(id=1, first_name="Test")
chat = Chat(id=2, title="Chat")

# Test text condition
msg = Message(id=1, author=user, chat=chat, text="Hello world")
bot.dispatcher.dispatch_event(bot, msg)
asyncio.sleep(0.1)

# Test command condition
msg2 = Message(id=2, author=user, chat=chat, text="/start")

bot.dispatcher.dispatch_event(bot, msg2)
asyncio.sleep(0.1)

# Test RPCError import
err = RPCError.create(400, "Bad Request", "SendMessage")
got["rpc_error"] = str(err)

bot.shutdown()

print("Test results:", got)
assert got.get("text") == "Hello world", "Text condition failed"
assert got.get("command_start") is True, "Command handler failed"
assert got.get("hello") is True, "Text condition match failed"
assert "Bad Request" in got.get("rpc_error", ""), "RPCError creation failed"
print("All assertions passed!")


if __name__ == "__main__":
    bot.run()