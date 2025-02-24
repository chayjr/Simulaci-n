#Autor: David Osvaldo Chay May
# Este tendra un menu para escoger si queire entrar al juego de los dados o de la moneda
import random as rnd

def Moneda(eleccion):
    valor = rnd.random()
    resultado = "águila" if valor > 0.50 else "sol"
    print(f"La moneda cayó en {resultado}")
    
    if eleccion.lower() == resultado:
        print("¡Ganaste!")
    else:
        print("Perdiste.")
    
    return resultado

def Dados(eleccion):
    dado = rnd.randint(1, 6)
    print(f"El dado cayó en {dado}")
    
    if eleccion == dado:
        print("¡Ganaste!")
    else:
        print("Perdiste.")
    
    return dado

def main():
    while True:
        print("---------- Menú Principal ----------")
        print("1. Dado")
        print("2. Moneda")
        print("3. Salir")
        
        opc = input("Ingrese una opción: ")
        
        if opc == "1":
            print("Bienvenido al juego de los dados")
            eleccion = int(input("Elige un número del 1 al 6: "))
            if 1 <= eleccion <= 6:
                Dados(eleccion)
            else:
                print("Número inválido. Debe ser entre 1 y 6.")
        elif opc == "2":
            print("Bienvenido al juego de la moneda")
            eleccion = input("Elige águila o sol: ")
            if eleccion.lower() in ["águila", "sol"]:
                Moneda(eleccion)
            else:
                print("Elección inválida. Debe ser 'águila' o 'sol'.")
        elif opc == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
