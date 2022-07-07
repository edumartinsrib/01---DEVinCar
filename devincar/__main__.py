from os import system
from devincar.modules.cls_validacoes import Validacoes
from modules import *

db = Database()
menu = Menu()
db.carrega_classes_inicial()

if __name__ == "__main__":
    system("cls")
    print("Bem vindo ao sistema de gerenciamento de veículos da concessionária.")
    while True:
        print(menu.mensagem_inicial)
        menu.get_menu(menu.menu_principal)
        opcao = input("Escolha uma opção: ")
        if opcao in menu.menu_principal:
            system("cls")
            if opcao == "1":
                while True:
                    menu.get_menu(menu.escolha_veiculo)
                    sub_opcao = input("Escolha o tipo de veículo para cadastro: ")
                    if sub_opcao in menu.escolha_veiculo:
                        if sub_opcao == "1":
                            Carro().cadastrar_veiculo(db)
                        elif sub_opcao == "2":
                            Moto().cadastrar_veiculo(db)
                        elif sub_opcao == "3":
                            Caminhonete().cadastrar_veiculo(db)
                        elif sub_opcao == "4":
                            system("cls")
                            break
                    else:
                        print("Opção inválida")
            elif opcao == "2":
                while True:
                    print('Escolha o tipo de veículo para listagem:')
                    menu.get_menu(menu.menu_relatorio_veiculos)
                    sub_opcao = input("Digite a opção escolhida: ")
                    if sub_opcao in menu.menu_relatorio_veiculos:
                        system("cls")
                        if sub_opcao == "1":
                            db.listar_todos_veiculos()
                        elif sub_opcao == "2":
                            Carro().listar_veiculos(db)
                        elif sub_opcao == "3":
                            Moto().listar_veiculos(db)
                        elif sub_opcao == "4":
                            Caminhonete().listar_veiculos(db)
                        elif sub_opcao == "5":
                            system("cls")
                            break
                        input("Pressione qualquer tecla para voltar...")
                        system("cls")
                    else:
                         input('Opção inválida')
                         system("cls")  
            elif opcao == "3":
                while True:
                    print("Digite a placa do veículo que deseja alterar:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                    placa = input("Placa: ").upper()
                    
                    if placa == "":
                        system("cls")
                        break
                    
                    if placa == "LISTAR":
                        print(f"Listando todos os veiculos disponíveis".center(50, "-"))
                        db.listar_veiculos_disponiveis()
                        placa = input("Placa: ").upper()
                        
                    veiculo_existe = db.verifica_existencia_veiculo('placa', placa)
                    veiculo_disponivel = db.verifica_disponibilidade_veiculo(placa)
                    
                    if  veiculo_existe == True and veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        print(f"Escolha a opção que deseja alterar - a cor atual do veículo é ({veiculo.cor}) e o valor atual é ({veiculo.valor}): ")
                        menu.get_menu(menu.menu_modificacoes_veiculos)
                        opcao = input("Digite a opção desejada: ")
                        if opcao in menu.menu_modificacoes_veiculos:
                            if opcao == "1":
                                veiculo.alterar_veiculo(db, 'cor')
                                break
                            elif opcao == "2":
                                veiculo.alterar_veiculo(db, 'valor')
                                break
                            elif opcao == "3":
                                system("cls")
                                break
                        else:
                            print("Opção inválida")
                    else:    
                        input("Digite qualquer tecla para continuar...")
                        system("cls")

            elif opcao == "4":
                print("Digite a placa do veículo que deseja vender:\nOu digite 'LISTAR' para exibir todos os veiculos ou ENTER para voltar")
                placa = input("Placa: ").upper()
                    
                if placa == "":
                   system("cls")
                   break
                    
                if placa == "LISTAR":
                    print(f"Listando todos os veiculos disponíveis".center(50, "-"))
                    db.listar_veiculos_disponiveis()
                    input("Pressione qualquer tecla para continuar...")
                    placa = input("Placa: ").upper()
                    
                veiculo_existe = db.verifica_existencia_veiculo('placa', placa)
                veiculo_disponivel = db.verifica_disponibilidade_veiculo(placa)
                
                if  veiculo_existe == True and veiculo_disponivel == True:
                        veiculo = db.get_veiculo(placa_veiculo=placa)
                        veiculo.vender_veiculo(db)
                else:
                    input("Pressione qualquer tecla para continuar...")
                    system("cls")
                    
            elif opcao == "5":
                break
            elif opcao == "6":
                break
            elif opcao == "7":
                break
        else:
            input("Opção inválida")
            system("cls")
            continue
 