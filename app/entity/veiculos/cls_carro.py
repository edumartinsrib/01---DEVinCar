from .cls_veiculos import Veiculos

class Carro(Veiculos):
    opt_combustivel = {
        1: "Somente Gasolina",
        2: "Flex",
    }
    tipo_veiculo = 'Carro'
    
    def __init__(self):
        super().__init__()
        self.combustivel: str = None
        self.qtd_portas: int = None
        self.potencia: int = None

    def cadastrar_veiculo(self):
        super().cadastrar_veiculo(Carro.tipo_veiculo)
        while True:
            self.escolher_combustivel()
            opcao = int(input("Escolha a opção de combustivel para o veículo: "))
            if opcao in self.opt_combustivel.keys():
                self.combustivel = self.opt_combustivel[opcao]
                break
        self.potencia = int(input("Digite a potencia (CV): "))
        self.qtd_portas = int(input("Digite a quantidade de portas: "))
        super().salvar_veiculo()
        print("Veiculo cadastrado com sucesso!")

    def escolher_combustivel(self):
        for combustivel in self.opt_combustivel:
            print(f"{combustivel} - {self.opt_combustivel[combustivel]}")
