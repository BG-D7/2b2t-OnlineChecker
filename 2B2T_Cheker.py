#IMPORTS
from mcstatus import MinecraftServer
import colorama
import time
#INITIALIZE
colorama.init()
server = MinecraftServer.lookup("2b2t.org")
#Checker
print("2b2t online check by BG")
while True:
	# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
	#Trying to check server
	try:
		status = server.status()
		print(colorama.Fore.BLACK + colorama.Back.GREEN + "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
	except:
		print(colorama.Fore.BLACK + colorama.Back.RED + "Сервер не отвечает")
	#Reset Style
	print(colorama.Style.RESET_ALL)
