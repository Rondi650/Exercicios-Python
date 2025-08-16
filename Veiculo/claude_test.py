from abc import ABC, abstractmethod

class Veiculo(ABC):
    veiculos = []
    
    def __init__(self, marca, modelo):
        print(f">>> Executando Veiculo.__init__ para {marca} {modelo}")
        self._marca = marca
        self._modelo = modelo
        print(f">>> Fazendo append do objeto na lista...")
        Veiculo.veiculos.append(self)
        print(f">>> Append concluído. Lista agora tem {len(Veiculo.veiculos)} itens")
        print(f">>> Nenhum __str__ foi chamado ainda!\n")
        
    def __str__(self):
        print(f"*** CHAMOU Veiculo.__str__() ***")
        return f'{self._marca} | {self._modelo}'      
        
    @classmethod
    def listar(cls):
        print("=== INICIANDO LISTAGEM ===")
        for i, v in enumerate(cls.veiculos):
            print(f"Item {i+1}: Chamando __str__() agora...")
            resultado = f'{v}'
            print(f"Resultado: {resultado}\n")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        print(f">>> Executando Carro.__init__")
        super().__init__(marca, modelo)
        self._cor = cor
        print(f">>> Carro criado completamente\n")
        
    def __str__(self):
        print(f"*** CHAMOU Carro.__str__() ***")
        return f'{super().__str__()} | {self._cor}'

# Teste
print("=== CRIANDO OBJETOS ===")
carro1 = Carro("Toyota", "Corolla", "Preto")
carro2 = Carro("Honda", "Civic", "Branco")

print("=== LISTANDO (AQUI QUE __str__ É CHAMADO) ===")
Veiculo.listar()