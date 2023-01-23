def questionarioinicio ():
    print('''Digite uma opção abaixo
1 PARA DÚVIDAS SOBRE EXAMES
2 PARA DUVIDAS SOBRE CONSULTAS
3 PARA FALAR COM UM ATENDENTE
4 PARA SAIR''')

def questionario2 ():
    print('''
1 - BAIXAR EXAME
2 - IMPRIMIR EXAME
3 - ENVIAR EXAME PARA O MÉDICO
4 - EXCLUIR EXAME''')

def questionario3 ():
    print('''
1 - RETORNAR AO INICIO
2 - SAIR''')

def quesconsultas1 ():
    print('''
    1 PARA VER CONSULTAS AGENDADAS
    2 PARA CANCELAR CONSULTA
    3 PARA REMARCAR CONSULTA
    ''')
def separador ():
    print('*'*30)


inicio = ''

while inicio != '4':
    questionarioinicio()
    separador()
    inicio = input('Qual é a opção desejada: ')
    separador()
    if inicio == '1':
        questionario2()
        separador()
        questio2 = input('Qual é a opção desejada para exames: ')
        separador()
        if questio2 == '1':
            print('clique aqui para baixar')
            questionario3()
            quest3 = input('Qual é a opção desejada: ')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo...')
                break
        if questio2 == '2':
            print('clique aqui para imprimir')

            questionario3()
            quest3 = input('Qual é a opção desejada ')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo...')
                break
            separador()
        if questio2 == '3':
            print('clique aqui para enviar')

            questionario3()
            quest3 = input('Qual é a opção desejada: ')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo...')
                break
            separador()
        if questio2 == '4':
            print('clique aqui para excluir')

            questionario3()
            quest3 = input('Qual é a opção desejada: ')
            if quest3 == '1':
                pass
            elif quest3 == '2':
                print('Saindo...')
                break
            separador()