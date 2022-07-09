from os import system
from rich.console import Console
from rich.theme import Theme
from modules import *
from database import *
from utils import *


personal_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
})


console = Console(theme=personal_theme)

db = Database()
db.carrega_classes_inicial()
menu = Menu()

if __name__ == "__main__":
    system("cls")
    console.print("Bem vindo ao sistema de gerenciamento de veículos da concessionária.", style="info")
    while True:
        console.print(menu.mensagem_inicial)
        menu.get_menu(menu.menu_principal)
        opcao = console.input("Escolha uma opção: ")
        if opcao in menu.menu_principal:
            system("cls")
            if opcao == "0":
                system("cls")
                break
            elif opcao == "1":
                while True:
                    menu.get_menu(menu.escolha_veiculo)
                    sub_opcao = console.input("Escolha o tipo de veículo para cadastro: ")
                    if sub_opcao in menu.escolha_veiculo:
                        if sub_opcao == "0":
                            system("cls")
                            break
                        elif sub_opcao == "1":
                            Carro().cadastrar_veiculo(db)
                        elif sub_opcao == "2":
                            Moto().cadastrar_veiculo(db)
                        elif sub_opcao == "3":
                            Caminhonete().cadastrar_veiculo(db)
                    else:
                        console.input("[bold red]Opção inválida - Pressione qualquer tecla para voltar...")
            elif opcao == "2":
                while True:
                    console.print('Escolha o tipo de veículo para listagem:')
                    menu.get_menu(menu.menu_relatorio_veiculos)
                    sub_opcao = console.input("Digite a opção escolhida: ")
                    if sub_opcao in menu.menu_relatorio_veiculos:
                        system("cls")
                        if sub_opcao == "0":
                            system("cls")
                            break
                        if sub_opcao == "1":
                            Veiculos().listar_veiculos(db=db, valor_index='Todos', valor_filtro='Todos', tipo_veiculo='Todos')
                        elif sub_opcao == "2":
                            Carro().listar_veiculos(db=db, valor_index='tipo_veiculo', valor_filtro='Carro', tipo_veiculo='Carro')
                        elif sub_opcao == "3":
                            Moto().listar_veiculos(db=db, valor_index='tipo_veiculo', valor_filtro='Moto/Triciclo', tipo_veiculo='Moto/Triciclo')
                        elif sub_opcao == "4":
                            Caminhonete().listar_veiculos(db=db, valor_index='tipo_veiculo', valor_filtro='Caminhonete', tipo_veiculo='Caminhonete' )
                            
                        console.input("Pressione qualquer tecla para voltar...")
                        system("cls")
                    else:
                         console.input("[bold red]Opção inválida - Pressione qualquer tecla para voltar...")
                         system("cls")  
            elif opcao == "3":
                while True:
                    console.print("Digite a placa do veículo que deseja alterar:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                    placa = console.input("Placa: ").upper()
                    
                    if placa == "":
                        system("cls")
                        break
                    
                    if placa == "LISTAR":
                        Veiculos().listar_veiculos(db=db, valor_index='status', valor_filtro='disponivel', tipo_veiculo='Todos')
                        placa = console.input("Placa: ").upper()
                        
                    veiculo_existe = db.verifica_existencia_veiculo('placa', placa)
                    veiculo_disponivel = db.verifica_disponibilidade_veiculo(placa)
                    
                    if  veiculo_existe == True and veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        console.print(f"Escolha a opção que deseja alterar - a cor atual do veículo é ({veiculo.cor}) e o valor atual é ({veiculo.valor}): ")
                        menu.get_menu(menu.menu_modificacoes_veiculos)
                        sub_opcao = console.input("Digite a opção desejada: ")
                        if sub_opcao in menu.menu_modificacoes_veiculos:
                            if sub_opcao == "0":
                                system("cls")
                                break
                            elif sub_opcao == "1":
                                veiculo.alterar_veiculo(db, 'cor')
                                break
                            elif sub_opcao == "2":
                                veiculo.alterar_veiculo(db, 'valor')
                                break
                            elif sub_opcao == "3":
                                system("cls")
                                break
                        else:
                            console.input("[bold red]Opção inválida - Pressione qualquer tecla para voltar...")
                    else:    
                        console.input("Digite qualquer tecla para continuar...")
                        system("cls")
            elif opcao == "4":
                console.print("Digite a placa do veículo que deseja vender:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                placa = console.input("Placa: ").upper()
                    
                if placa == "":
                   system("cls")
                    
                if placa == "LISTAR":
                    Veiculos().listar_veiculos(db=db, valor_index='status', valor_filtro='disponivel', tipo_veiculo='Todos')
                    placa = console.input("Placa: ").upper()
                    
                veiculo_existe = db.verifica_existencia_veiculo('placa', placa)
                veiculo_disponivel = db.verifica_disponibilidade_veiculo(placa)
                
                if  veiculo_existe == True and veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        veiculo.vender_veiculo(db)
                        console.input("\nVeículo vendido com sucesso - pressione qualquer tecla para continuar...")
                        system("cls")
                else:
                    console.input("Pressione qualquer tecla para continuar...")
                    system("cls")    
            elif opcao == "5":
                while True:
                    menu.get_menu(menu.menu_relatorios)
                    sub_opcao = console.input("Digite a opção escolhida: ")
                    
                    if sub_opcao in menu.menu_relatorios:
                        system("cls")
                        if sub_opcao == "0":
                            system("cls")
                            break
                        if sub_opcao == "1":
                             while True:
                                console.print('Escolha o tipo de veículo para listagem:')
                                menu.get_menu(menu.menu_relatorio_veiculos)
                                sub_opcao = console.input("Digite a opção escolhida: ")
                                if sub_opcao in menu.menu_relatorio_veiculos:
                                    system("cls")
                                    if sub_opcao == "0":
                                        system("cls")
                                        break
                                    if sub_opcao == "1":
                                        Veiculos().listar_veiculos(db=db, valor_index='Todos', valor_filtro='Todos', tipo_veiculo='Todos')
                                    elif sub_opcao == "2":
                                        Carro().listar_veiculos(db=db, valor_index='tipo_veiculo', valor_filtro='Carro', tipo_veiculo='Carro')
                                    elif sub_opcao == "3":
                                        Moto().listar_veiculos(db=db, valor_index='tipo_veiculo', valor_filtro='Moto/Triciclo', tipo_veiculo='Moto/Triciclo')
                                    elif sub_opcao == "4":
                                        Caminhonete().listar_veiculos(db=db, valor_index='tipo_veiculo', valor_filtro='Caminhonete', tipo_veiculo='Caminhonete' )
                                    console.input("Pressione qualquer tecla para voltar...")
                                    system("cls")
                                else:
                                    console.input("[bold red]Opção inválida - Pressione qualquer tecla para voltar...")
                                    system("cls")  
                        elif sub_opcao == "2":
                           while True:
                                console.print('Escolha o tipo de veículo para listagem:')
                                menu.get_menu(menu.menu_relatorio_vendas)
                                sub_opcao = console.input("Digite a opção escolhida: ")
                                if sub_opcao in menu.menu_relatorio_vendas:
                                    system("cls")
                                    if sub_opcao == "0":
                                        system("cls")
                                        break
                                    if sub_opcao == "1":
                                        Veiculos().listar_veiculos(db=db, valor_index='status', valor_filtro='vendido', tipo_veiculo='Todos')
                                    elif sub_opcao == "2":
                                        Carro().listar_veiculos(db=db, valor_index='status', valor_filtro='vendido', tipo_veiculo='Carro')
                                    elif sub_opcao == "3":
                                        Moto().listar_veiculos(db=db, valor_index='status', valor_filtro='vendido', tipo_veiculo='Moto/Triciclo')
                                    elif sub_opcao == "4":
                                        Caminhonete().listar_veiculos(db=db, valor_index='status', valor_filtro='vendido', tipo_veiculo='Caminhonete' )
                                    console.input("Pressione qualquer tecla para voltar...")
                                    system("cls")
                                else:
                                    console.print("[bold red]Opção inválida - Pressione qualquer tecla para voltar...")
                                    system("cls")  
                        elif sub_opcao == "3":
                            Veiculos().listar_veiculos(db=db, valor_index='status', valor_filtro='disponivel', tipo_veiculo='Todos')
                            console.input("Pressione qualquer tecla para voltar...")
                            system("cls")
                        elif sub_opcao == "4":
                            db.historico_vendas.listar_vendas()
                            console.input("Pressione qualquer tecla para voltar...")
                            system("cls")
                        elif sub_opcao == "5":
                            db.historico_vendas.maior_valor_venda()
                            console.input("Pressione qualquer tecla para voltar...")
                            system("cls")
                        elif sub_opcao == "6":
                            db.historico_vendas.menor_valor_venda()
                            console.input("Pressione qualquer tecla para voltar...")
                            system("cls")
                    else:
                        console.input("[bold red]Opção inválida - Pressione qualquer tecla para voltar...")        
                        system("cls")
        else:
            console.input("[bold red]Opção inválida")
            system("cls")
            continue
 