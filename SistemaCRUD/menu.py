def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Guilherme Mourad (RA: 24024625)                             |')
    print('|                                                             |')
    print('| Versão 2.0 de 21/05/2025                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)
        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True
    return txt


def opcaoEscolhida(mnu):
    print()
    opcoesValidas = []
    for posicao in range(len(mnu)):
        print(posicao + 1, ') ', mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        if agd[meio][0].lower() == nom.lower():
            return [True, meio]
        elif agd[meio][0].lower() < nom.lower():
            inicio = meio + 1
        else:
            final = meio - 1
    return [False, inicio]


def cadastrar(agd):
    while True:
        nome = input("Digite o nome (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Cadastro não realizado.")
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            print("Nome já cadastrado. Tente outro.")
        else:
            break

    aniversario = input("Digite o aniversário: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone fixo: ")
    celular = input("Digite o celular: ")
    email = input("Digite o e-mail: ")

    contato = [nome, aniversario, endereco, telefone, celular, email]
    agd.insert(pos, contato)
    print("Cadastro realizado com sucesso!")


def procurar(agd):
    if not agd:
        print("Agenda vazia.")
        return

    while True:
        nome = input("Digite o nome a procurar (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            contato = agd[pos]
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone fixo: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"E-mail: {contato[5]}")
            return
        else:
            print("Nome não encontrado. Tente novamente.")


def atualizar(agd):
    if not agd:
        print("Agenda vazia.")
        return

    while True:
        nome = input("Digite o nome a atualizar (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            break
        else:
            print("Nome não encontrado. Tente novamente.")

    submenu = ['Atualizar Aniversário',
               'Atualizar Endereço',
               'Atualizar Telefone Fixo',
               'Atualizar Celular',
               'Atualizar E-mail',
               'Finalizar atualizações']
    
    while True:
        opcao = int(opcaoEscolhida(submenu))
        if opcao == 1:
            novo = input("Novo aniversário (ou 'cancela'): ")
            if novo.lower() == 'cancela':
                return
            agd[pos][1] = novo
        elif opcao == 2:
            novo = input("Novo endereço (ou 'cancela'): ")
            if novo.lower() == 'cancela':
                return
            agd[pos][2] = novo
        elif opcao == 3:
            novo = input("Novo telefone fixo (ou 'cancela'): ")
            if novo.lower() == 'cancela':
                return
            agd[pos][3] = novo
        elif opcao == 4:
            novo = input("Novo celular (ou 'cancela'): ")
            if novo.lower() == 'cancela':
                return
            agd[pos][4] = novo
        elif opcao == 5:
            novo = input("Novo e-mail (ou 'cancela'): ")
            if novo.lower() == 'cancela':
                return
            agd[pos][5] = novo
        else:
            print("Atualizações finalizadas.")
            return


def listar(agd):
    if not agd:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de contatos:")
    for contato in agd:
        print("-" * 40)
        print(f"Nome: {contato[0]}")
        print(f"Aniversário: {contato[1]}")
        print(f"Endereço: {contato[2]}")
        print(f"Telefone fixo: {contato[3]}")
        print(f"Celular: {contato[4]}")
        print(f"E-mail: {contato[5]}")
    print("-" * 40)


def excluir(agd):
    if not agd:
        print("Agenda vazia.")
        return

    while True:
        nome = input("Digite o nome a excluir (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            return
        achou, pos = ondeEsta(nome, agd)
        if achou:
            contato = agd[pos]
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone fixo: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"E-mail: {contato[5]}")
            confirmacao = input("Tem certeza que deseja excluir? Digite 'sim' para confirmar: ")
            if confirmacao.lower() == 'sim':
                agd.pop(pos)
                print("Contato excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            return
        else:
            print("Nome não encontrado. Tente novamente.")

# ---- Parte principal do programa ----

apresenteSe()

agenda = []  # lista principal com contatos

menu = ['Cadastrar Contato',
        'Procurar Contato',
        'Atualizar Contato',
        'Listar Contatos',
        'Excluir Contato',
        'Sair do Programa']

deseja_terminar_o_programa = False

while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))
    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    else:
        deseja_terminar_o_programa = True

print('PROGRAMA ENCERRADO COM SUCESSO!')
