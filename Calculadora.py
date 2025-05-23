#python 3.12

#Entrada de datos del usuario 
def calculadora():
    try:
        a = int(input("Ingrese un número para calcular: "))
        print("")
        b = int(input("Elije el operable: suma, resta, multi, div"))
        c = int(input("Ingrese el segundo número para calcular: "))
    except ValueError:
        print("¡Inválido! por favor solo ingrese números y el operador dependiendo de lo que te diga :)")
  # Comprobando la respuesta del usuario
    if b.lower() == "suma":
        resultado_suma = (f"{a} + {c}")
        print(f"El resultado es: {resultado_suma}")
    elif b.lower() == "resta":
        resultado_resta = (f"{a} + {c}")
        print(f"{resultado_resta}")
    elif b.lower() == "multi":
        resultado_multi = (f"{a} * {c}")
    elif b.lower() == "div":
        resultado_div = (f"{a} / {c}")
        print(f"{resultado_div}")
    else:
        print("¡Entrada Inválida! escriba por favor números y operadores ")
  # Calculando y mostrando el resultado
    print(f"El resultado es: {d}")
    print("Espero que hayas disfrutado de la calculadora ^_^")
    print("")
    print("En desarrollo....")
if __name__ == '__main__':
    calculadora()
