import PySimpleGUI as sg

def calc_imc(p,h):
    return p /(h**2)

sg.theme('Topanga')

layout = [
            [sg.T('Peso (kh): '),sg.InputText(),],
            [sg.T('Altura (m): '),sg.InputText()],
            [sg.Button("Clear"), sg.Button("Calc"), sg.Button("Salir")]
        ]

window = sg.Window('IMC CALCULATOR',layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break

    elif event == "Clear":
        window[0].update("")
        window[1].update("")
    elif event == "Calc":
        try:
            p = float(values[0])
            h = float(values[1])
            imc = calc_imc(p,h)
            sg.popup(f"IMC={imc}")
        except:
            sg.popup_ok("No ingresaste numeros o te falta un campo")

window.close()