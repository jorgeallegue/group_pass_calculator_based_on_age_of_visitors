from enum import Enum

class TipoEntrada(Enum):
    BEBE = {'P': 0, 'Q': 0}
    NIÑO = {'P': 14, 'Q': 0}
    ADULTO = {'P': 23, 'Q': 0}
    JUBILADO = {'P': 18, 'Q': 0}

class Entrada:
    def __init__(self, edad: int):
        self.__validate_edad(edad)
        self.__edad = edad
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa")
        
class Grupo_Entrada:

    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.BEBE: {'P': TipoEntrada.BEBE.value['P'], 'Q': 0},
            TipoEntrada.NIÑO: {'P': TipoEntrada.NIÑO.value['P'], 'Q': 0},
            TipoEntrada.ADULTO: {'P': TipoEntrada.ADULTO.value['P'], 'Q': 0},
            TipoEntrada.JUBILADO: {'P': TipoEntrada.JUBILADO.value['P'], 'Q': 0}
        }

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
    
    