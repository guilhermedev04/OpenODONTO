import PySimpleGUI as sg
class TelaPython:
    def __init__(self,scrollable=False, vertical_scroll_only=False,pacientes=[]) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        print(pacientes)
        column1 = [
            
]

        for i in pacientes:
            column1.append([sg.Text(i)])
        layout = [
           [sg.Image(filename="odonto.png")],
            [sg.Column(column1, scrollable=True,  vertical_scroll_only=True, size=(900,500))],
            [sg.Button("Sair",size=(10,2))]
        ]
        #for i in range(40):
            #layout.append([sg.Text("abcskdfksdf sgsgs sdgsd")])


        janela = sg.Window('Todos os pacientes cadastrados no banco de dados', resizable=True).Layout(layout)
        self.button, self.values = janela.Read()
        janela.close()
