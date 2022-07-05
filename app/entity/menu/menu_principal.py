class Menu_Principal:
    mensagem_inicial = '''
        
    '''
    def __init__(self):
        self.__menu_principal = {
            '1': 'Cadastrar novo veículo',
            '2': 'Listar veículos fabricados',
            '3': 'Alterar informações veículo',
            '4': 'Vender veículo',
            '5': 'Acessar Relatórios',
            '6': 'Sair'
        }
        self.__menu_relatorios = {
            '1': 'Relatório de veículos',
            '2': 'Relatório de vendas',
            '3': 'Carros disponíveis',
            '4': 'Carros vendidos',
            '5': 'Carros vendidos com maior preço',
            '6': 'Carros vendidos com menor preço',
            '7': 'Voltar'
        }
        self._menu_relatorio_veiculos = {
            '1': 'Listar todos os veículos',
            '2': 'Motos - Triciclos',
            '3': 'Carros',
            '4': 'Camionetes',
            '5': 'Voltar'
        }
        self._menu_relatorio_vendas = {
            '1': 'Listar todas as vendas',
            '2': 'Vendas por mês',
            '3': 'Vendas por ano',
            '4': 'Voltar'
        }
        self._menu_relatorio_carros_disponiveis = {
            '1': 'Listar todos os carros disponíveis',
            '2': 'Carros disponíveis por tipo de automóvel',
            '3': 'Carros disponíveis por faixa de preço',
            '4': 'Voltar'
        }
        self._menu_relatorio_carros_vendidos = {
            '1': 'Listar todos os carros vendidos',
            '2': 'Carros vendidos por tipo de automóvel',
            '3': 'Carros vendidos por faixa de preço',
            '4': 'Voltar'
        }
    
    @property
    def menu_principal(self):
        return self.__menu_principal
    
    def get_menu_principal(self):
        for key, value in self.__menu_principal.items():
            print(f'{key} - {value}')
            
    def get_menu_relatorios(self):
        for key, value in self.__menu_relatorios.items():
            print(f'{key} - {value}')
    
    def get_menu_relatorio_veiculos(self):
        for key, value in self._menu_relatorio_veiculos.items():
            print(f'{key} - {value}')
    
    def get_menu_relatorio_vendas(self):
        for key, value in self._menu_relatorio_vendas.items():
            print(f'{key} - {value}')
            
    def get_menu_relatorio_carros_disponiveis(self):
        for key, value in self._menu_relatorio_carros_disponiveis.items():
            print(f'{key} - {value}')
    
    def get_menu_relatorio_carros_vendidos(self):
        for key, value in self._menu_relatorio_carros_vendidos.items():
            print(f'{key} - {value}')
    
    