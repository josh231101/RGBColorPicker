import PySimpleGUI as sg

CALC_INFO = {
    "LONGITUD": ("Metros", "Yardas"),
    "MASA": ("Libras", "Gramos"),
    "VOLUMEN": ("Galón", "Litros")
}


def calcularConversion(magnitud, mg1, mg2, entrada):
    if magnitud == "LONGITUD":
        if mg1 == "Metros" and mg2 == "Yardas":
            return entrada * 0.914
        elif mg1 == "Yardas" and mg2 == "Metros":
            return entrada / 0.914
        else:
            return entrada
    elif magnitud == "MASA":
        if mg1 == "Libras" and mg2 == "Gramos":
            return entrada * 453.6
        elif mg1 == "Gramos" and mg2 == "Libras":
            return entrada / 453.6
        else:
            return entrada
    elif magnitud == "VOLUMEN":
        if mg1 == "Litros" and mg2 == "Galón":
            return entrada / 3.785
        elif mg1 == "Galón" and mg2 == "Litros":
            return entrada * 3.785


def cleanMagnitudes(window, magnitudes):
    window["_FIRSTC_"].Update("")
    window["_SECONDC_"].update("")
    window["_FIRSTC_"].Update(values=magnitudes)
    window["_SECONDC_"].update(values=magnitudes)
    window["_ENTRADA_"].update("")


def main():
    sg.theme("Topanga")

    layout = [
        [sg.Text("MAGNITUD")],
        [sg.Combo(("LONGITUD", "MASA", "VOLUMEN"), default_value="LONGITUD", size=(20, 4), key="_MAGNITUD_"),
         sg.Button("CAMBIAR")],
        [sg.T("Cantidad a convertir: ")],
        [sg.Input(key="_ENTRADA_")],
        [sg.Combo(["Metros", "Yardas"], key="_FIRSTC_"), sg.T("a"), sg.Combo(CALC_INFO["LONGITUD"], key="_SECONDC_")],
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
            cleanMagnitudes(window, magnitudes)
        elif event == "CALCULAR":
            salida = ""
            try:
                entrada = float(values["_ENTRADA_"])
                print(entrada)
                current_magnitud = values["_MAGNITUD_"]
                mg1 = values["_FIRSTC_"]
                mg2 = values["_SECONDC_"]
                print(mg1, mg2)
                print(current_magnitud)
                resultado = calcularConversion(current_magnitud, mg1, mg2, entrada)
                salida = f"{entrada}, {mg1} a {mg2} son {resultado}"
            except:
                salida="Ingresaste un campo vacío o un número no válido. Intenta de nuevo."

            sg.popup_ok(salida)

        else:
            continue
    window.close()


main()
