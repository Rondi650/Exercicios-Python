from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, tamanho):
        super().__init__(marca, modelo)
        self._tamanho = tamanho

    def __str__(self):
        return f'{super().__str__()} | {self._tamanho}'
