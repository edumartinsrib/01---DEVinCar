from pathlib import Path
from sys import path
from os import system
from modules import *

path.append(str(Path.cwd()))

""" def carrega_classes_inicial():
        dados = db.all()
        veiculos = []
        
        for dado in dados:
            if dado['tipo'] == 'carro':
                veiculos.append(Carro.carregamento_inicial(dado['numero_chassi'], dado['data_fabricacao'], dado['nome'], 
                                                                         dado['placa'], dado['valor'], dado['cpf_comprador'], dado['cor'], 
                                                                         dado['data_atual'], dado['potencia'], dado['qtd_rodas'], dado['combustivel']))
            elif dado['tipo'] == 'moto':
                veiculos.append(Moto.carregamento_inicial(dado['numero_chassi'], dado['data_fabricacao'], dado['nome'], 
                                                                         dado['placa'], dado['valor'], dado['cpf_comprador'], dado['cor'], 
                                                                         dado['data_atual'], dado['potencia'], dado['qtd_rodas']))
            elif dado['tipo'] == 'caminhonete':
                veiculos.append(Caminhonete.carregamento_inicial(dado['numero_chassi'], dado['data_fabricacao'], dado['nome'], 
                                                                         dado['placa'], dado['valor'], dado['cpf_comprador'], dado['cor'], 
                                                                         dado['data_atual'], dado['potencia'], dado['qtd_portas'], dado['combustivel'], 
                                                                         dado['capacidade_carregamento']))
        
carrega_classes_inicial()     """    

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
