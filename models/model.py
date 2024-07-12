from enum import Enum
from collections import namedtuple

Datos_Entrada = namedtuple("Datos_Entrada", ("precio", "edad_max"))

class TipoEntrada(Enum):
    BABY = Datos_Entrada (0, 2)
    CHILDREN = Datos_Entrada (15, 12)
    ADULT = Datos_Entrada (25, 64)
    SENIOR = Datos_Entrada (20, 99)

class Entrada:
    def __init__(self, edad: int):
        self.__validate_edad(edad)
        self.__edad = edad

        for tipo in TipoEntrada: 
            if edad <= tipo.value.edad_max:
                self.tipo = tipo
                self.precio = tipo.value.precio
                break 

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("You cannot introduce a negative age")
        
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