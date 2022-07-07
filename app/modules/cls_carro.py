from cls_veiculos import Veiculos

class Carro(Veiculos):
    opt_combustivel = {
        1: "Somente Gasolina",
        2: "Flex",
    }
    tipo_veiculo = 'Carro'
    
    def __init__(self):
        super().__init__()
        self.tipo_veiculo = self.__class__.__name__
        self.combustivel: str = None
        self.qtd_portas: int = None
        self.potencia: int = None

    def cadastrar_veiculo(self):
        super().cadastrar_veiculo()
        self.escolher_combustivel()
        self.potencia = int(input("Digite a potencia (CV): "))
        self.qtd_portas = int(input("Digite a quantidade de portas (litros): "))
        super().salvar_veiculo()
        print("Veiculo cadastrado com sucesso!")

    def escolher_combustivel(self):
        for combustivel in self.opt_combustivel:
            print(f"{combustivel} - {self.opt_combustivel[combustivel]}")
            
        while True:
            opcao = int(input("Escolha a opção de combustivel para o veículo: "))
            if opcao in self.opt_combustivel.keys():
                self.combustivel = self.opt_combustivel[opcao]
                break
            
    def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual, potencia, qtd_portas, combustivel):
          tipo_veiculo = self.__class__.__name__
          super().carregamento_inicial(tipo_veiculo, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual)
          self.potencia = potencia
          self.qtd_portas = qtd_portas
          self.combustivel = combustivel