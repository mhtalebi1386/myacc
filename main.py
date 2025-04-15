import datetime
from telethon import TelegramClient, events

api_id = 23088910
api_hash = '59294da203b25242ccc19c2fc6df7cfd'

client = TelegramClient('session_name', api_id, api_hash)
last_reply = {}

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    sender_id = sender.id
    sender_name = sender.username or sender.first_name or "there"
    now = datetime.datetime.now().date()

    if event.is_private or (event.message.mentioned and not event.is_channel):
        if last_reply.get(sender_id) != now:
            await event.reply(f"Hello {sender_name} 👋 This is an automated message. I will get back to you as soon as I'm available.")
            last_reply[sender_id] = now

client.start()
client.run_until_disconnected()
