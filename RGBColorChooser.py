import PySimpleGUI as sg


# Obtenido de Dietrich Epp
def rgb2hex(rgb):
    return '%02x%02x%02x' % rgb

layout = [
            [sg.Text("RED SLIDER"), sg.Text('', key='_OUTPUTR_')],
            [sg.T('0',key='_LEFTR_'),
             sg.Slider((0,255),key='_SLIDERR_', orientation='h', enable_events=True, disable_number_display=False),
             sg.T('255', key='_RIGHTR_')
            ],
            [sg.Text("GREEN SLIDER"), sg.Text('', key='_OUTPUTG_')],
            [sg.T('0', key='_LEFTG_'),
             sg.Slider((0, 255), key='_SLIDERG_', orientation='h', enable_events=True, disable_number_display=False),
             sg.T('255', key='_RIGHTG_')
             ],
            [sg.Text("BLUE SLIDER"), sg.Text('', key='_OUTPUTB_')],
            [sg.T('0', key='_LEFTB_'),
             sg.Slider((0, 255), key='_SLIDERB_', orientation='h', enable_events=True, disable_number_display=False),
             sg.T('255', key='_RIGHTB_')
             ],

            [sg.Canvas(size=(250,250),key="canvas",background_color="#000000")],
            [sg.Text(text="HEX COLOR: "),sg.Text(text='#000000',key="_HEX_"),sg.Button('Exit')]
          ]

window = sg.Window('RGB COLOR PICKER', layout)
window.Finalize()

canvas = window['canvas']
cir = canvas.TKCanvas.create_rectangle(0, 0, 250, 250)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED,'Exit'):
        break

    #COLORS
    r = int(values['_SLIDERR_'])
    g = int(values['_SLIDERG_'])
    b = int(values['_SLIDERB_'])
    hexcolor = '#' + str(rgb2hex((r,g,b)))
    canvas.TKCanvas.itemconfig(cir, fill=hexcolor)
    window["_HEX_"].update(hexcolor)
window.close()


