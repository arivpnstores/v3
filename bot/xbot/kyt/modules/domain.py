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
                [Button.inline(" mypremium.biz.id ", "1"),
                 Button.inline(" klmpk.me ", "2")],
                [Button.inline(" klmpk.my.id ", "3"),
                Button.inline(" vipme.my.id ", "4")],
                [Button.inline(" klmpk-tunneling.my.id ", "5"),
                Button.inline(" vpn-store.my.id ", "6")],
                [Button.inline(" klmpk.cfd ", "7"),
                 Button.inline(" server-tunneling.tech ", "8")]
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
» 🤖@LunaticTunnel"""
            await event.respond(msg)

    # Tidak perlu pengecekan validitas, langsung jalankan fungsi
    await perpanjang_(event)
