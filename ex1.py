# Antonio Tian 1 DAM presencial
import random
# variables
continuar = True
partida = 0
partidaGanadas = 0
intentomin = 999999
intentomax = 0
intentosTotal = 0
# bucle para el juego
while continuar:
    # entrada de datos
    intentos = int(input("En cuantos intentos crees que lo adivinarias: "))
# variables
    partida = partida + 1
    numeroRandom = random.randint(1, 100)
    numeroIntentos = 0
    acertado = False
    noAcertado = False
    intentoGanados = 0
    valormax = 100
    valormin = 1
# prueba del número random
    print(numeroRandom)
# control del número introducido
    while True:
        # control de intentos
        numeroIntentos = numeroIntentos + 1
        numero = int(input("Dime un número de 1-100: "))
        while numero > 100 or numero <= 0:
            numero = int(
                input("¿Éstas tonto? DIme un número de 1 - 100: "))
#
        if numero == numeroRandom:
            acertado = True
            partidaGanadas = partidaGanadas + 1
            intentoGanados = intentoGanados + numeroIntentos
            break
# ayuda para adivinar el número
        if numero > numeroRandom:
            if numero <= valormax:
                valormax = numero
                valormax = valormax - 1
            print(f"No, es menor. Está entre {valormin} y {valormax}")
        elif numero < numeroRandom:
            if numero >= valormin:
                valormin = numero
                valormin = valormin + 1
            print(f"No, es mayor. Está entre {valormin} y {valormax}")
        intentosTotal = intentosTotal + numeroIntentos
# control de intentos
        if numeroIntentos == intentos:
            noAcertado = True
            break
# control de acertado
    if acertado:
        print(
            f"Enora buena has acertado el número con {numeroIntentos} intentos")
        if numeroIntentos < intentomin:
            intentomin = numeroIntentos
        elif intentomax < numeroIntentos:
            intentomax = numeroIntentos
    elif noAcertado:
        print(
            "Has superado el número de intentos y no lo has encertado. El número era el", numeroRandom)
# Resctrinccion de repetir
    x = str(input(
        "¿Quieres jugar otra partida? Pulsar s o S para continuar u otra para salir de programa: "))
    if x == "S" or x == "s":
        continuar = True
    else:
        break
# salida de datos
print(f"Has jugado {partida} partida")
# condición si no ha ganado ningúna partida
if partidaGanadas == 0:
    print("No has ganado ningúna partida tu media es 0")
elif partidaGanadas == 1:
    print("Premio")
    print("Solo has jugado una partida y lo has ganado")
else:
    # salida de datos
    print("Premio" * partidaGanadas)
    mediaDeIntentos = intentosTotal / partidaGanadas
    print(f"La media de intentos en partidas ganadas son {mediaDeIntentos}")
    print(f"Has ganado con {intentomin} de intentos en tu mejor partida")
    print(f"Has ganado con {intentomax} de intentos en tu peor partida")
