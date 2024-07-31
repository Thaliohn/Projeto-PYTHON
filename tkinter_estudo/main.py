import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Graus'), sg.Input()],
            [sg.Button('Verificar Ponto')]
        ]
        janela = sg.Window("Carne No Ponto").layout(layout)

        self.button, self.values = janela.Read()
    
    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()