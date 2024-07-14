# Defines the data models and logic for managing entrance tickets and groups of tickets.
from enum import Enum
from collections import namedtuple

Datos_Entrada = namedtuple("Datos_Entrada", ("precio", "edad_max"))

class TipoEntrada(Enum):  # An Enum that defines different types of entrance tickets (BABY, CHILDREN, ADULT, SENIOR), each associated with a Datos_Entrada namedtuple.
    BABY = Datos_Entrada (0, 2)
    CHILDREN = Datos_Entrada (15, 12)
    ADULT = Datos_Entrada (25, 64)
    SENIOR = Datos_Entrada (20, 99)

class Entrada: # Entrada represents a single entrance ticket. 
    def __init__(self, edad: int): #__init__ function: Initializes an Entrada object, validating the age and determining the type and price of the ticket based on the age. 
        self.__validate_edad(edad) #__validate_edad function: Ensures the age is not negative.
        self.__edad = edad

        for tipo in TipoEntrada: 
            if edad <= tipo.value.edad_max:
                self.tipo = tipo
                self.precio = tipo.value.precio
                break 

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("You cannot introduce a negative age")
        
class Grupo_Entrada: # Represents a group of entrance tickets.
    def __init__(self): #__init__ function: Initializes a Grupo_Entrada object, setting up counters for total price, number of tickets, and types of tickets.
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {}
        for tipo in TipoEntrada:
            self.tipos_entrada[tipo] = {"Q": 0, "P": tipo.value[0]}
        
    def add_entrada(self, edad): #add_entrada function: Adds a new entrance ticket to the group based on the age provided, updating the totals and counts.
        """
        En funcion de la edad, crear una entrada y incrementar el contador de entradas
        Con el precio de la entrada nueva incrementar el total
        """
        nueva_entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += nueva_entrada.precio

        self.tipos_entrada[nueva_entrada.tipo]["Q"] += 1

    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada) -> int: #cantidad_entradas_por_tipo function: Returns the count of tickets for a specific type.
        return self.tipos_entrada[tipo]["Q"]


    def subtotal_tipo(self, tipo: TipoEntrada) -> int: #subtotal_tipo function: Calculates the subtotal price for a specific type of ticket.
        return self.tipos_entrada[tipo]["Q"] * self.tipos_entrada[tipo]["P"]