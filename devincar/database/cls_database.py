from re import M
from tinydb import TinyDB, Query
from pathlib import Path
from rich import print as rprint

from ..modules.cls_veiculos import *
from ..modules.cls_caminhonete import *
from ..modules.cls_carro import *
from ..modules.cls_moto import *
from .cls_historico_vendas import *

class Database:
    caminho_banco = Path() / 'data'
    field_names = ['chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor', 'status']
    values = ['numero_chassi', 'tipo_veiculo', 'nome', 'data_fabricacao', 'placa', 'valor']
    
    def __init__(self):
        self.dados_externos = TinyDB(self.caminho_banco / 'database.json')
        self.dados_local = []
        self.historico_vendas = HistoricoVendas()
    
    def carrega_classes_inicial(self):
        for dado in self.dados_externos.all():
            if dado['tipo_veiculo'] == 'Carro':
                novo_carro = Carro()
                novo_carro.carregamento_inicial(numero_chassi=dado['numero_chassi'],
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
                self.dados_local.append(novo_carro)
            elif dado['tipo_veiculo'] == 'Moto':
                novo_moto = Moto()
                novo_moto.carregamento_inicial(numero_chassi = dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_rodas=dado['qtd_rodas'])
                self.dados_local.append(novo_moto)
            elif dado['tipo_veiculo'] == 'Caminhonete':
                novo_caminhonete = Caminhonete()
                novo_caminhonete.carregamento_inicial(numero_chassi = dado['numero_chassi'],
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
                self.dados_local.append(novo_caminhonete)
    
    def retorna_dados_local(self):
        return self.dados_local
    
    def salvar_veiculo(self, veiculo):
        self.dados_local.append(veiculo)
        self.dados_externos.insert(veiculo.__dict__)
        input("\nVeículo salvo com sucesso - pressione qualquer tecla para continuar...")
        system('cls')
    
    def atualizar_veiculo(self, veiculo):
        try:
            for veiculo_salvo in self.dados_local:
                if veiculo_salvo.placa == veiculo.placa:
                    veiculo_salvo = veiculo
                    self.dados_externos.update(veiculo.__dict__, Query().placa == veiculo.placa)
                    input("\nVeículo alterado com sucesso - pressione qualquer tecla para continuar...")
                    system('cls')
                    return True
        except Exception as e:
            print(e)
            return False
    
    def vender_veiculo(self, veiculo):
        for veiculo_salvo in self.dados_local:
            if veiculo_salvo.placa == veiculo.placa:
                veiculo_salvo = veiculo
                self.dados_externos.update({'cpf_comprador': veiculo.cpf_comprador}, Query()['placa'] == veiculo.placa)
                self.historico_vendas.adicionar_venda(veiculo)
                
    def listar_todos_veiculos(self):
        titulo_tabela = "Todos os Veículos"
        for veiculo in self.dados_local:
            if veiculo.cpf_comprador != 0:
                status = 'Vendido'
            else:
                status = 'Disponível'
            self.montar_tabela(titulo_tabela, veiculo, status)

    
    def listar_veiculos_disponiveis(self):
        my_table = PrettyTable()
        my_table.field_names = self.field_names
        for veiculo in self.dados_local:
            if veiculo.cpf_comprador == 0:
                status = 'Disponível'
                my_table.add_row([veiculo.numero_chassi, veiculo.tipo_veiculo, veiculo.nome, veiculo.data_fabricacao, veiculo.placa, veiculo.valor, status])
        rprint(my_table)
        
    def listar_veiculos_por_tipo(self, tipo_veiculo):
        my_table = PrettyTable()
        my_table.field_names = self.field_names
        for veiculo in self.dados_local:
            if veiculo.tipo_veiculo == tipo_veiculo:
                if veiculo.cpf_comprador != 0:
                    status = 'Vendido'
                else:
                    status = 'Disponível'
                    
                my_table.add_row([veiculo.numero_chassi, veiculo.tipo_veiculo, veiculo.nome, veiculo.data_fabricacao, veiculo.placa, veiculo.valor, status])
        rprint(my_table)
        
    def verifica_existencia_veiculo(self, key, valor):
        if self.dados_externos.contains(Query()[key] == valor) == True:
            return True
        return False

    def verifica_disponibilidade_veiculo(self, placa):
        for veiculo in self.dados_local:
            if veiculo.placa == placa and veiculo.cpf_comprador == 0:
                return True
        rprint("\nVeículo não disponível!")
        return False
    
    def verifica_existencia_veiculo_por_placa(self, placa):
        for veiculo in self.dados_local:
            if veiculo.placa == placa:
                return True
        return False
    
    def get_veiculo(self, placa_veiculo):
        for veiculo in self.dados_local:
            if veiculo.placa == placa_veiculo:
                return veiculo
        return None


    
        
