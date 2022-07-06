import os
from re import sub
from entity.menu.menu_principal import Menu_Principal as Menu
from entity.veiculos.cls_veiculos import Veiculos
from entity.veiculos.cls_motoTriciclo import Moto
from entity.veiculos.cls_carro import Carro
from entity.veiculos.cls_caminhonete import Caminhonete

if __name__ == "__main__":
    os.system("cls")
    menu = Menu()
    print(menu.mensagem_inicial)
    while True:
        
        menu.get_menu(menu.menu_principal)
        opcao = input("Escolha uma opção: ")
        if opcao in menu.menu_principal:
            os.system("cls")
            if opcao == "1":
                while True:
                    # menu.get_escolha_veiculo()
                    menu.get_menu(menu.escolha_veiculo)
                    sub_opcao = input("Escolha o tipo de veículo para cadastro: ")
                    if sub_opcao in menu.escolha_veiculo:
                        if sub_opcao == "1":
                            Carro().cadastrar_veiculo()
                        elif sub_opcao == "2":
                            Moto().cadastrar_veiculo()
                        elif sub_opcao == "3":
                            Caminhonete().cadastrar_veiculo()
                        elif sub_opcao == "4":
                            os.system("cls")
                            break
                    else:
                        print("Opção inválida")
            elif opcao == "2":
                Veiculos().listar_todos_veiculos()
            elif opcao == "3":
                Veiculos().alterar_veiculo()
            elif opcao == "4":
                Veiculos().vender_veiculo()
            elif opcao == "5":
                break
            elif opcao == "6":
                break
            elif opcao == "7":
                break
        else:
            print("Opção inválida")
            continue
