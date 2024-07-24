from pynput import keyboard
from time import time
import json
import os

comecarTimer = None

teclaSeguradas = []
guardar = []
arquivar = []

NOME_ARQUIVO = "teste01"


def main():
    ouvinte()
    print("Duração da Gravação: {} segundos".format(tempoPassado()))
    global guardar
    print(json.dumps(guardar))

    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(
        script_dir,
        "arquivos",
        "{}.json".format(NOME_ARQUIVO)
    )
    with open(filepath, "w") as outfile:
        json.dump(guardar, outfile, indent = 4)

class EventType ():
    KEYDOWN = "keyDown"
    KEYUP = "keyUp"


def tempoPassado():
    global comecarTimer
    return time() - comecarTimer


def guardarInput(tipo, tempo, tecla):
    global guardar
    guardar.append({
        "tempo": tempo,
        "tipo": tipo,
        "tecla":str(tecla)
    })


def on_press(key):
    global teclaSeguradas
    if key in teclaSeguradas:
        return
    else:
        teclaSeguradas.append(key)

    try:
        guardarInput(EventType.KEYDOWN, tempoPassado(), key.char)
    except AttributeError:
        guardarInput(EventType.KEYDOWN, tempoPassado(), key)


def on_release(key):
    global teclaSeguradas

    try:
        teclaSeguradas.remove(key)
    except ValueError:
        print("ERRO {} não está na lista".format(key))

    try:
        guardarInput(EventType.KEYUP, tempoPassado(), key.char)
    except AttributeError:
        guardarInput(EventType.KEYUP, tempoPassado(), key)
    if key == keyboard.Key.esc:
        # parar de checar
        return False


def ouvinte():
    # coletar inputs do teclato até soltar
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as checador:
        global comecarTimer
        comecarTimer = time()
        checador.join()


if __name__ == "__main__":
    main()


"""
pedro caue correa santos
"""
