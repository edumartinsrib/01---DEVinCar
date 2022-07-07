from os import system
from re import sub

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
                Veiculo().listar_todos_veiculos(db)
                print('\nGostaria de alterar algum veículo? (S/N)')
                while True:
                    menu.get_menu(menu.menu_modificacoes_veiculos)
                    sub_opcao = input("Escolha a opção: ")
                    if sub_opcao in menu.menu_modificacoes_veiculos:
                        if sub_opcao == "1":
                            Veiculo().alterar_veiculo(db)
                        elif sub_opcao == "2":
                            Veiculo().vender_veiculo(db)
                        elif sub_opcao == "3":
                            system("cls")
                            break
            elif opcao == "3":
                ##Veiculo().alterar_veiculo() 
                """ while True:
                    print("Escolha o veículo para edição a partir do: ")
                    Menu().get_menu(menu.menu_edicao_veiculo)
                    opcao = input("Digite a opção desejada: ")
                    if opcao in menu.menu_edicao_veiculo:
            
                        if opcao == "3":
                            system("cls")
                            break
                        
                        sub_opcao = input(
                            f"Digite o {Menu.menu_edicao_veiculo[opcao]} para pesquisa: "
                        )
                        veiculo = db.get_veiculo(
                            Menu.menu_edicao_veiculo[opcao], sub_opcao
                        )
                        if veiculo:
                            while True:
                                novo_valor = input(
                                    f"Digite o novo valor para o {veiculo['tipo_veiculo']}: "
                                )
                                try:
                                    novo_valor = float(novo_valor)
                                    veiculo.valor = novo_valor
                                    break
                                except ValueError:
                                    print("Valor inválido")
                                
                                exibe_cores_disponiveis() 
                                cor_escolhida = int(input("Escolha a opção de cor disponível para o veiculo: "))
                            
                                if cor_escolhida in self.cores_disponiveis:
                                    veiculo.cor = self.cores_disponiveis[cor_escolhida]
                                    break
                                
                            system("cls")
                        else:    
                            print("Veículo não encontrado")
                    else:
                        print("Opção inválida") """
            
                    
            elif opcao == "4":
                """ while True:
                    print("Escolha o veículo para venda a partir do: ")
                    Menu().get_menu(menu.menu_edicao_veiculo)
                    opcao = input("Digite a opção desejada: ")
                    if opcao in menu.menu_edicao_veiculo:
                        sub_opcao = input(
                            f"Digite o {Menu.menu_edicao_veiculo[opcao]} para pesquisa: "
                        )
                        if db.verifica_existencia_veiculo(
                            Menu.menu_edicao_veiculo[opcao], sub_opcao
                        ):
                            cpf_comprador = Validacoes.valida_cpf()
                            db.vender_veiculo(
                                Menu.menu_edicao_veiculo[opcao], sub_opcao, cpf_comprador
                            )
                        else:
                            print("Veículo não encontrado")

                    else:
                        print("Opção inválida") """
                    
            elif opcao == "5":
                break
            elif opcao == "6":
                break
            elif opcao == "7":
                break
        else:
            print("Opção inválida")
            continue
 