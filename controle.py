import PySimpleGUI as sg
class TelaPython:
    def __init__(self,pagamentos) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        abc = ''

        for i in pagamentos:
            abc= abc+i+"R$\n"
        layout = [
           [sg.Image(filename="odonto.png")],
            [sg.Text(abc)],
            [sg.Button("Sair",size=(10,2))]
        ]
        #for i in range(40):
            #layout.append([sg.Text("abcskdfksdf sgsgs sdgsd")])


        janela = sg.Window('CONTROLE DE PAGAMENTO', resizable=True).Layout(layout)
        self.button, self.values = janela.Read()
        janela.close()
class TelaPython2:
    def __init__(self,consultas) :
        sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#5c5c5c', button_color=('white', '#4F4F4F'))
        abc = ''
        endl = "\n"
        for i in consultas:
            abc= f"{abc} {i} {endl}"
            abc = str(abc)
        layout = [
           [sg.Image(filename="odonto.png")],
            [sg.Text(abc)],
            [sg.Button("Sair",size=(10,2))]
        ]
        #for i in range(40):
            #layout.append([sg.Text("abcskdfksdf sgsgs sdgsd")])


        janela = sg.Window('CONTROLE DE PAGAMENTO', resizable=True).Layout(layout)
        self.button, self.values = janela.Read()
        janela.close()
