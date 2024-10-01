PararJuego = True
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
        print("Empezamos el juego de adivinar el numero")
    elif choice == "2":
        print("Empezamos el juego de jugar al ahorcado")
    elif choice == "3":
        print("Empezamos el juego de jugar al tijera")
    elif choice == "4":
        print("Hasta luego")
        PararJuego = True
    else:    
        print("Opción incorrecta")


