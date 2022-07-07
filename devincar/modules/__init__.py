from .database import Database as db
from .cls_menu import Menu_Principal as Menu
from .cls_veiculos import Veiculos as Veiculo
from .cls_caminhonete import Caminhonete as Caminhonete
from .cls_moto import Moto as Moto
from .cls_carro import Carro as Carro



__all__ = [
    'db', 
    'Menu',
    'Veiculo',
    'Caminhonete',
    'Moto',
    'Carro'
]

