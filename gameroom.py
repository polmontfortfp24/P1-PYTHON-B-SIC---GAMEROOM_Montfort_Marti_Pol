import random
import time

PararJuego = True

# Funcions Penjat
def obtPalabraRandom():
    palabras = [
        'python', 'programacion', 'ahorcado', 'desarrollo', 'codigo',
        'óbito', 'aurora', 'columbra', 'rauco', 'quiescente',
        'efímero', 'lúgubre', 'perenne', 'sempiterno', 'fugaz',
        'inmarcesible', 'inefable', 'onírico', 'pletórico', 'sibilino',
        'taciturno', 'ubiquitario', 'volátil', 'yermo', 'zozobra'
    ]
    return random.choice(palabras)
def imprimir(palabra, letrasAdivinadas):
    tablero = ''
    for letra in palabra:
        if letra in letrasAdivinadas:
            tablero += letra + ' '
        else:
            tablero += '_ '
    print(tablero)
def ahorcado():
    palabra = obtPalabraRandom()
    letrasAdivinadas = []
    intentos = 6
    print("¡Bienvenido a     juego del ahorcado!")
    while intentos > 0:
        imprimir(palabra, letrasAdivinadas)
        letra = input("Adivina una letra: ").lower()
        if letra in letrasAdivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif letra in palabra:
            letrasAdivinadas.append(letra)
            print("¡Bien hecho! Has adivinado una letra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
        if all(letra in letrasAdivinadas for letra in palabra):
            print("")
            print(f"¡Felicidades! Has adivinado la palabra '{palabra}'.")
            time.sleep(4)
            break
    else:
        print(f"Lo siento, has perdido. La palabra era '{palabra}'.")
        
# Funcions Numero

def adivinaNum():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")
    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            time.sleep(3)
            break
        
def piedraPapelTijera():
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)
    
    print(f"Tú elegiste: {usuario}") 
    print(f"La computadora eligió: {computadora}")
    
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    time.sleep(3)



#Joc en si

while PararJuego:
    print(" ")
    print(" ")
    print("Bienvenido a game room!")
    print("Qué quieres a hacer?")
    print("1. Jugar a adivinar el numero")
    print("2. Jugar al piedra, papel o tijera")
    print("3. Jugar al ahorcado")
    print("4. Salir")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Has seleccionado jugar al numero")
        print("------------------------------------")
        adivinaNum()
    elif choice == "2":
        print("Has seleccionado Piedra Papel Tijera")
        print("------------------------------------")
        piedraPapelTijera()
    elif choice == "3":
        print("Has seleccionado jugar al Ahorcado")
        print("------------------------------------")
        ahorcado()
    elif choice == "4":
        print("Hasta luego")
        PararJuego = True
    else:    
        print("Opción incorrecta")


