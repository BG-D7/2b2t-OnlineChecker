print("Money Mod lite by BG")
Framework_Ver = int(input("Framework edition: 1(provided by mcstatus and 2b2t), 2(provided by jewtrick.ml) "))
if (Framework_Ver == 1):
	import MoneymodLite_Framework as m
	while True:
		Resp = m.CheckerClean(1)
		print(Resp)
elif (Framework_Ver == 2):
	import JewMod_framework as j
	print("forked from ZimnyCat/jewtrick-client")
	while True:
		Resp = j.JewMod(1)
		print(Resp)
else:
	print("error")




