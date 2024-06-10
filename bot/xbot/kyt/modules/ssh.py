from kyt import *

#DELETESSH
@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("Username To Be Deleted:")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
			cmd = f'printf "%s\n" "{user}" | bot-delssh'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"User `{user}` Not Found")
		else:
			await event.respond(f"Successfully Deleted `{user}`")
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('Username:')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("Password:")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("Choose Expiry Day",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 3 Day ","3")],
[Button.inline(" 7 Day ","7"),
Button.inline(" 15 Day ","15")],
[Button.inline(" 22 Day ","22"),
Button.inline(" 30 Day ","30")],
[Button.inline(" 60 Day ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(3)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("User Already Exist")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
━━━━━━━━━━━━━━━━━
🟢 SSH ACCOUNT 🟢
━━━━━━━━━━━━━━━━━
» Username         : `{user.strip()}`
» Password         : `{pw.strip()}`
━━━━━━━━━━━━━━━━━
» Host             : `{DOMAIN}`
» Host Slowdns     : `{HOST}`
» Pub Key          : `{PUB}`
» Port OpenSSH     : `443, 80, 22`
» Port DNS         : `443, 53 ,22`
» Port Dropbear    : `443, 109`
» Port Dropbear WS : `443, 109`
» Port SSH WS      : `80, 8080, 8081-9999 `
» Port SSH SSL WS  : `443`
» Port SSL/TLS     : `222-1000`
» Port OVPN WS SSL : `443`
» Port OVPN SSL    : `443`
» Port OVPN TCP    : `443, 1194`
» Port OVPN UDP    : `2200`
» Proxy Squid      : `3128`
» BadVPN UDP       : `7100, 7300, 7300`
━━━━━━━━━━━━━━━━━
» Payload WSS      : `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
━━━━━━━━━━━━━━━━━
» OpenVPN WS SSL   : `https://{DOMAIN}:81/ws-ssl.ovpn`
» OpenVPN SSL      : `https://{DOMAIN}:81/ssl.ovpn`
» OpenVPN TCP      : `https://{DOMAIN}:81/tcp.ovpn`
» OpenVPN UDP      : `https://{DOMAIN}:81/udp.ovpn`
━━━━━━━━━━━━━━━━━
» Save Link Account: `https://{DOMAIN}:81/ssh-{user.strip()}.txt`
» Expired Until: `{later}`

"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'show-ssh'))
async def show_ssh(event):[Button.inline(" 3 Day ","3"),
	async def show_ssh_(event):
		cmd = 'bot-member-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""
```
{z}
```
Show All SSH User

""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await show_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		cmd = 'bot-cek-login-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

shows logged in users SSH Ovpn
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline(" CREATE SSH ","create-ssh"),
Button.inline(" DELETE SSH ","delete-ssh")],
[Button.inline(" SHOW All USER SSH ","show-ssh"),
Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
🇮🇩 ARI VPN STORE 🇮🇩
━━━━━━━━━━━━━━━━━━━━━━━ 
━━━━━━━━━━━━━━━━━━━━━━━ 
 ⚠️ MENU SSH & OVPN ⚠️
━━━━━━━━━━━━━━━━━━━━━━━ 
🟢 » Service: `SSH OVPN`
🟢 » Hostname/IP: `{DOMAIN}`
🟢 » ISP: `{z["isp"]}`
🟢 » Country: `{z["country"]}`
🇮🇩 » @ARI_VPN_STORE
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
