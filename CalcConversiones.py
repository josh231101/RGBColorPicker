import PySimpleGUI as sg

#UTILS
def convert_LONGITUD(value,option):
    return value * 0.914 if option == "Metros a Yardas" else value/0.914

def convert_MASA(value,option):
    return value * 453.6 if option == "Libras a Gramos" else value/453.6

def convert_VOLUMEN(value,option):
    return value*3.785 if option == "Galón a litros" else value/3.785


calc_info = {
    "LONGITUD": {
        "TITLE": "Longitud",
        "COMBO": ("Metros a Yardas", "Yardas a Metros"),
        "CONVERSION" : convert_LONGITUD,
    },
    "MASA" : {
        "TITLE": "Masa",
        "COMBO": ("Libras a Gramos","Gramos a Libras"),
        "CONVERSION": convert_MASA,
    },
    "VOLUMEN" : {
        "TITLE": "Volumen",
        "COMBO": ("Galón a litros", "Litros a Galón"),
        "CONVERSION": convert_VOLUMEN,
    },

}
def createLayout(ev1):
    layout_2 = [
        [sg.Text("Ingresa la cantidad a convertir: ")],
        [sg.Input(key="_VALUE_")],
        [sg.Combo((calc_info[ev1]["COMBO"]), default_value=calc_info[ev1]["COMBO"][0],key="_CONVERSION_")],
        [sg.Button("CALCULATE")]
    ]
    return layout_2

sg.theme('Topanga')

layout = [
            [sg.Image(r'CALCR.png')],
            [sg.Text("Magnitud a Calcular:")],
            [sg.Button("LONGITUD",size=(25,2))],
            [sg.Button("MASA",size=(25,2))],
            [sg.Button("VOLUMEN",size=(25,2))],
        ]

win1 = sg.Window("CALCULADOR DE MAGNITUDES",layout)



while True:
    ev1, val1= win1.read()
    if ev1 in (sg.WINDOW_CLOSED, "Close"):
        break
    if ev1 in ("LONGITUD","MASA","VOLUMEN"):
        win1.Hide()
        layout = createLayout(ev1)

        win2 = sg.Window(calc_info[ev1]["TITLE"]).Layout(layout)
        while True:
           ev2,val2 = win2.read()
           if ev2 == sg.WIN_CLOSED:
               win2.close()
               win1.UnHide()
               break
           if ev2 == "CALCULATE":
                try:
                    value = float(val2["_VALUE_"])
                    conversion = val2["_CONVERSION_"]
                    result = calc_info[ev1]["CONVERSION"](value,conversion)
                    sg.popup(result)
                except:
                    sg.popup("No ingresaste un valor entero positivo o ingresaste un campo vacío","Intenta de nuevo")


win1.close()