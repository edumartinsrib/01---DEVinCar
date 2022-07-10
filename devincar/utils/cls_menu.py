from os import system
from time import sleep

from rich.progress import track


class MenuPrincipal:
    mensagem_inicial = """
    
██████╗ ███████╗██╗   ██╗██╗███╗   ██╗ ██████╗ █████╗ ██████╗ 
██╔══██╗██╔════╝██║   ██║██║████╗  ██║██╔════╝██╔══██╗██╔══██╗
██║  ██║█████╗  ██║   ██║██║██╔██╗ ██║██║     ███████║██████╔╝
██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║╚██╗██║██║     ██╔══██║██╔══██╗
██████╔╝███████╗ ╚████╔╝ ██║██║ ╚████║╚██████╗██║  ██║██║  ██║
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                              
_____________________________________________________________________
"""
    menu_principal = {
        "0": "Sair",
        "1": "Cadastrar novo veículo",
        "2": "Listar veículos fabricados",
        "3": "Alterar informações veículo",
        "4": "Vender veículo",
        "5": "Acessar Relatórios",

    }
    escolha_tipo_informacao = {
        "1": "Tipo de veículo",
        "2": "Nome (Modelo)",
        "3": "Chassi",
        "4": "Placa",
    }
    escolha_veiculo = {
        "0": "Voltar",
        "1": "Carro",
        "2": "Moto/Triciclo",
        "3": "Caminhonete",

    }
    menu_relatorios = {
        "0": "Voltar",
        "1": "Relatório de veiculos disponíveis",
        "2": "Relatório de veiculos vendidos",
    }
    menu_relatorio_veiculos = {
        "0": "Voltar",
        "1": "Listar todos os veículos",
        "2": "Carros",
        "3": "Moto/Triciclos",
        "4": "Caminhonetes",
    }
    menu_relatorio_vendas = {
        "0": "Voltar",
        "1": "Listar todas as vendas",
        "2": "Listar vendas de Carros",
        "3": "Listar vendas de Motos",
        "4": "listar vendas de Caminhonetes",
        "5": "Listar venda de MAIOR valor",
        "6": "Listar venda de MENOR valor",

    }
    menu_modificacoes_veiculos = {
        "0": "Voltar",
        "1": "Alterar a cor do veículo",
        "2": "Alterar o valor do veículo",
    }

    estilos_dados = {
        'erro': '[bold red]',
        'sucesso': '[bold green]',
        'info': '[bold blue]',
    }

    @staticmethod
    def get_menu(menu):
        for key, value in menu.items():
            print(f"{key} - {value}".ljust(100))

    @staticmethod
    def limpar_menu(console, tipo=0, texto=0, estilo=0):
        if tipo == 'input':
            console.input(f"{MenuPrincipal.estilos_dados[estilo]}{texto}")
        elif tipo == 'print' and texto != "":
            console.print(f"{MenuPrincipal.estilos_dados[estilo]}{texto}")

        try:
            system("cls")
        except:
            system("clear")

    @staticmethod
    def barra_progresso(texto):
        for _ in track(range(100), description=f'[cyan] {texto}'):
            sleep(0.02)
        return True
