import PySimpleGUI as sg

class Login:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
            [sg.Text("Login"),sg.Input(key='Login')],
            [sg.Text("Senha"),sg.Input(key="Senha")],
          

            [sg.Button("Cadastrar")]
        ]
        self.janela = sg.Window("Cadastrar Sistema").layout(layout)
        self.button, self.values = self.janela.Read()
    def Iniciar(self):
        self.janela.close()
        return self.values
