from abc import ABC, abstractmethod

class Veiculo(ABC):
    veiculos = []
    
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        Veiculo.veiculos.append(self)
        
    def __str__(self):
        return f'{self._marca} | {self._modelo}'
            
    @classmethod
    def listar(cls):
        for v in cls.veiculos:
            print(f'{v}')


