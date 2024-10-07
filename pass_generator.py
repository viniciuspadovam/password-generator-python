import math
import keyboard, sys, os
from random import random
from time import sleep
from threading import Thread

password = ""
characterNumber = 0
charset = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%!@$"


def killScriptOnCtrlC():
    while True:
        if keyboard.is_pressed('ctrl+c'):
            os._exit(0)
            sys.exit()
            break                       


def verifyFileExists():
    return os.path.exists("./senhas.txt")


def getFileLines():
    with open("senhas.txt", "r") as f:
        return len(f.readlines())


def passNameInTxtFile():
    return input("Insira um nome para ser colocado junto a senha no arquivo de texto: ")


def generatePassword():
    global password
    password = ""
    for i in range(int(characterNumber)):
        password += charset[math.floor(random() * len(charset))]


Thread(target = killScriptOnCtrlC).start()

print("=============================== Gerador de senha ===============================")
print("Para interromper a aplicação a qualquer momento, basta pressionar 'Ctrl + C'.\n")
isCharacterNumberValid = False
while not isCharacterNumberValid:
    try:
        characterNumber = int(input("Digite a quantidade de caracetes que deseja em sua senha(até 20 caracteres): "))
        if characterNumber < 0:
            raise Exception("Valor inválido")
        elif characterNumber > 20:
            raise Exception("Valor inválido")
        isCharacterNumberValid = True
    except:
        print("Ops... Parece que você digitou um valor inválido, tente novamente.\n")
        isCharacterNumberValid = False

generatePassword()

remakePass = "Y"
while remakePass == "Y":
    try:
        print("\nSua senha é: " + password)
        remakePass = input("\n\nDeseja recriar a senha (y/N)? ").upper() or "N"
        if remakePass == "Y":
            generatePassword()
        elif remakePass == "N":
            fileLinesLenght = 0
            if verifyFileExists():
                fileLinesLenght = getFileLines()

            file = open("senhas.txt", "a")

            if fileLinesLenght > 0:
                file.write("\n" + passNameInTxtFile() + ": " + password)
            else:
                file.write(passNameInTxtFile() + ": " + password)

            print("\nEssa senha estará disponivel em um arquivo de texto criado neste mesmo diretório")
            print("Você pode copiar a senha deste pronpt e verifica novamente depois neste arquivo")
        else:
            raise Exception("Valor inválido")
    except:
        print("Ops... Parece que você digitou um valor inválido, tente novamente.\n")
        remakePass = "Y"

file.close()
sleep(5)
