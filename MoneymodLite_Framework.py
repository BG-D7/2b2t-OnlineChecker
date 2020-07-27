#IMPORTS
from mcstatus import MinecraftServer
#INITIALIZE
server = MinecraftServer.lookup("2b2t.org")
#INIT Functions
def CheckerClean(a):
	try:
		status=server.status()
		if status.players.online>=75:
			Response = f"Онлайн: {status.players.online} игроков. Рестарт вроде прошёл. Сервер ответил в {status.latency} ms"
		else:
			Response = f"Онлайн: {status.players.online} игроков. Рестарт вроде не прошёл. Сервер ответил в {status.latency} ms"
	except:
		Response = "Ошибка"
	return Response
print("Money Mod lite by BG")

	

