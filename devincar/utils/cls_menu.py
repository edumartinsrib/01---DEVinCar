
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
        "1": "Relatório de veículos",
        "2": "Relatório de vendas",
        "3": "Veículos disponíveis",
        "4": "Veículos vendidos",
        "5": "Veículos vendidos com maior preço",
        "6": "Veículos vendidos com menor preço",
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
        "2": "Listar vendas de carros",
        "3": "Listar vendas de motos",
	    "4": "listar vendas de caminhonetes"
    }
    menu_relatorio_carros_disponiveis = {
        "0": "Voltar",
        "1": "Listar todos os carros disponíveis",
        "2": "Veículos disponíveis por tipo de automóvel",
        "3": "Veículos disponíveis por faixa de preço",
    }
    menu_relatorio_carros_vendidos = {
        "0": "Voltar",
        "1": "Listar todos os carros vendidos",
        "2": "Veículos vendidos por tipo de automóvel",
        "3": "Veículos vendidos por faixa de preço",
    }
    menu_modificacoes_veiculos = {
        "0": "Voltar",
        "1": "Alterar a cor do veículo",
        "2": "Alterar o valor do veículo",
    }
    @staticmethod
    def get_menu(menu):
        for key, value in menu.items():
            print(f"{key} - {value}".ljust(100))

