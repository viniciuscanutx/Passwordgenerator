import random
import PySimpleGUI as sg 
import os
from PySimpleGUI.PySimpleGUI import Text


#Class que integra todos os componentes da HUD do programa
class PassGen:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Site/Software',size=(10, 1)),
            sg.Input(key='site',size=(20, 1))],
            [sg.Text('E-mail/Usuario', size=(10,1)), 
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=12, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')],
            [sg.Button('Fechar Programa')]
            
        ]

        self.janela = sg.Window('Password Generator', layout, icon=f'./img/ico1.ico')

#Bloco que gera os eventos para funcionamento do programa
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
            if evento == 'Fechar Programa':
                break

#Definição do que vai aparecer na tela do usuário
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789@#$%*&/'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        print('Sua nova senha é:')
        new_pass = ''.join(chars)
        return new_pass

#Arquivo de Senhas
    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a',newline='') as arquivo:
            arquivo.write( 
             f"\nsite: {valores['site']} \nusuario: {valores['usuario']} \nnova senha: {nova_senha}\n")
    
        

#Gens
gen = PassGen()
gen.Iniciar()

