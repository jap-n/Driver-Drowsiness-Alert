from playsound import playsound

def play_alarm(level):
    if level == "sedang":
        playsound("sounds/sedang.mp3")
    elif level == "berat":
        playsound("sounds/berat.mp3")
    elif level == "tertidur":
        playsound("sounds/tertidur.mp3")
    elif level == "eror":
        playsound("sounds/eror.mp3")
    elif level == "welcome":
        playsound("sounds/welcome.mp3")