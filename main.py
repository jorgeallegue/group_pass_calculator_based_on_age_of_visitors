from models.model import Grupo_Entrada
from views.main_view import VistaGrupo
from simple_screen import locate, Screen_manager, Input


if __name__ == "__main__":
    with Screen_manager:
        grupo = Grupo_Entrada()
        grupo.add_entrada(2)
        grupo.add_entrada(6)
        grupo.add_entrada(15)

        vg = VistaGrupo(grupo)
        vg.paint()

        otrog = Grupo_Entrada()
        otrog.add_entrada(54)
        otrog.add_entrada(43)

        vg2 = VistaGrupo(otrog, 42, 1)
        vg2.paint()

        Input()
