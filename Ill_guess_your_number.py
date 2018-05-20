# -*- coding: utf-8 -*-

from random import randint

def computer_guess():
    inf_limit = 0
    sup_limit = 100
    flag = False

    print("Intentaré adivinar el número en el que estás pensando, entonces...")
    print("Pulsa '-' si tu número es menor, '+' si tu número es mayor o '=' si he adivinado tu número ")

    while flag == False:

        num = randint(inf_limit, sup_limit)
        respuesta = input("Tu número es "+str(num)+" ?")

        if respuesta == '-':
            sup_limit = num
        elif respuesta == '+':
            inf_limit = num
        elif respuesta == '=':
            flag = True
        else:
            print('Creo que ingresaste una respuesta inválida')
    else:
        print('Genial!')

def user_guess():
    num = randint(0, 100)
    flag = False

    print("Adivina mi número, entonces...")

    while flag == False:
        try:
            user_number = int(input("Ingresa número "))

            if user_number < num:
                print("Mi número es mas alto")
            elif user_number > num:
                print("Mi número es mas bajo")
            else:
                print("Ese es mi número! :D")
                flag = True

        except ValueError:
            print("Debes ingresar un número")

user_response = input("Escribe 'yo' si quieres adivinar mi número. Sino, yo intentaré adivinar tu número ")

if user_response == 'yo':
    user_guess()
else:
    computer_guess()

