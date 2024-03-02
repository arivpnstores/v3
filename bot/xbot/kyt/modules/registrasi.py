from kyt import *

@bot.on(events.CallbackQuery(data=b'registrasi'))
async def ganti_ip(event):
    async def ganti_ip_(event):
        chat = event.chat_id  # Definisikan variabel chat di sini
        async with bot.conversation(chat) as user_conv:
            await event.respond('Username:')
            user = await user_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = user.raw_text.strip()

        async with bot.conversation(chat) as pw_conv:
            await event.respond("ipvps:")
            pw = await pw_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = pw.raw_text.strip()
            
        async with bot.conversation(chat) as day_conv:
            await event.respond("Berpa day:")
            day = await day_conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            day = day.raw_text.strip()
            
        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(1)
        await event.edit("`Processing Daftar IPVPS`")
        time.sleep(1)
        await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 36%\n████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
        time.sleep(1)
        await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
        time.sleep(0)
        await event.edit("`Processing... 100%\n█████████████████████████ `")
        time.sleep(1)
        await event.edit("`Wait.. Setting up an Account`")

        cmd = f'printf "%s\n" "{pw}" "{user}" "{day}" |  bash /root/usr/bin/add-ipvps'
        try:
            subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🍀VPS SUCCESSFULLY REGISTER🍀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌹NAME AUTHOR : {user}
🏵️SCRIPT TIME : {day} day
🌺IP SERVER   : {pw}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            await event.respond(msg)
        except subprocess.CalledProcessError as e:
            await event.respond(f"Error: {e.output}")

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await ganti_ip_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)
