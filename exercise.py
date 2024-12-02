import FreeSimpleGUI as sg
from exconv import conv
text1 = sg.Text("Enter feet: ")
box1 = sg.InputText(key='feet')
text2 = sg.Text("Enter inches: ")
box2 = sg.InputText(key='inch')
button = sg.Button("Convert")
text3 = sg.Text("",key='result')

window = sg.Window("Convertor",layout=[[text1,box1],[text2,box2],[button,text3]])
while True:
    event,values = window.read()
    feet = float(values['feet'])
    inches = float(values['inch'])
    if event == sg.WIN_CLOSED:
        break
    elif event == "Convert":
        final = round(conv(feet,inches),2)
        window['result'].update(value = final)
    # print(event)
    # print(values)
window.close()