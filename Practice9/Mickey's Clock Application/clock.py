import datetime

def get_angles():
    now = datetime.datetime.now()
    
    # секунды
    sec = now.second
    # минуты + чуть-чуть секунд для плавности
    minute = now.minute + sec / 60

    # формула (12 часов = 90 градусов)
    sec_angle = 90 - (sec * 6)
    min_angle = 90 - (minute * 6)

    return min_angle, sec_angle