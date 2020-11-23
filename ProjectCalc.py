import PySimpleGUI as sg

def calcularConversion(magnitud, u1, u2, entrada):
    if magnitud == "LONGITUD":
        # In case we convert Meters to Yd we use the formula, else means it's inverted so we use the inverted formula
        return entrada * 0.914 if u1 == "Metros" and u2 == "Yardas" else entrada / 0.914
    elif magnitud == "MASA":
        return entrada * 453.6 if u1 == "Libras" and u2 == "Gramos" else entrada / 463.6
    elif magnitud == "VOLUMEN":
        return entrada / 3.785 if u1 == "Litros" and u2 == "Galón" else entrada * 3.785

def cleanAndUpdateMagnitude(window, magnitude):    # This method cleans the input and combo box to the correct units
    window["_ENTRADA_"].update("")  # Clean the input and combos
    window["_UNIT1_"].Update("")
    window["_UNIT2_"].update("")
    window["_UNIT1_"].Update(values=magnitude) # Update the units to the according magnitude
    window["_UNIT2_"].update(values=magnitude)

def validateInput(entrada, combo_1, combo_2):
    if entrada != "" and combo_1 != "" and combo_2 != "":   # Both units and input are filled
        try:
            # If user sends letters and invalid characters we send the user to the exception
            entrada = float(entrada)
            if combo_1 != combo_2:  # User must choose different units
                # The number must be positive
                return True if entrada > 0 else "Ingresa por favor un número positivo mayor a cero"
            else:
                return "Ingresaste las mismas unidades"
        except ValueError:
            return "Ingresa un número entero"
    else:
        return "Ingresa todos los campos!"

# Create info for the combos
CALC_INFO = {
    "LONGITUD": ("Metros", "Yardas"),
    "MASA": ("Libras", "Gramos"),
    "VOLUMEN": ("Galón", "Litros")
}

def main():
    sg.theme("Topanga")
    # Create layout
    layout = [
        [sg.Text("MAGNITUD A CALCULAR: ")],
        [sg.Combo(("LONGITUD", "MASA", "VOLUMEN"), default_value="LONGITUD", size=(20, 4), key="_MAGNITUD_"),
         sg.Button("CAMBIAR")],
        [sg.T("Cantidad a convertir: ")],
        [sg.Input(key="_ENTRADA_")],
        [sg.Combo(CALC_INFO["LONGITUD"], key="_UNIT1_"), sg.T("a"), sg.Combo(CALC_INFO["LONGITUD"], key="_UNIT2_")],
        [sg.Button("CALCULAR")]
    ]
    window = sg.Window("CALCULADORA DE CONVERSIONES", layout)

    while True:
        event, values = window.read() # Read the window
        if event == sg.WIN_CLOSED:  # User clicked X btn
            break
        elif event == "CAMBIAR":    # User wants to change magnitude
            # Get the user magnitude to calculate
            magnitude_units = CALC_INFO[values["_MAGNITUD_"]]
            # Clean the screen and update combobox info to the corresponding magnitude units
            cleanAndUpdateMagnitude(window, magnitude_units)
        elif event == "CALCULAR":
            entrada = values["_ENTRADA_"]
            unit_1 = values["_UNIT1_"] # The first unit (from)
            unit_2 = values["_UNIT2_"] # The second unit(to)
            # VALIDATE USER INPUT
            if validateInput(entrada, unit_1, unit_2) == True:  # Validate the user form
                current_magnitude = values["_MAGNITUD_"]
                entrada = float(entrada)    # Convert to float the input to calculate the conversion
                resultado = calcularConversion(current_magnitude, unit_1, unit_2,entrada)
                salida = f"Al convertir {entrada}, de {unit_1} a {unit_2} obtenemos {resultado}"
            else:
                salida = validateInput(entrada, unit_1, unit_2) # Function returns the msg of the error
            sg.popup_ok(salida) #Print the result in the popup

    window.close()
main()
