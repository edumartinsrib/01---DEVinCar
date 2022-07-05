from uuid import uuid4

class Veiculos:
    cores_disponiveis = ['vermelho', 'azul', 'verde', 'branco', 'preto', 'roxo']

    def __init__(self):
        self.tipo_veiculo = None
        self.numero_chassi: str = uuid4()
        self.data_fabricao: str = None
        self.nome: str = None
        self.placa: str = None
        self.valor: int = None
        self.cpf_comprador: int = 0
        self.cor: str = None
       
    def cadastrar_veiculo(self, tipo_veiculo):
        print(f"Cadastrando {tipo_veiculo}")
        self.tipo_veiculo = tipo_veiculo 
        self.nome = input("Digite o nome (modelo) do veiculo: ")
        self.placa = input("Digite a placa do veiculo: ")
        self.valor = int(input("Digite o valor do veiculo: "))
        self.cor = input("Digite a cor do veiculo: ")
        self.data_fabricao = input("Digite a data de fabricação do veiculo: ")
    
    def __str__(self):
        return f"{self.tipo_veiculo} \n {self.nome} \n {self.placa} \n {self.valor} \n {self.cor} \n {self.data_fabricao}"

    


