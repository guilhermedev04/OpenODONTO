import PySimpleGUI as sg

class TelaPython:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
            [sg.Text("Causa"),sg.Input(key='Causa', size= (15,8))],
            [sg.Text("Quanto foi?"),sg.Input(key="Pagamento")],
            
           
            [sg.Button("Cadastrar")]
        ]
        self.janela = sg.Window("Cadastrar Consulta").layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        self.janela.close()
        return self.values

