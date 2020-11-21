import PySimpleGUI as sg

# .:FUNCTIONS:.

# Conversions Functions
def convert_LONGITUD(value, option):
    # We use ternary operator because there are always only 2 options
    return value * 0.914 if option == "Metros a Yardas" else value / 0.914

def convert_MASA(value, option):
    return value * 453.6 if option == "Libras a Gramos" else value / 453.6

def convert_VOLUMEN(value, option):
    return value * 3.785 if option == "Galón a litros" else value / 3.785

# Layouts functions
def createMainLayout():
    layout = [
        [sg.Image(r'CALCR.png')],
        [sg.Text("Magnitud a Calcular:")],
        [sg.Button("LONGITUD", size=(25, 2))],
        [sg.Button("MASA", size=(25, 2))],
        [sg.Button("VOLUMEN", size=(25, 2))],
    ]
    return layout

def createLayout(ev1):
    layout_2 = [
        [sg.Text("Ingresa la cantidad a convertir: ")],
        [sg.Input(key="_VALUE_")],
        [sg.Combo(calc_info[ev1]["COMBO"], default_value=calc_info[ev1]["COMBO"][0], key="_CONVERSION_")],
        [sg.Button("CALCULATE")]
    ]
    return layout_2

# .:UTILS:.
# Our dictionary will handle the informations,functions that will operate in the second layout
calc_info = {
    "LONGITUD": {
        "TITLE": "Longitud",
        "COMBO": ("Metros a Yardas", "Yardas a Metros"),
        "CONVERSION": convert_LONGITUD,
    },
    "MASA": {
        "TITLE": "Masa",
        "COMBO": ("Libras a Gramos", "Gramos a Libras"),
        "CONVERSION": convert_MASA,
    },
    "VOLUMEN": {
        "TITLE": "Volumen",
        "COMBO": ("Galón a litros", "Litros a Galón"),
        "CONVERSION": convert_VOLUMEN,
    },
}

def main():
    sg.theme('Topanga')
    # Create the main layout and then the window
    main_layout = createMainLayout()
    win1 = sg.Window("CALCULADOR DE MAGNITUDES", main_layout)

    while True:
        ev1, val1 = win1.read()
        if ev1 == sg.WINDOW_CLOSED:
            break
        # To avoid errors we hide the MAIN window.
        win1.Hide()

        # Create second layout passing the event value so it knows the correct info to be display.
        layout_2 = createLayout(ev1)
        win2 = sg.Window(calc_info[ev1]["TITLE"]).Layout(layout_2)

        # CREATING SECOND WINDOW
        while True:
            ev2, val2 = win2.read()
            if ev2 == sg.WIN_CLOSED:
                # Close the second window and UNHIDE(show) the first one.
                win2.close()
                win1.UnHide()
                break

            try:
                # Getting the user value and option to convert.
                value = float(val2["_VALUE_"])
                conversion = val2["_CONVERSION_"]
                # Call the option according to user option to convert.
                result = calc_info[ev1]["CONVERSION"](value, conversion)
                result = round(result, 4)
                sg.popup(result)
            except:
                # VALIDATION: The user pass none,not a number,letters,symbols,etc.
                sg.popup("No ingresaste un valor entero o ingresaste un campo vacío", "Intenta de nuevo")

    # Main window gets closed
    win1.close()

main()
