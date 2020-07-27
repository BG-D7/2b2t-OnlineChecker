import requests
requests_counter = 0

def JewMod(a): 
    while True:
        global requests_counter
        requests_counter = requests_counter + 1
        try:
            JewMod_int = int(requests.get("https://jewtrick.ml/server/jewtrickstatus.html").text)
            if JewMod_int == 2:
                JewMod_online = requests.get("https://jewtrick.ml/server/jew_online.html").text
                Resp = f"Рестарт прошёл!!! Онлайн 2b2t: {JewMod_online}. Попытка {requests_counter}."
            elif JewMod_int == 1:
                Resp = f"Рестарт вроде не прошёл. Попытка {requests_counter}." 
            elif JewMod_int == 0:
                Resp = f"2b2t не отвечает {requests_counter}."
        except:
            if requests.get("https://jewtrick.ml/server/jewtrickstatus.html").status_code == 200:
                Resp = f"Сервер jew trick получает онлайн 2b2t {requests_counter}."
            else:
                Resp = f"Сервер jew trick недоступен {requests_counter}."
        return Resp
