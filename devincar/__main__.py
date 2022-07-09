from os import system
from rich import print as rprint
from modules import *
from database import *
from utils import *

db = Database()
menu = Menu()
db.carrega_classes_inicial()

if __name__ == "__main__":
    system("cls")
    rprint("Bem vindo ao sistema de gerenciamento de veículos da concessionária.")
    while True:
        print(menu.mensagem_inicial)
        menu.get_menu(menu.menu_principal)
        opcao = input("Escolha uma opção: ")
        if opcao in menu.menu_principal:
            system("cls")
            if opcao == "0":
                system("cls")
                break
            elif opcao == "1":
                while True:
                    menu.get_menu(menu.escolha_veiculo)
                    sub_opcao = input("Escolha o tipo de veículo para cadastro: ")
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
                        rprint("Opção inválida")
            elif opcao == "2":
                while True:
                    rprint('Escolha o tipo de veículo para listagem:')
                    menu.get_menu(menu.menu_relatorio_veiculos)
                    sub_opcao = input("Digite a opção escolhida: ")
                    if sub_opcao in menu.menu_relatorio_veiculos:
                        system("cls")
                        if sub_opcao == "0":
                            system("cls")
                            break
                        if sub_opcao == "1":
                            db.listar_todos_veiculos()
                        elif sub_opcao == "2":
                            Carro().listar_veiculos(db)
                        elif sub_opcao == "3":
                            Moto().listar_veiculos(db)
                        elif sub_opcao == "4":
                            Caminhonete().listar_veiculos(db)
                            
                        input("Pressione qualquer tecla para voltar...")
                        system("cls")
                    else:
                         input('Opção inválida')
                         system("cls")  
            elif opcao == "3":
                while True:
                    rprint("Digite a placa do veículo que deseja alterar:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                    placa = input("Placa: ").upper()
                    
                    if placa == "":
                        system("cls")
                        break
                    
                    if placa == "LISTAR":
                        rprint(f"Listando todos os veiculos disponíveis".center(50, "-"))
                        db.listar_veiculos_disponiveis()
                        placa = input("Placa: ").upper()
                        
                    veiculo_existe = db.verifica_existencia_veiculo('placa', placa)
                    veiculo_disponivel = db.verifica_disponibilidade_veiculo(placa)
                    
                    if  veiculo_existe == True and veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        rprint(f"Escolha a opção que deseja alterar - a cor atual do veículo é ({veiculo.cor}) e o valor atual é ({veiculo.valor}): ")
                        menu.get_menu(menu.menu_modificacoes_veiculos)
                        sub_opcao = input("Digite a opção desejada: ")
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
                            rprint("Opção inválida")
                    else:    
                        input("Digite qualquer tecla para continuar...")
                        system("cls")
            elif opcao == "4":
                rprint("Digite a placa do veículo que deseja vender:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                placa = input("Placa: ").upper()
                    
                if placa == "":
                   system("cls")
                    
                if placa == "LISTAR":
                    rprint(f"Listando todos os veiculos disponíveis".center(50, "-"))
                    db.listar_veiculos_disponiveis()
                    placa = input("Placa: ").upper()
                    
                veiculo_existe = db.verifica_existencia_veiculo('placa', placa)
                veiculo_disponivel = db.verifica_disponibilidade_veiculo(placa)
                
                if  veiculo_existe == True and veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        veiculo.vender_veiculo(db)
                        input("\nVeículo vendido com sucesso - pressione qualquer tecla para continuar...")
                        system("cls")
                else:
                    input("Pressione qualquer tecla para continuar...")
                    system("cls")    
            elif opcao == "5":
                while True:
                    menu.get_menu(menu.menu_relatorios)
                    sub_opcao = input("Digite a opção escolhida: ")
                    
                    if sub_opcao in menu.menu_relatorios:
                        system("cls")
                        if sub_opcao == "0":
                            system("cls")
                            break
                        if sub_opcao == "1":
                             while True:
                                rprint('Escolha o tipo de veículo para listagem:')
                                menu.get_menu(menu.menu_relatorio_veiculos)
                                sub_opcao = input("Digite a opção escolhida: ")
                                if sub_opcao in menu.menu_relatorio_veiculos:
                                    system("cls")
                                    if sub_opcao == "0":
                                        system("cls")
                                        break
                                    if sub_opcao == "1":
                                        db.listar_todos_veiculos()
                                    elif sub_opcao == "2":
                                        Carro().listar_veiculos(db)
                                    elif sub_opcao == "3":
                                        Moto().listar_veiculos(db)
                                    elif sub_opcao == "4":
                                        Caminhonete().listar_veiculos(db)
                                    input("Pressione qualquer tecla para voltar...")
                                    system("cls")
                                else:
                                    input('Opção inválida')
                                    system("cls")  
                        elif sub_opcao == "2":
                           while True:
                                rprint('Escolha o tipo de veículo para listagem:')
                                menu.get_menu(menu.menu_relatorio_vendas)
                                sub_opcao = input("Digite a opção escolhida: ")
                                if sub_opcao in menu.menu_relatorio_vendas:
                                    system("cls")
                                    if sub_opcao == "0":
                                        system("cls")
                                        break
                                    if sub_opcao == "1":
                                        db.historico_vendas.listar_vendas()
                                    elif sub_opcao == "2":
                                        db.historico_vendas.listar_vendas_por_tipo('Carro')
                                    elif sub_opcao == "3":
                                        db.historico_vendas.listar_vendas_por_tipo('Moto')
                                    elif sub_opcao == "4":
                                        db.historico_vendas.listar_vendas_por_tipo('Caminhonete')
                                    input("Pressione qualquer tecla para voltar...")
                                    system("cls")
                                else:
                                    input('Opção inválida')
                                    system("cls")  
                        elif sub_opcao == "3":
                            db.listar_veiculos_disponiveis()
                            input("Pressione qualquer tecla para voltar...")
                            system("cls")
                        elif sub_opcao == "4":
                            db.historico_vendas.listar_vendas()
                            input("Pressione qualquer tecla para voltar...")
                            system("cls")
                        elif sub_opcao == "5":
                            db.historico_vendas.maior_valor_venda()
                            input("Pressione qualquer tecla para voltar...")
                            system("cls")
                        elif sub_opcao == "6":
                            db.historico_vendas.menor_valor_venda()
                            input("Pressione qualquer tecla para voltar...")
                            system("cls")
                    else:        
                        input("Opção inválida - Pressione qualquer tecla para voltar...")
                        system("cls")
        else:
            input("Opção inválida")
            system("cls")
            continue
 