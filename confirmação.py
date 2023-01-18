import PySimpleGUI as sg

class TelaPython:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
            [sg.Text("CPF DO PACIENTE: "),sg.Input(key='cpf', size= (15,8))],
             [sg.Text("VALOR DO DÉBITO: "),sg.Input(key='débito', size= (15,8))],
            
           
            [sg.Button("Próximo")]
        ]
        self.janela = sg.Window("Confirmação").layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        self.janela.close()
        return self.values

class TelaPython2:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
            [sg.Text("CPF NÃO ENCOTRADO, DIGITE NOVAMENTE:")],
            [sg.Text("CPF DO PACIENTE: "),sg.Input(key='cpf', size= (15,8))],
            
            
           
            [sg.Button("Próximo")]
        ]
        self.janela = sg.Window("Confirmação").layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        self.janela.close()
        return self.values
    
class TelaPython3:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
           
            [sg.Text("CPF DO PACIENTE: "),sg.Input(key='cpf', size= (15,8))],
            
            
           
            [sg.Button("Próximo")]
        ]
        self.janela = sg.Window("Confirmação").layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        self.janela.close()
        return self.values