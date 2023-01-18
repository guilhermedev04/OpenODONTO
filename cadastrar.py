import PySimpleGUI as sg

class TelaPython:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
            [sg.Text("NOME"),sg.Input(key='NOME')],
            [sg.Text("CPF"),sg.Input(key="CPF")],
            [sg.Text("TELEFONE"),sg.Input(key="TELEFONE")],
            [sg.Text("RUA"),sg.Input(key="RUA")],
            [sg.Text("BAIRRO"),sg.Input(key="BAIRRO")],
            [sg.Text("CIDADE"),sg.Input(key="CIDADE")],
            [sg.Text("ESTADO"),sg.Input(key="ESTADO")],
            [sg.Text("INDICAÇÃO"),sg.Input(key="INDICAÇÃO")],

            [sg.Button("Cadastrar")]
        ]
        self.janela = sg.Window("Cadastrar Paciente").layout(layout)
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        self.janela.close()
        return self.values


class TelaPython2:
    def __init__(self) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="odonto.png")],
            [sg.Text("NOME"),sg.Input(key='NOME')],
            [sg.Text("CPF"),sg.Input(key="CPF")],
            [sg.Text("TELEFONE"),sg.Input(key="TELEFONE")],
            [sg.Text("RUA"),sg.Input(key="RUA")],
            [sg.Text("BAIRRO"),sg.Input(key="BAIRRO")],
            [sg.Text("CIDADE"),sg.Input(key="CIDADE")],
            [sg.Text("ESTADO"),sg.Input(key="ESTADO")],
            [sg.Text("SALÁRIO"),sg.Input(key="SALÁRIO")],
[sg.Text("FUNÇÃO"),sg.Input(key="FUNÇÃO")],
            [sg.Button("Cadastrar")]
        ]
        janela = sg.Window("Cadastrar Funcionário").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        return self.values



