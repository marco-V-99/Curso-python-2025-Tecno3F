import random

numero_secreto = random.randint(1, 100)
intentos_maximos = 5
intentos_realizados = 0
adivino = False

print("Bienvenido. Tenés que adivinar un número entre 1 y 100.")
print(f"Tenés {intentos_maximos} intentos como máximo.")

while intentos_realizados < intentos_maximos and not adivino:
    print(f"Te quedan {intentos_maximos - intentos_realizados} intentos.")
    entrada = input("Ingresá un número entre 1 y 100: ")

    if entrada.isdigit():
        numero = int(entrada)
        if 1 <= numero <= 100:
            intentos_realizados += 1

            if numero == numero_secreto:
                print("¡Adivinaste el número! Ganaste.")
                adivino = True
            elif numero < numero_secreto:
                print("El número secreto es más grande.")
            else:
                print("El número secreto es más chico.")
        else:
            print("El número debe estar entre 1 y 100.")
    else:
        print("Eso no es un número válido. Solo se aceptan números del 1 al 100.")

if not adivino:
    print(f"Perdiste. El número secreto era {numero_secreto}.")