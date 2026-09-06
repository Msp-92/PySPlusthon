from PySPlusthon import Client
from PySPlusthon.conditions import document, text, command, photo, video, animation
from PySPlusthon.objects import InlineKeyboard, InputMedia, Message, ReplyKeyboard, InlineKeyboardButton, CallbackQuery
from PySPlusthon.dispatcher import Dispatcher
from PySPlusthon.event_handlers import MessageHandler, CallbackQueryHandler
import config

print("PySPlusthon Test Suite")
print("=" * 40)

# Test 1: Client import and basic initialization
print("\n1. Testing Client import and initialization...")
try:
    bot = Client(config.TOKEN)
    print("   OK Client created successfully with bot token")
except Exception as e:
    print(f"   FAIL Client creation failed: {e}")

# Test 2: Conditions import and functionality
print("\n2. Testing Conditions...")
try:
    from PySPlusthon.conditions import document, text, command, photo, video, animation
    print("   OK All conditions imported successfully")
    
    # Test document condition
    class MockMessage:
        def __init__(self):
            self.document = None
            self.text = None
    
    msg = MockMessage()
    doc_cond = document(msg)
    print(f"   OK document condition works: {doc_cond}")
    
    # Test text condition
    msg.text = "Hello world"
    text_cond = text(msg)
    print(f"   OK text condition works: {text_cond}")
    
except Exception as e:
    print(f"   FAIL Conditions test failed: {e}")

# Test 3: Objects import
print("\n3. Testing Objects...")
try:
    from PySPlusthon.objects import (
        InlineKeyboard, InputMedia, Message, ReplyKeyboard,
        InlineKeyboardButton, CallbackQuery, User, Chat
    )
    print("   OK All objects imported successfully")
    
    # Test InlineKeyboard
    keyboard = InlineKeyboard()
    keyboard.add(InlineKeyboardButton("Button", callback_data="test"))
    print(f"   OK InlineKeyboard created: {len(keyboard.inline_keyboard)} buttons")
    
    # Test InputMedia
    media = InputMedia("photo", "test.jpg", "Caption")
    print(f"   OK InputMedia created: type={media.type}, media={media.media}")
    
except Exception as e:
    print(f"   FAIL Objects test failed: {e}")

# Test 4: Event handlers
print("\n4. Testing Event Handlers...")
try:
    from PySPlusthon.event_handlers import MessageHandler, CallbackQueryHandler
    print("   OK Event handlers imported successfully")
    
    # Test MessageHandler
    async def my_handler(client, message):
        pass
    
    handler = MessageHandler(my_handler)
    print(f"   OK MessageHandler created: {handler.__class__.__name__}")
    
    # Test CallbackQueryHandler
    async def cb_handler(client, callback_query):
        pass
    
    cb_handler_obj = CallbackQueryHandler(cb_handler)
    print(f"   OK CallbackQueryHandler created: {cb_handler_obj.__class__.__name__}")
    
except Exception as e:
    print(f"   FAIL Event handlers test failed: {e}")

# Test 5: Dispatcher
print("\n5. Testing Dispatcher...")
try:
    dispatcher = Dispatcher()
    print(f"   OK Dispatcher created successfully")
    print(f"   OK Dispatcher reasonable_async_workers: {dispatcher.reasonable_async_workers}")
    print(f"   OK Dispatcher reasonable_sync_workers: {dispatcher.reasonable_sync_workers}")
except Exception as e:
    print(f"   FAIL Dispatcher test failed: {e}")

# Test 6: Errors
print("\n6. Testing Errors...")
try:
    from PySPlusthon.errors import RPCError, TooManyRequestsError
    print("   OK Errors imported successfully")
    
    error = RPCError.create(400, "Bad Request", "test_service")
    print(f"   OK RPCError.create works: {error}")
    
    error2 = TooManyRequestsError(5, "Too many requests")
    print(f"   OK TooManyRequestsError works: {error2}")
    
except Exception as e:
    print(f"   FAIL Errors test failed: {e}")

print("\n" + "=" * 40)
print("Test Suite Complete")
print("=" * 40)