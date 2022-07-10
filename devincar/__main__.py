from database import *
from modules import *
from rich.console import Console
from rich.theme import Theme
from utils import *

personal_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "sucesso": "bold green",
})

console = Console(theme=personal_theme)
db = Database()
db.carrega_classes_inicial()
menu = Menu()

if __name__ == "__main__":
    menu.limpar_menu(console=console)
    console.print(
        "Bem vindo ao sistema de gerenciamento de veículos da concessionária. :car:", style="info")
    while True:
        console.print(menu.mensagem_inicial)
        menu.get_menu(menu.menu_principal)
        opcao = console.input("Escolha uma opção: ")
        if opcao in menu.menu_principal:
            menu.limpar_menu(console=console)
            if opcao == "0":  # sair
                menu.limpar_menu(console=console)
                break
            elif opcao == "1":  # cadastro de veículos
                while True:
                    menu.get_menu(menu.escolha_veiculo)
                    sub_opcao = console.input(
                        "Escolha o tipo de veículo para cadastro: ")
                    if sub_opcao in menu.escolha_veiculo:
                        if sub_opcao == "0":
                            menu.limpar_menu(console=console)
                            break
                        elif sub_opcao == "1":
                            Carro().cadastrar_veiculo(db)
                            menu.barra_progresso('Cadastrando veículo...')
                            menu.limpar_menu(
                                console=console, tipo='input', texto="Veículo cadastrado com sucesso!\nPressione qualquer tecla para voltar...", estilo='sucesso')
                        elif sub_opcao == "2":
                            MotoTriciclo().cadastrar_veiculo(db)
                            menu.barra_progresso('Cadastrando veículo...')
                            menu.limpar_menu(
                                console=console, tipo='input', texto="Veículo cadastrado com sucesso!\nPressione qualquer tecla para voltar...", estilo='sucesso')
                        elif sub_opcao == "3":
                            Caminhonete().cadastrar_veiculo(db)
                            menu.barra_progresso('Cadastrando veículo...')
                            menu.limpar_menu(
                                console=console, tipo='input', texto="Veículo cadastrado com sucesso!\nPressione qualquer tecla para voltar...", estilo='sucesso')
                    else:
                        menu.limpar_menu(
                            console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
            elif opcao == "2":  # listagem de veículos
                while True:
                    console.print('Escolha o tipo de veículo para listagem:')
                    menu.get_menu(menu.menu_relatorio_veiculos)
                    sub_opcao = console.input("Digite a opção escolhida: ")
                    if sub_opcao in menu.menu_relatorio_veiculos:
                        menu.limpar_menu(console=console)
                        if sub_opcao == "0":
                            menu.limpar_menu(console=console)
                            break
                        if sub_opcao == "1":
                            Veiculos().listar_veiculos(db=db, valor_index='Todos',
                                                       valor_filtro='Todos', tipo_veiculo='Todos')
                        elif sub_opcao == "2":
                            Carro().listar_veiculos(db=db, valor_index='tipo_veiculo',
                                                    valor_filtro='Carro', tipo_veiculo='Carro')
                        elif sub_opcao == "3":
                            MotoTriciclo().listar_veiculos(db=db, valor_index='tipo_veiculo',
                                                           valor_filtro='MotoTriciclo', tipo_veiculo='MotoTriciclo')
                        elif sub_opcao == "4":
                            Caminhonete().listar_veiculos(db=db, valor_index='tipo_veiculo',
                                                          valor_filtro='Caminhonete', tipo_veiculo='Caminhonete')

                        menu.limpar_menu(
                            console=console, tipo='input', texto="Pressione qualquer tecla para continuar...", estilo='info')
                    else:
                        menu.limpar_menu(
                            console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
            elif opcao == "3":  # alterar veículo
                while True:
                    console.print(
                        "Digite a placa do veículo que deseja alterar:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                    placa = console.input("Placa: ").upper()

                    if placa == "":
                        menu.limpar_menu(console=console)
                        break

                    if placa == "LISTAR":
                        Veiculos().listar_veiculos(db=db, valor_index='status',
                                                   valor_filtro='disponivel', tipo_veiculo='Todos')
                        placa = console.input("Placa: ").upper()

                    veiculo_disponivel = db.verifica_disponibilidade_veiculo(
                        placa)

                    if veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        console.print(
                            f"Escolha a opção que deseja alterar - a cor atual do veículo é ({veiculo.cor}) e o valor atual é ({veiculo.valor}): ")
                        menu.get_menu(menu.menu_modificacoes_veiculos)
                        sub_opcao = console.input("Digite a opção desejada: ")
                        if sub_opcao in menu.menu_modificacoes_veiculos:
                            while True:
                                if sub_opcao == "0":
                                    menu.limpar_menu(console=console)
                                    break
                                elif sub_opcao == "1":
                                    veiculo.alterar_veiculo(db, 'cor')
                                    menu.barra_progresso(
                                        'Alterando cor do veículo...')
                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Veículo alterado com sucesso!\nPressione qualquer tecla para voltar...", estilo='sucesso')
                                    break
                                elif sub_opcao == "2":
                                    veiculo.alterar_veiculo(db, 'valor')
                                    menu.barra_progresso(
                                        'Alterando valor do veículo...')
                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Veículo alterado com sucesso!\nPressione qualquer tecla para voltar...", estilo='sucesso')
                                    break
                                elif sub_opcao == "3":
                                    menu.limpar_menu(console=console)
                                    break
                                else:
                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
                        else:
                            menu.limpar_menu(
                                console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
                    else:
                        menu.limpar_menu(console=console, tipo='input',
                                         texto="Veiculo não encontrado ou não disponível.", estilo='erro')
            elif opcao == "4":  # vender veículo
                while True:
                    console.print(
                        "Digite a placa do veículo que deseja vender:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                    placa = console.input("Placa: ").upper()

                    if placa == "":
                        menu.limpar_menu(console=console)
                        break

                    if placa == "LISTAR":
                        Veiculos().listar_veiculos(db=db, valor_index='status',
                                                   valor_filtro='disponivel', tipo_veiculo='Todos')
                        placa = console.input("Placa: ").upper()

                    veiculo_disponivel = db.verifica_disponibilidade_veiculo(
                        placa)

                    if veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        veiculo.vender_veiculo(db)
                        menu.barra_progresso('Realizando operação de venda...')
                        menu.limpar_menu(console=console, tipo='input',
                                         texto="Veículo vendido com sucesso!", estilo='sucesso')
                    else:
                        menu.limpar_menu(
                            console=console, tipo='input', texto="Veiculo não disponível - Pressione qualquer tecla para continuar...", estilo='erro')
                        continue
            elif opcao == "5":  # relatórios
                while True:
                    menu.get_menu(menu.menu_relatorios)
                    sub_opcao = console.input("Digite a opção escolhida: ")

                    if sub_opcao in menu.menu_relatorios:
                        menu.limpar_menu(console=console)
                        if sub_opcao == "0":
                            menu.limpar_menu(console=console)
                            break
                        if sub_opcao == "1":
                            while True:
                                console.print(
                                    'Escolha o tipo de veículo para listagem:')
                                menu.get_menu(menu.menu_relatorio_veiculos)
                                sub_opcao = console.input(
                                    "Digite a opção escolhida: ")
                                if sub_opcao in menu.menu_relatorio_veiculos:
                                    menu.limpar_menu(console=console)
                                    if sub_opcao == "0":
                                        menu.limpar_menu(console=console)
                                        break
                                    if sub_opcao == "1":
                                        Veiculos().listar_veiculos(db=db, valor_index='status',
                                                                   valor_filtro='disponivel', tipo_veiculo='Todos')
                                    elif sub_opcao == "2":
                                        Carro().listar_veiculos(db=db, valor_index='status',
                                                                valor_filtro='disponivel', tipo_veiculo='Carro')
                                    elif sub_opcao == "3":
                                        MotoTriciclo().listar_veiculos(db=db, valor_index='status',
                                                                       valor_filtro='disponivel', tipo_veiculo='MotoTriciclo')
                                    elif sub_opcao == "4":
                                        Caminhonete().listar_veiculos(db=db, valor_index='status',
                                                                      valor_filtro='disponivel', tipo_veiculo='Caminhonete')
                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Pressione qualquer tecla para continuar...", estilo='info')
                                else:
                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
                        elif sub_opcao == "2":
                            while True:
                                console.print(
                                    'Escolha o tipo de veículo para listagem:')
                                menu.get_menu(menu.menu_relatorio_vendas)
                                sub_opcao = console.input(
                                    "Digite a opção escolhida: ")
                                if sub_opcao in menu.menu_relatorio_vendas:
                                    menu.limpar_menu(console=console)
                                    if sub_opcao == "0":
                                        menu.limpar_menu(console=console)
                                        break
                                    if sub_opcao == "1":
                                        Veiculos().listar_veiculos(db=db, valor_index='status',
                                                                   valor_filtro='vendido', tipo_veiculo='Todos')
                                    elif sub_opcao == "2":
                                        Carro().listar_veiculos(db=db, valor_index='status',
                                                                valor_filtro='vendido', tipo_veiculo='Carro')
                                    elif sub_opcao == "3":
                                        MotoTriciclo().listar_veiculos(db=db, valor_index='status',
                                                                       valor_filtro='vendido', tipo_veiculo='MotoTriciclo')
                                    elif sub_opcao == "4":
                                        Caminhonete().listar_veiculos(db=db, valor_index='status',
                                                                      valor_filtro='vendido', tipo_veiculo='Caminhonete')
                                    elif sub_opcao == "5":
                                        Veiculos().listar_veiculos(db=db, valor_index='maior',
                                                                   valor_filtro='vendido', tipo_veiculo='Todos')
                                    elif sub_opcao == "6":
                                        Veiculos().listar_veiculos(db=db, valor_index='menor',
                                                                   valor_filtro='vendido', tipo_veiculo='Carro')

                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Pressione qualquer tecla para continuar...", estilo='info')
                                else:
                                    menu.limpar_menu(
                                        console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')

                    else:
                        menu.limpar_menu(
                            console=console, tipo='input', texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
        else:
            menu.limpar_menu(console=console, tipo='input',
                             texto="Opção inválida - Pressione qualquer tecla para voltar...", estilo='erro')
            continue
