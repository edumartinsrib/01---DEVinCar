from os import system
from prettytable import PrettyTable
from tinydb import TinyDB, Query
from rich import print as rprint
from modules import *
from utils import Tables as PersonalTable
from .cls_historico_vendas import HistoricoVendas

class Database:
    def __init__(self):
        self.dados_externos = TinyDB('database.json')
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
            elif dado['tipo_veiculo'] == 'Moto/Triciclo':
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
                
    def listar_veiculos_por_tipo(self, tipo_veiculo):
        if tipo_veiculo == 'todos':
            campos = Veiculo().campos_relatorio
            valores = []
            valores.append = [veiculo.__dict__ for veiculo in self.dados_local]
            
        elif tipo_veiculo == 'Carro':
            campos = Carro().campos_relatorio
            valores = []
            valores.append = [veiculo.__dict__ for veiculo in self.dados_local if veiculo.tipo_veiculo == 'Carro']

        elif tipo_veiculo == 'Moto/Triciclo':
            campos = Moto().campos_relatorio
            valores = []
            valores.append = [veiculo.__dict__ for veiculo in self.dados_local if veiculo.tipo_veiculo == 'Carro']

        elif tipo_veiculo == 'Caminhonete':
            campos = Caminhonete().campos_relatorio
            valores = []
            valores.append = [veiculo.__dict__ for veiculo in self.dados_local if veiculo.tipo_veiculo == 'Carro']
            
        PersonalTable().monta_tabela(titulo=f'Lista de {campos.__class__.__name__}', campos=campos, valores=valores)
        
        
    def listar_veiculos_disponiveis(self):
        my_table = PrettyTable()
        my_table.field_names = self.field_names
        for veiculo in self.dados_local:
            if veiculo.cpf_comprador == 0:
                status = 'Disponível'
                my_table.add_row([veiculo.numero_chassi, veiculo.tipo_veiculo, veiculo.nome, veiculo.data_fabricacao, veiculo.placa, veiculo.valor, status])
        rprint(my_table)
        
        
    def verifica_existencia_veiculo(self, key, valor):
        if self.dados_externos.contains(Query()[key] == valor) == True:
            return True
        return False
    
    def verifica_existencia_veiculo_por_placa(self, placa):
        for veiculo in self.dados_local:
            if veiculo.placa == placa:
                return True
        return False

    def verifica_disponibilidade_veiculo(self, placa):
        for veiculo in self.dados_local:
            if veiculo.placa == placa and veiculo.cpf_comprador == 0:
                return True
        rprint("\nVeículo não disponível!")
        return False
    
    def get_veiculo(self, placa_veiculo):
        for veiculo in self.dados_local:
            if veiculo.placa == placa_veiculo:
                return veiculo
        return None


    
        
