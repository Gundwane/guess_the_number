# -*- coding: utf-8 -*-

from random import randint

#Computadora adivina el número
def computer_guess():
    inf_limit = 1
    sup_limit = 100
    flag = False

    print("Intentaré adivinar el número en el que estás pensando, entonces. \n Piensa en un número del 1 al 100")
    print("Pulsa '-'(menos) si tu número es menor, '+'(mas) si tu número es mayor o '='(igual) si he adivinado tu número ")

    while flag == False:

        num = randint(inf_limit, sup_limit)

        respuesta = input("Tu número es "+str(num)+" ?")

        if respuesta == '-':
            sup_limit = num - 1
        elif respuesta == '+':
            inf_limit = num + 1
        elif respuesta == '=':
            flag = True
        else:
            print('Creo que ingresaste una respuesta inválida')
    else:
        print('Genial!')

#Usuario adivina el número
def user_guess():
    num = randint(1, 100)
    flag = False

    print("Pensaré en un número del 1 al 100. Tu intenta adivinar cuál es.")

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

keep_playing = True

print("Bienvenido!")

while keep_playing == True:

    user_response = input("Escribe 'yo' si quieres adivinar mi número. Sino, yo intentaré adivinar tu número ")

    if user_response.lower() == 'yo':
        user_guess()
    else:
        computer_guess()

    response = input("Quieres volver a jugar? (Responde Si o No, o Salir para bueno...salir)")

    if response.lower() == 'si':
        keep_playing = True
    elif response.lower() == 'no':
        keep_playing = False
    else:
        print("No reconozco tu respuesta : /")
        keep_playing = True

else:
    print("See ya!")

