from entity.menu.menu_principal import Menu_Principal
from entity.veiculos.cls_motoTriciclo import Moto


while True:
    
    menu = Menu_Principal()
    menu.get_menu_principal()
    opcao = input('Escolha uma opção: ')
    if opcao in menu.menu_principal:
        if opcao == '1':
            moto = Moto()
            moto.cadastrar_veiculo('moto')
            print(moto)
        elif opcao == '2':
            break
        elif opcao == '3':
            break
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
    
  