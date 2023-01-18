import PySimpleGUI as sg
import EXIBIR_BOLETO
import model
import cadastrar
import login
import confirmação
import historico
import controle
import registrar_consulta
sg.SetOptions(background_color='#363636', text_element_background_color='#363636', element_background_color='#363636', scrollbar_color=None, input_elements_background_color='#F7F3EC', button_color=('white', '#4F4F4F'))
layout = [[sg.Image(filename="odonto.png")],[sg.Text("Equipe:")], [sg.Text("GUILHERME SILVA")],[sg.Text("JEAN CARLOS")],[sg.Button("Próximo")]]
    ###Setting Window

window = sg.Window('iNTEGRANTES', layout)
event, values = window.read()
window.close()

Login_sistema = login.Login()
outs = Login_sistema.Iniciar()
sistema = model.Sistema(outs["Login"],outs["Senha"])

while True:
    layout = [
        [sg.Image(filename="odonto.png")],
        [sg.Text("Escolha sua opção!")],
            [sg.Radio('Cadastrar Paciente', "RADIO1",  key="opc1")],
            [sg.Radio('Cadastrar Funcionário', "RADIO1",key="opc2")],
            [sg.Radio('Exibir todos os pacientes cadastrados', "RADIO1",key="opc3")],
            [sg.Radio('Apagar paciente', "RADIO1",key="opc4")],
            [sg.Radio('Apagar funcionario', "RADIO1",key="opc5")],
            [sg.Radio('Controle de pagamento', "RADIO1",key="opc6")],
            [sg.Radio('Criar carnê', "RADIO1",key="opc7")],
            [sg.Radio('Exibir históricos de consultas', "RADIO1",key="opc8")],
            [sg.Radio('Cadastrar Consulta', "RADIO1",key="opc9")],
            [sg.Button("Próximo")]
            ]
    ###Setting Window
    window = sg.Window('Menu', layout)

    ###Showing the Application, also GUI functions can be placed here.

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values["opc1"] == True :
        tela = cadastrar.TelaPython()
        resultados = tela.Iniciar()
        
        paciente = model.Pacientes(resultados['NOME'],resultados["CPF"],resultados["TELEFONE"],resultados["INDICAÇÃO"],resultados["RUA"],resultados["BAIRRO"],resultados["CIDADE"],resultados["ESTADO"])
        sistema.cadastrar_paciente(paciente)
        #print(resultados)
    elif values["opc2"] == True :
        tela = cadastrar.TelaPython2()
        resultados = tela.Iniciar()
        #nome, cpf, telefone, salário, função, rua, bairro, cidade, estado
        paciente = model.Funcionarios(resultados['NOME'],resultados["CPF"],resultados["TELEFONE"],resultados["SALÁRIO"],resultados["FUNÇÃO"],resultados["RUA"],resultados["BAIRRO"],resultados["CIDADE"],resultados["ESTADO"])
        sistema.cadastrar_funcionario(paciente)
        #print(resultados)
    elif values["opc3"] == True :
        pacientes = (sistema.exibir_pacientes())
        lista = []
        for i in pacientes:
            lista.append(f"Nome: {i[0]} CPF: {i[1]} TELEFONE: {i[2]} ENDEREÇO: {i[3]} {i[4]} {i[5]} {i[6]} INDICAÇÂO: {i[7]}")
        abc = historico.TelaPython( False,False,lista)

  


    elif values["opc4"] == True :
        
            a = confirmação.TelaPython3()
            cpf = (a.Iniciar())["cpf"]
            while True:
                if sistema.deletar_paciente(cpf):
                    break
                a = confirmação.TelaPython2()
                cpf = (a.Iniciar())["cpf"]
    elif values["opc5"] == True :
        a = confirmação.TelaPython3()
        cpf = (a.Iniciar())["cpf"]
        while True:
            if sistema.deletar_funcionario(cpf):
                break
            a = confirmação.TelaPython2()
            cpf = (a.Iniciar())["cpf"]
    elif values["opc6"] == True :
        a = confirmação.TelaPython3()
        cpf = (a.Iniciar())["cpf"]
        while True:
            if sistema.cpf_true(cpf):
                a = sistema.controle_de_pagamento(cpf)
                b = controle.TelaPython(a)
                break
            a = confirmação.TelaPython2()
            cpf = (a.Iniciar())["cpf"]
        

    elif values["opc7"] == True : # pronto
        a = confirmação.TelaPython()
        cpf = (a.Iniciar())["cpf"]
        debito = (a.Iniciar())["débito"]
        if sistema.cpf_true(cpf):
            dados = sistema.dados_cpf(cpf)
            EXIBIR_BOLETO.TelaPython(debito, dados.rua, cpf, dados.nome)
            sistema.Registrar_Pagamento(cpf,debito)
        else:
            while True:
                a = confirmação.TelaPython2()
                cpf = (a.Iniciar())["cpf"]
                if sistema.cpf_true(cpf):
                    
                    dados = sistema.dados_cpf(cpf)
                    EXIBIR_BOLETO.TelaPython(debito, dados.rua, cpf, dados.nome)
                    sistema.Registrar_Pagamento(cpf,debito)

                    break
    elif values["opc8"] == True :
        a = confirmação.TelaPython3()
        cpf = (a.Iniciar())["cpf"]
        while True:
            if sistema.cpf_true(cpf):
                a = sistema.exibir_historico_consultas(cpf)
                b = controle.TelaPython2(a)
                break

            a = confirmação.TelaPython2()
            cpf = (a.Iniciar())["cpf"]
        sistema.exibir_historico_consultas(cpf)

    else :
        a = confirmação.TelaPython3()
        cpf = (a.Iniciar())["cpf"]
        while True:
            if sistema.cpf_true(cpf):
                b = registrar_consulta.TelaPython()
                motivo = (b.Iniciar())["Causa"]
                debito = (b.Iniciar())["Pagamento"]
                a = sistema.Registrar_Consulta(cpf, debito, motivo)
                break

            a = confirmação.TelaPython2()
            cpf = (a.Iniciar())["cpf"]
        
    window.close()