from pynput import keyboard

from time import sleep
import os
import json

keyboard = Controller ()

def main ():
    iniciar()
    contagemInicial()
    
    jogar("teste01.json")
    
    print ("Pronto")
    
def iniciar ():
    pass

def contagemInicial ():
    print ("Starting", end = "")
    for i in range (0, 10):
        print (".", end = "")
        sleep(1)

def jogar (nome):
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(
        script_dir,
        "arquivos",
        nome
    )
    with open(filepath, "r") as jsonfile:
        dados = json.load(jsonfile)
        
        for index, tecla in enumerate(dados):
            if tecla ["tecla"] == "Key.esc":
                break
            elif tecla ["tipo"] == "keyDown":
                keyboard.press(tecla["tecla"])
            elif tecla ["tipo"] == "keyUp":
                keyboard.release(tecla ["tecla"])
            try:
                proximaTecla = dados [index + 1]
            except IndexError:
                break
            tempoPassado = proximaTecla ["tempo"] - tecla ["tempo"]
            if tempoPassado >= 0:
                sleep(tempoPassado)
            else:
                raise Exception("ERRO")

if __name__ == "__main__":
    main()
    ##  pedro