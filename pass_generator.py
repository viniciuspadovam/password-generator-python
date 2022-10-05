import math
import os
from random import random
from time import sleep

def verifyFileExists():
    return os.path.exists("./senhas.txt")

def getFileLines():
    with open("senhas.txt", "r") as f:
        return len(f.readlines())

def passNameInTxtFile():
    return input("Insira um nome para ser colocado junto a senha no arquivo de texto: ")

password = ""
characterNumber = 0
charset = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%!"

print("===== Gerador de senha =====")
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
        print("Ops... Parece que você digitou um valor invaálido, tente novamente.\n")
        isCharacterNumberValid = False

for i in range(int(characterNumber)):
    password += charset[math.floor(random() * len(charset))]

print("\nTua senha é: " + password)

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

file.close()
sleep(5)
