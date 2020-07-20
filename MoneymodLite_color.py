#IMPORTS
from mcstatus import MinecraftServer
import colorama
#INITIALIZE
colorama.init()
server = MinecraftServer.lookup("2b2t.org")
#INIT Functions
def CheckerClean(a):
	try:
		status=server.status()
		if status.players.online>=50:
			Response = colorama.Fore.BLACK + colorama.Back.GREEN + f"Онлайн: {status.players.online} игроков. Рестарт вроде прошёл. Сервер ответил в {status.latency} ms"
		else:
			Response = colorama.Fore.BLACK + colorama.Back.YELLOW + f"Онлайн: {status.players.online} игроков. Рестарт вроде не прошёл. Сервер ответил в {status.latency} ms"
	except:
		Response = colorama.Fore.BLACK + colorama.Back.RED + "Ошибка"
	return Response
#Checker
print(" Moneymod Lite by BG")
while True:
	# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
	#Trying to check server
	CheckResponse = CheckerClean(1)
	print(CheckResponse)
	print(colorama.Style.RESET_ALL)
