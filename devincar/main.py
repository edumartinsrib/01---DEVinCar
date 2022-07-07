from os import system

from modules import *

def carrega_classes_inicial():
        dados = db.get_db()
        veiculos = []
        
        for dado in dados:
            if dado['tipo_veiculo'] == 'Carro':
                novo_carro = Carro()
                Carro().carregamento_inicial(numero_chassi = dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_portas=dado['qtd_portas'],
                                                           combustivel=dado['combustivel'])
                veiculos.append(novo_carro)
            elif dado['tipo_veiculo'] == 'Moto':
                novo_moto = Moto()
                Moto().carregamento_inicial(numero_chassi = dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_rodas=dado['qtd_rodas'])
                veiculos.append(novo_moto)
            elif dado['tipo_veiculo'] == 'Caminhonete':
                novo_caminhonete = Caminhonete()
                Caminhonete().carregamento_inicial(numero_chassi = dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_portas=dado['qtd_portas'],
                                                           combustivel=dado['combustivel'],
                                                           capacidade_carregamento=dado['capacidade_carregamento'])
                veiculos.append(novo_caminhonete)
            
        for veiculo in veiculos:
            print(veiculo)
            


carrega_classes_inicial()        
""" 
if __name__ == "__main__":
    system("cls")
    menu = Menu()
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
                            Carro().cadastrar_veiculo()
                        elif sub_opcao == "2":
                            Moto().cadastrar_veiculo()
                        elif sub_opcao == "3":
                            Caminhonete().cadastrar_veiculo()
                        elif sub_opcao == "4":
                            system("cls")
                            break
                    else:
                        print("Opção inválida")
            elif opcao == "2":
                Veiculo().listar_todos_veiculos()
            elif opcao == "3":
                 while True:
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
                                
                                self.exibe_cores_disponiveis() 
                                cor_escolhida = int(input("Escolha a opção de cor disponível para o veiculo: "))
                            
                                if cor_escolhida in self.cores_disponiveis:
                                    veiculo.cor = self.cores_disponiveis[cor_escolhida]
                                    break
                                
                            system("cls")
                        else:    
                            print("Veículo não encontrado")
                    else:
                        print("Opção inválida")
                    Veiculo().alterar_veiculo()
                    
            elif opcao == "4":
                while True:
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
                        print("Opção inválida")
                    
            elif opcao == "5":
                break
            elif opcao == "6":
                break
            elif opcao == "7":
                break
        else:
            print("Opção inválida")
            continue
 """