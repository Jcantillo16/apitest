import os
import time
from prettytable import PrettyTable


# Funciones

def text_to_ascii():
    try:
        print("Texto a ASCII")
        print("Ingresa el texto")
        ascii = []
        text = input()
        for i in text:
            ascii.append(ord(i))
        ascii2 = ".".join(str(i) for i in ascii)
        print(ascii2)
        ascii_table(text)
        time.sleep(2)
        clear()
    except ValueError:
        print('Error al convertir el texto')


def ascii_to_text():
    try:
        print("ASCII a texto")
        print("Ingresa el texto en ASCII")
        ascii3 = []
        ascii = input()
        ascii2 = ascii.split(".")
        for i in ascii2:
            ascii3.append(chr(int(i)))
        ascii4 = "".join(ascii3)
        print(ascii4)
        ascii_table(ascii4)
        time.sleep(2)
        clear()
    except ValueError:
        print('Error al convertir el texto')


def menu():
    try:
        print("1. Conversión de texto a ASCII.")
        print("2. ASCII a texto")
        print("3. Salir")
        option = int(input())
        if option == 1:
            text_to_ascii()
        elif option == 2:
            ascii_to_text()
        elif option == 3:
            exit()
        else:
            print("Opción inválida")
            time.sleep(3)
            clear()
            menu()
    except ValueError:
        print("Opción inválida")
        clear()
        menu()


def clear():
    try:
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
            os.system('cls')
    except:
        print("Error al limpiar pantalla")
        time.sleep(3)
        exit()


def ascii_table(cadena):
    table = PrettyTable()
    table.field_names = ["Letra", "ASCII"]
    for i in cadena:
        table.add_row([i, ord(i)])
    print(table)


# Main
menu()
