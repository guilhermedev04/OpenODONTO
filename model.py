import time
import PySimpleGUI as sg
def time_string(): #Never mind the unreadable formatting
    return str(time.localtime().tm_year)+'/'+str(time.localtime().tm_mon)+'/'+str(time.localtime().tm_mday)+" | "+str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)

class Pacientes:

    def __init__(self,nome, cpf, telefone, indicação, rua, bairro, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.indicação = indicação
        self.consultas = []
        self.pagamentos = []
        
    def registrar_consulta(self, motivo, pagamento):
        self.consultas.append([str(time.localtime().tm_year)+'/'+str(time.localtime().tm_mon)+'/'+str(time.localtime().tm_mday)+" | "+str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)+": "+motivo, pagamento])
    def registrar_pagamento(self, pagamento):
        self.pagamentos.append(str(time.localtime().tm_year)+'/'+str(time.localtime().tm_mon)+'/'+str(time.localtime().tm_mday)+" | "+str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)+": "+pagamento)
class Funcionarios:
  

    def __init__(self,nome, cpf, telefone, salário, função, rua, bairro, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.salário = salário
        self.função = função

class Sistema:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.funcionarios = []
        self.pacientes = []
   
    def Registrar_Consulta(self, cpf,debito,motivo):
        for i in self.pacientes:
            if i.cpf == cpf:
                i.registrar_consulta(motivo,debito)
                i.registrar_pagamento(debito)
    def controle_de_pagamento(self,cpf):
        for i in self.pacientes:
            if i.cpf == cpf:
                return i.pagamentos
    def Registrar_Pagamento(self,cpf,debito):
        for i in self.pacientes:
            if i.cpf == cpf:
                i.registrar_pagamento(debito)
    def exibir_pacientes(self):
        a=[]
        for i in self.pacientes:
            a.append([i.nome,i.cpf,i.telefone,i.rua,i.bairro,i.cidade,i.estado,i.indicação])
            
        return a
    def exibir_historico_consultas(self, cpf): #OK
        a = []
        for i in self.pacientes:
            if i.cpf == cpf:
                if len(i.consultas) >=1:
                    for consulta in i.consultas:
                        a.append(consulta)
                    
                    
        return a
    def cpf_true(self, cpf): #OK
        for i in self.pacientes:
            if i.cpf == cpf:
                return True
    def dados_cpf(self,cpf):
        for i in self.pacientes:
            if i.cpf == cpf:
                return i      
    def deletar_paciente(self, cpf):
        for i in self.pacientes:
            if i.cpf == cpf:
                self.pacientes.remove(i)
                return True      
        return False
    def deletar_funcionario(self, cpf):
        for i in self.funcionarios:
            if i.cpf == cpf:
                self.funcionarios.remove(i)
                return True      
        return False
    def cadastrar_paciente(self, paciente): # OK
        self.pacientes.append(paciente)

    def cadastrar_funcionario(self, funcionario): # OK
        self.funcionarios.append(funcionario)
class Clinica:
    def __init__(self, endereço, cnpj, telefone, dono):
        self.endereço = endereço  
        self.cnpj = cnpj
        self.telefone = telefone
        self.dono = dono
