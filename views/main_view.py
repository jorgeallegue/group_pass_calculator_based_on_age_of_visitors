from models.model import Grupo_Entrada, TipoEntrada
from simple_screen import locate, Screen_manager, Input

class VistaGrupo:

    def __init__(self, grupo: Grupo_Entrada, x=1, y=1):
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self):
        locate(self.x, self.y, "TIPO             PU     Q       TOTAL")
        locate(self.x, self.y + 1, "=====================================")
        for indice, tipo in enumerate(TipoEntrada):
            nombre = tipo.name
            precio_unitario = tipo.value['P']
            cantidad = self.grupo.cantidad_entradas_por_tipo(tipo)
            subtotal = self.grupo.subtotal_tipo(tipo)
            locate(self.x, self.y + 3 + indice, f"{nombre:<14s}{precio_unitario:5.2f}    {cantidad:2d}     {subtotal:7.2f}")

        locate(self.x, self.y + 7, "-------------------------------------")
        locate(self.x, self.y + 8, f"                      {self.grupo.num_entradas:3d}    {self.grupo.total:8.2f}")

        """
               1         2         3        
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09                          
10    EDAD: 
11    CONF
"""