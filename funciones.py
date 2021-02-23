import random

# input: un integer que será el win_condition o el lose_condition (encontrados en settings.py)
# return: retorna int_condition para modificar el win/lose condition
# lo que hace la función es un personalizador de dificultad, si el jugador quiere un reto mayor al estándar
# o menor esta es la función para ello
def set_dificulty(int_condition, condicion):
    print("¿Quiere cambiar la condición de " + condicion + "? Actualmente para " + condicion +
          " necesitas " + str(int_condition) + ".")
    respuesta = "ajks"
    while respuesta not in ["y", "n"]:
        respuesta = input("[y, n]\n")
    if respuesta == "y":
        done = False
        while not done:
            try:
                int_condition = int(input("Pon el número de aciertos para ganar:\n"))
                done = True
            except:
                pass
    return int_condition


# input: un diccionario que es el mazo de cartas
# return: expulsa una tupla que es una carta
# lo que hace esta funcion es escoger una carta aleatoria del mazo y la devuelve,
# antes de acabar la función esa carta es eliminada del mazo para que no vuelva a salir en el futuro
def get_random_card(mazo):
    nombre = random.choice(list(mazo.keys()))
    fecha = mazo[nombre]
    mazo.pop(nombre)
    return (nombre, fecha)


# input: un diccionario que son las cartas en mesa
# return: - (es una función tipo void)
# esta función se encarga de hacer print de forma bonita de las cartas que hay en mesa
def print_mesa(mazo):
    i = 0
    j = 1
    while i < len(list(mazo.keys())):
        if j == 1:
            print(str(j) + ') ' + "Antes de ", end="")
            print(list(mazo.keys())[i] + " (", end="")
            date = convert_date(mazo[list(mazo.keys())[i]])
            print(str(date) + ')')
        else:
            print(str(j) + ') ' + "Después de ", end="")
            print(list(mazo.keys())[i] + " (", end="")
            date = convert_date(mazo[list(mazo.keys())[i]])
            print(str(date) + ')')
            i += 1
        j += 1

# input: i es un int que es la posición donde creemos que va, fecha es la fecha de creación del objeto que queremos adivinar (un int)
# mazo son las cartas de la mesa (un diccionario)
# return: retorna un bool, true si acertamos, false si fallamos nuestra predicción
# es una función que indica si el jugador acierta o falla su prediccón de fecha
def get_position(i, fecha, mazo):
    list_dates = []
    for elemento in mazo:
        list_dates.append(mazo[elemento])
    if i == -1:
        if list_dates[0] >= fecha:
            return True
    elif i < len(list_dates) - 1:
        if list_dates[i] <= fecha and fecha <= list_dates[i+1]:
            return True
    else:
        if list_dates[i] <= fecha:
            return True
    return False

# input: un diccionario
# return: un diccionario
# el diccionario que entra como input sale como return ordenado por valor
def sort_dict(mesa):
    sorted_dict = {}
    sorted_keys = sorted(mesa, key=mesa.get)

    for w in sorted_keys:
        sorted_dict[w] = mesa[w]

    return sorted_dict

# input: recibe una fecha (interger)
# return: una fecha (string)
# esta función convierte una fecha negativa (-10000) por 10000 A.C.
def convert_date(date):
    if int(date) < 0:
        fecha = str(date)
        date = fecha.replace("-", "")
        date += " A.C."
    return date