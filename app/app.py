import os
from entity.menu.menu_principal import Menu_Principal
from entity.veiculos.cls_veiculos import Veiculos
from entity.veiculos.cls_motoTriciclo import Moto
from entity.veiculos.cls_carro import Carro
from entity.veiculos.cls_caminhonete import Caminhonete
from data.database import Database as db
##comando cls para limpar a tela

if __name__ == '__main__':
    os.system('cls')
    while True:
        database = db()
        menu = Menu_Principal()
        menu.get_menu(menu.menu_principal)
        opcao = input('Escolha uma opção: ')
        if opcao in menu.menu_principal:
            if opcao == '1':
                while True:
                    #menu.get_escolha_veiculo()
                    menu.get_menu(menu.escolha_veiculo)
                    opcao = input('Escolha o tipo de veículo para cadastro: ')
                    if opcao in menu.escolha_veiculo:
                        if opcao == '1':
                            carro = Carro()
                            carro.cadastrar_veiculo('Carro')
                            database.salvar_veiculo(carro)
                            break
                        elif opcao == '2':
                            moto = Moto()
                            moto.cadastrar_veiculo('Moto/Triciclo')
                            database.salvar_veiculo(moto)
                            break
                        elif opcao == '3':
                            caminhonete = Caminhonete()
                            caminhonete.cadastrar_veiculo('Caminhonete')
                            database.salvar_veiculo(caminhonete)
                            break
                        elif opcao == '4':
                            os.system('cls')
                            break  
                    else:
                        print('Opção inválida')
            elif opcao == '2':
                database.listar_todos_veiculos_menu()
            elif opcao == '3':
                ## pesquisar veículo para alteração
                while True:
                    database.listar_todos_veiculos_menu()
                    opcao_chassi = input('Escolha o veiculo para editar (utilizar numero do chassi): ')
                    veiculo = database.show_veiculo(opcao_chassi)
                    if veiculo != 'Veiculo não encontrado':
                        while True:
                            menu.get_menu(menu.menu_modificacoes_veiculos)
                            opcao_modificacao = input('Escolha uma opção: ')
                           
                
                    
            elif opcao == '4':
                break
            elif opcao == '5':
                break
            elif opcao == '6':
                break
            elif opcao == '7':
                break
        else :
            print('Opção inválida')
            continue
        
  