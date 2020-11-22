import PySimpleGUI as sg

CALC_INFO = {
    "LONGITUD": ("Metros", "Yardas"),
    "MASA": ("Libras", "Gramos"),
    "VOLUMEN": ("Galón", "Litros")
}

def calcularConversion(magnitud, mg1, mg2, entrada):
    if magnitud == "LONGITUD":
        # In case we convert Meters to Yd we use the formula, else means it's inverted so we use the inverted formula
        return entrada * 0.914 if mg1 == "Metros" and mg2 == "Yardas" else entrada / 0.914
    elif magnitud == "MASA":
        return entrada * 453.6 if mg1 == "Libras" and mg2 == "Gramos" else entrada / 463.6
    elif magnitud == "VOLUMEN":
        return entrada / 3.785 if mg1 == "Litros" and mg2 == "Galon" else entrada * 3.785

def cleanAndUpdateMagnitudes(window, magnitudes):
    window["_ENTRADA_"].update("")
    window["_FIRSTC_"].Update("")
    window["_SECONDC_"].update("")
    window["_FIRSTC_"].Update(values=magnitudes)
    window["_SECONDC_"].update(values=magnitudes)

def validateInput(entrada, combo_1, combo_2):
    if entrada != "" and combo_1 != "" and combo_2 != "":
        try:
            # If user sends leters and invalid characters we send the user to the exception
            entrada = float(entrada)
            if combo_1 != combo_2:
                return True if entrada > 0 else "Ingresa por favor un número positivo mayor a cero"
            else:
                return "Ingresaste las mismas magnitudes"
        except ValueError:
            return "Ingresa un número entero"
    else:
        return "Ingresa todos los campos!"

def main():
    sg.theme("Topanga")

    layout = [
        [sg.Text("MAGNITUD A CALCULAR: ")],
        [sg.Combo(("LONGITUD", "MASA", "VOLUMEN"), default_value="LONGITUD", size=(20, 4), key="_MAGNITUD_"),
         sg.Button("CAMBIAR")],
        [sg.T("Cantidad a convertir: ")],
        [sg.Input(key="_ENTRADA_")],
        [sg.Combo(CALC_INFO["LONGITUD"], key="_FIRSTC_"), sg.T("a"), sg.Combo(CALC_INFO["LONGITUD"], key="_SECONDC_")],
        [sg.Button("CALCULAR")]
    ]
    window = sg.Window("CALCULADORA DE CONVERSIONES", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "CAMBIAR":
            # Get the user magnitude to calculate
            magnitudes = CALC_INFO[values["_MAGNITUD_"]]
            # Clean the screen and combobox info
            cleanAndUpdateMagnitudes(window, magnitudes)
        elif event == "CALCULAR":
            entrada = values["_ENTRADA_"]
            mg_1 = values["_FIRSTC_"]
            mg_2 = values["_SECONDC_"]
            # VALIDATE USER INPUT
            if validateInput(entrada, mg_1, mg_2) == True:
                current_magnitude = values["_MAGNITUD_"]
                entrada = float(entrada)
                resultado = calcularConversion(current_magnitude, mg_1, mg_2,entrada)
                salida = f"Al convertir {entrada} de {mg_1} a {mg_2} obtenemos {resultado}"
            else:
                salida = validateInput(entrada, mg_1, mg_2)
            sg.popup_ok(salida)

    window.close()
main()
