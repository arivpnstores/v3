from kyt import *

@bot.on(events.CallbackQuery(data=b'domain'))
async def perpanjang(event):
    async def perpanjang_(event):
        chat = event.chat_id  # Ambil ID obrolan dari objek event
        async with bot.conversation(chat) as user:
            await event.respond('Username:')
            user = user.wait_event(events.NewMessage(incoming=True))
            user = (await user).raw_text
        async with bot.conversation(chat) as pw:
            await event.respond("Input IP VPS:")
            pw = pw.wait_event(events.NewMessage(incoming=True))
            pw = (await pw).raw_text
        async with bot.conversation(chat) as exp:
            await event.respond("Pilih Domain Nya", buttons=[
                [Button.inline(" sgpremium.my.id ", "1"),
                 Button.inline(" idpremium.my.id ", "2")]
            ])
            exp = exp.wait_event(events.CallbackQuery)
            exp = (await exp).data.decode("ascii")
        cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" | domain'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except Exception as e:
            await event.respond(f"Error: {e}")
        else:
            msg = f"""```{a}```
» @ARI_VPN_STORE"""
            await event.respond(msg)

    # Tidak perlu pengecekan validitas, langsung jalankan fungsi
    await perpanjang_(event)
