from .cls_caminhonete import Caminhonete
from .cls_carro import Carro
from .cls_motoTriciclo import Moto
from .cls_veiculos import Veiculos
from .cls_menu import Menu_Principal as Menu
from .cls_validacoes import Validacoes


menu = Menu()

menu.get_menu(menu.menu_principal)
__all__ = ['Caminhonete', 'Carro', 'Moto', 'Veiculos', 'Menu', 'Validacoes']