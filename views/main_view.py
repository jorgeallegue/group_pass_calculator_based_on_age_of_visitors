from models.model import Grupo_Entrada, TipoEntrada
from simple_screen import locate, Screen_manager, Input, cls, DIMENSIONS

class VistaGrupo:

    def __init__(self, grupo: Grupo_Entrada, x=1, y=1):
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self):
        locate(self.x, self.y, "TYPE          PRICE  QUANTITY   TOTAL")
        locate(self.x, self.y + 1, "=====================================")
        for indice, tipo in enumerate(TipoEntrada):
            locate(self.x, self.y + 3 + indice, f"{tipo.name:.<14s}{tipo.value.precio:5.2f}    {self.grupo.cantidad_entradas_por_tipo(tipo):2d}     {self.grupo.subtotal_tipo(tipo):7.2f}")

        locate(self.x, self.y + 7, "-------------------------------------")
        locate(self.x, self.y + 8, f"                      {self.grupo.num_entradas:3d}    {self.grupo.total:8.2f}")

class VistaEntrada:
        def __init__(self, etiqueta: str, x, y):
             self.etiqueta = etiqueta
             self.y = y
             self.x = x
             self.value = ""
        
        def paint(self):
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