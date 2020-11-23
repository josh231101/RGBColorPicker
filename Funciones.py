# ESTA ES EL AREA PARA HACER LAS FUNCIONES

def calcular(conversion1,entrada1):
    if conversion1 == "LITROS A GALONES":
        resultado = float(entrada1) / 3.785
    elif conversion1 == "GALONES A LITROS":
        resultado = float(entrada1) * 3.785
    # otras formulas en elif
    else:
        resultado = "intente otra conversion"
        sg.popup("Opciones disponibles:", "LITROS A GALONES", "GALONES A LITROS")  # Poner las faltantes
    return resultado



def main():
    nombre = input("Ingresa tu nombre")

    resultad = calcular_conversion(converison1,entrada1)
    sg.popup(resultado)


main()





