import PySimpleGUI as sg
import boleto

class TelaPython:
    def __init__(self, valor, endereço, cpf, nome) :
        boleto.create_image(valor, endereço, cpf, nome)
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC', button_color=('white', '#4F4F4F'))
        layout = [
            [sg.Image(filename="bobo2.png")],
            
            [sg.Button("Sair", size=(5,2))]
        ]
        janela = sg.Window("Exibir Carnê").layout(layout)
        self.button, self.values = janela.Read()
        janela.close()


#tela = TelaPython()
