from pyrogram import Client, filters, emoji
from dotenv import load_dotenv
import os
import json

def configure():
    load_dotenv()

app = Client(
    "my_account",
    app_version="1.3.0",
    device_model="PC",
    system_version="Mac",
    lang_code="it",
    api_id=os.getenv('api_id'), 
    api_hash=os.getenv('api_hash'),
    bot_token=os.getenv('bot_token')
)

MESSAGE = "{} Ciao {}, benvenutƏ nel gruppo ufficiale del MUG. Trovi il link per il telegraph con tutti i link ai gruppi qui: https://telegra.ph/Telegraph-MUG-11-08"

@app.on_message(filters.text)
async def command(client, message):

    ## LOGS ##
    if message.text.startswith('/'):
        print(message.chat.username, "IN", message.chat.id,"\ntext:", message.text)

        ## COMMAND ##
        if message.text == "/start" or message.text == "/start@MugBot":
            await message.reply("Grazie per avermi aggiunto a questo canale, per ulteriori informazioni scrivi in privato a @Ex_Noise", quote=False)

        if message.text == "/telegraph" or message.text == "/telegraph@MugBot":
            await message.reply("Il link del telegraph è: https://telegra.ph/Telegraph-MUG-11-08", quote=False)

    
        #elif message.text.startswith("/momentosbura") or message.text.startswith("/momentosbura@NonFunonziaBot")or message.text.startswith("/momentosburra") or message.text.startswith("/momentosburra@NonFunonziaBot"):
        #    await message.reply("ATT-T-T-T-ENTƏ ALLA SBURA", quote=False)
    
        # comando di prova da non aggiungere ai comandi base e che serve per vedere se il bot è online o pure no
        elif message.text.startswith("/prova") or message.text.startswith("/prova@MugBot"):
            await message.reply("ON", quote=False)
            


@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    if(message.new_chat_members[0].username=="MugBot"):
       await message.reply("Grazie per avermi aggiunto a questo canale, per ulteriori informazioni scrivi in privato a @Ex_Noise, template preso da @zAiro12")
    else:
        new_members = [u.mention for u in message.new_chat_members]
        text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
        await message.reply_text(text, disable_web_page_preview=True)

print("ONLINE")
app.run()