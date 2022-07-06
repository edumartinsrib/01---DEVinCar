from uuid import uuid4
from datetime import datetime

class Veiculos:
    cores_disponiveis = {
        1: 'Azul',
        2: 'Amarelo',
        3: 'Vermelho',
        4: 'Verde',
        5: 'Preto',
        6: 'Branco',
        7: 'roxo',
    }
    
    tipos_veiculos = {
        1: 'Carro',
        2: 'Moto',
        3: 'Caminhonete',
    }
    
    def __init__(self):
        self.tipo_veiculo = None
        self.numero_chassi: str = uuid4().fields[-1].to_bytes(5, 'big').hex()
        self.data_fabricacao: str = None
        self.nome: str = None
        self.placa: str = None
        self.valor: int = None
        self.cpf_comprador: int = 0
        self.cor: str = None
        self.data_atual: str = datetime.now().strftime('%d/%m/%Y')
       
    def cadastrar_veiculo(self, tipo_veiculo):
        print(f"Cadastrando {tipo_veiculo}")
        self.tipo_veiculo = tipo_veiculo 
        self.nome = input("Digite o nome (modelo) do veiculo: ")
        self.placa = input("Digite a placa do veiculo: ")
        self.valor = int(input("Digite o valor do veiculo: "))
        while True:
            self.exibe_cores_disponiveis(tipo_veiculo)
            if tipo_veiculo == 'Caminhonete':
                self.cor = 'Roxa'
                break
                
            cor_escolhida = int(input("Digite a cor para o veiculo: "))
            if cor_escolhida in self.cores_disponiveis:
                self.cor = self.cores_disponiveis[cor_escolhida]
                break
            else:
                print('Opção inválida')
    
        self.data_fabricacao = input("Digite a data de fabricação do veiculo: ")
    
    def exibe_cores_disponiveis(self, tipo_veiculo):
        if tipo_veiculo == 'Caminhonete':
            return 'Este veiculo está disponível apenas na cor Roxa'

        for cor in self.cores_disponiveis:
            print(f"{cor} - {self.cores_disponiveis[cor]}")
            
    # alterar informações de veículo
    def alterar_veiculo(self, tipo_veiculo):
        print(f"Alterando informações do veículo {self.nome}")
        self.valor = int(input("Digite o valor do veiculo: "))
        while True:
            self.exibe_cores_disponiveis(tipo_veiculo)
            if tipo_veiculo == 'Caminhonete':
                self.cor = 'Roxa'
                break
                
            cor_escolhida = int(input("Digite a cor para o veiculo: "))
            if cor_escolhida in self.cores_disponiveis:
                self.cor = self.cores_disponiveis[cor_escolhida]
                break
            else:
                print('Opção inválida')
                
        print("Veiculo alterado com sucesso!")
        
    



