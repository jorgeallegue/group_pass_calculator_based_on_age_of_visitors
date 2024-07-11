from enum import Enum

class TipoEntrada(Enum):
    BEBE = (0, 2)
    NIÑO = (14, 12)
    ADULTO = (23, 65)
    JUBILADO = (18, 120)

class Entrada:
    def __init__(self, edad: int):
        self.__validate_edad(edad)
        self.__edad = edad

        for tipo in TipoEntrada: 
            if edad <= tipo.value[1]:
                self.tipo = tipo
                self.precio = tipo.value[0]
                break 

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa")
        
class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {}
        for tipo in TipoEntrada:
            self.tipos_entrada[tipo] = {"Q": 0, "P": tipo.value[0]}
        

    def add_entrada(self, edad):
        """
        En funcion de la edad, crear una entrada y incrementar el contador de entradas
        Con el precio de la entrada nueva incrementar el total
        """
        nueva_entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += nueva_entrada.precio

        self.tipos_entrada[nueva_entrada.tipo]["Q"] += 1

    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo]["Q"]


    def subtotal_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo]["Q"] * self.tipos_entrada[tipo]["P"]