#Defines the views for displaying information and gathering user input.
from models.model import Grupo_Entrada, TipoEntrada
from simple_screen import locate, Screen_manager, Input, cls, DIMENSIONS

class VistaGrupo: #Displays a summary of the entrance tickets in a group.

    def __init__(self, grupo: Grupo_Entrada, x=1, y=1): # __init__ function: Initializes the view with a reference to the Grupo_Entrada object and coordinates for display.
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self): # paint function: Renders the table of ticket types, prices, quantities, and totals on the screen.
        locate(self.x, self.y, "PASS TYPE     PRICE  QUANTITY   TOTAL")
        locate(self.x, self.y + 1, "=====================================")
        for indice, tipo in enumerate(TipoEntrada):
            locate(self.x, self.y + 3 + indice, f"{tipo.name:.<14s}{tipo.value.precio:5.2f}    {self.grupo.cantidad_entradas_por_tipo(tipo):2d}     {self.grupo.subtotal_tipo(tipo):7.2f}")

        locate(self.x, self.y + 7, "-------------------------------------")
        locate(self.x, self.y + 8, f"                      {self.grupo.num_entradas:3d}    {self.grupo.total:8.2f}")

class VistaEntrada: # Handles user input for entering an age or deciding whether to restart.
        def __init__(self, etiqueta: str, x, y): #__init__ function: Initializes the view with a label and coordinates for display.
             self.etiqueta = etiqueta
             self.y = y
             self.x = x
             self.value = ""
        
        def paint(self): #paint function: Displays the label and gets user input.
             locate(self.x, self.y, self.etiqueta)
             return Input()

print(__name__)
if __name__ == "__main__":
    with Screen_manager:
        grupo = Grupo_Entrada()
        grupo.add_entrada(2)
        grupo.add_entrada(6)
        grupo.add_entrada(15)

        vg = VistaGrupo(grupo)

        vedad = VistaEntrada("AGE: ", 1, 10)

        vg.paint()
        vedad.paint()

        Input("Clic exit to enter")