from uuid import uuid4

class Veiculos:
    def __init__(self):
        self.tipo_veiculo = None
        self.numero_chassi: str = uuid4()
        self.data_fabricao: str = None
        self.nome: str = None
        self.placa: str = None
        self.valor: int = None
        self.cpf_comprador: str = None
        self.cor: str = None
       
    def cadastrar_veiculo(self, tipo_veiculo):
        print(f"Cadastrando {tipo_veiculo}")
        self.tipo_veiculo = tipo_veiculo 
        self.nome = input("Digite o nome do veiculo: ")
        self.placa = input("Digite a placa do veiculo: ")
        self.valor = int(input("Digite o valor do veiculo: "))
        self.cpf_comprador = input("Digite o cpf do comprador: ")
        self.cor = input("Digite a cor do veiculo: ")
        self.potencia = int(input("Digite a potencia do veiculo: "))
        self.qtd_rodas = int(input("Digite a quantidade de rodas do veiculo: "))
        self.data_fabricao = input("Digite a data de fabricação do veiculo: ")
        print("Veiculo cadastrado com sucesso")

class Moto(Veiculos):
        def __init__(self):
             super().__init__()
             self.potencia: int = None
             self.qtd_rodas: int = None
             
           
class Carro(Veiculos):
        def __init__(self):
             super().__init__()
             self.combustivel: str = None
             self.qtd_portas: int = None
             self.potencia: int = None
             
             
class Caminhonete(Veiculos): 
        def __init__(self):
             super().__init__()
             self.potencia: int = None
             self.qtd_rodas: int = None
             self.combustivel: str = None
             self.capacidade_carregamento: int = None
             

if __name__ == "__main__":
    print("Bem vindo ao sistema de veículos da empresa:")
    print("""" 
██████╗ ███████╗██╗   ██╗██╗███╗   ██╗ ██████╗ █████╗ ██████╗ 
██╔══██╗██╔════╝██║   ██║██║████╗  ██║██╔════╝██╔══██╗██╔══██╗
██║  ██║█████╗  ██║   ██║██║██╔██╗ ██║██║     ███████║██████╔╝
██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║╚██╗██║██║     ██╔══██║██╔══██╗
██████╔╝███████╗ ╚████╔╝ ██║██║ ╚████║╚██████╗██║  ██║██║  ██║
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                              
 """)
    


