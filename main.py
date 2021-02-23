from data import *
from funciones import *
from settings import *

win_condition = set_dificulty(win_condition, "ganar")
lose_condition = set_dificulty(lose_condition, "perder")

while len(mesa.keys()) < win_condition and fails < lose_condition:

    # esto es el turno 1 donde se saca la carta inicial
    if len(mesa.keys()) == 0:
        carta = get_random_card(mazo_inventos)
        nombre = carta[0]
        fecha = carta[1]
        print("La primera carta es:", nombre, "y fecha del", convert_date(fecha) + '.')
        mesa[nombre] = fecha

    print("==================================")
    print("Cartas en mesa:", str(len(mesa.keys())))
    print("Win condition:", str(win_condition))
    print("Fallos actuales:", str(fails))
    print("Fallos para perder:", str(lose_condition))

    print("")
    print("Hora de sacar una nueva carta...\n")
    carta = get_random_card(mazo_inventos)
    nombre = carta[0]
    fecha = carta[1]
    print("La carta nueva es: " + nombre + ". Intente adivinar su posición en la Timeline...")

    print("")
    print("Cartas en mesa:")
    print_mesa(mesa)
    print("")

    i = 0
    while i < 1 or i > len(mesa)+1:
        try:
            i = int(input("¿Dónde crees que va?\n"))
        except:
            pass

    i -= 2
    if get_position(i, fecha, mesa):
        print("¡Bien hecho!")
        mesa[nombre] = fecha
        mesa = sort_dict(mesa)

    else:
        fecha = convert_date(fecha)
        print("Error. " + nombre + ' es del ' + fecha)
        fails += 1

if fails == lose_condition:
    print("Has perdido :(")

else:
    print("¡Ganaste, felicidades!")