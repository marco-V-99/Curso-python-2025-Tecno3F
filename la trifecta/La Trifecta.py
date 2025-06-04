seguir = True
print("""***************************************
Bienvenido a la Trifecta
***************************************""")
while seguir:

    entrada_num = input("- Ingrese un número entero positivo para continuar\n- Ingrese 0 para salir\nIngrese aqui su valor: ")
    if entrada_num == "0":
        print("Saliendo del programa...")
        break

    corroboracion = entrada_num.isdigit()
    
    if not corroboracion:
        print("El valor ingresado no es un numero entero.")
        break
    if entrada_num == "0":
        print("El valor ingresado no es valido.")
        break
        
    entrada_frase = (input("Ingrese una palabra o frase:"))
    largo_frase = len(entrada_frase)
    print(f"La palabra ingresada es: {entrada_frase} \nLa longitud de la frase es: {largo_frase}")
    if largo_frase == 0:
        print("La frase no puede estar vacía.")
        break
    factorial = 1
    for i in range(1, largo_frase + 1):
        factorial *= i
    print("El factorial es:", factorial)
    
    if int(factorial) % 2 == 0:
        print("El resultado es par. \n")
    else:
        print("El resultado es impar. \n")   
   
   
    seguir == False






    

        




