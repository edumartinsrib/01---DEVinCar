from .cls_veiculos import Veiculos


class Caminhonete(Veiculos):

    opt_combustivel = {
        1: "Gasolina",
        2: "Diesel",
    }
    
    tipo_veiculo = 'Caminhonete'

    def __init__(self):
        super().__init__()
        self.potencia: int = None
        self.qtd_rodas: int = None
        self.combustivel: str = None
        self.capacidade_carregamento: float = None

    def cadastrar_veiculo(self):
        super().cadastrar_veiculo(Caminhonete.tipo_veiculo)
        self.potencia = int(input("Digite a potencia do veiculo: "))
        self.qtd_rodas = int(input("Digite a quantidade de rodas do veiculo: "))
        while True:
            self.escolher_combustivel()
            opcao = int(input("Escolha a opção de combustivel para o veículo: "))
            if opcao in self.opt_combustivel.keys():
                self.combustivel = self.opt_combustivel[opcao]
                break
        self.capacidade_carregamento = float(input("Digite a capacidade de carregamento do veiculo: "))
        super().salvar_veiculo()
        print("Veiculo cadastrado com sucesso!")

    def escolher_combustivel(self):
        for combustivel in self.opt_combustivel:
            print(f"{combustivel} - {self.opt_combustivel[combustivel]}")
