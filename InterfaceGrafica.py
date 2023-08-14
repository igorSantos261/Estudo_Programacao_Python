from PySimpleGUI import PySimpleGUI as sg

#Criação de Layout
sg.theme('Reddit')
Layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]
]
#Criação da Janela
janela = sg.Window('Tela De Login', Layout)
#Ler os Eventos que são Inseridos
while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Isantos' and valores['senha'] == '123456':
            print('Bem vindo ao Sistema !')

