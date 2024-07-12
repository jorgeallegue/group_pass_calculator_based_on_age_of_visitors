from models.model import Grupo_Entrada
from views.main_view import VistaGrupo, VistaEntrada
from simple_screen import locate, Screen_manager, Input, DIMENSIONS, cls


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
        vedad = VistaEntrada("EDAD: ", 1, 10)

        vg.paint()
        vedad.paint()
        Input("Pulsa Enter para acabar")

with Screen_manager:
    # Instanciamos lo necesario, modelos y componentes graficos
    grupo_entradas = Grupo_Entrada()
    x = (DIMENSIONS.w - 37) // 2

    vista_grupo = VistaGrupo(grupo_entradas, x, 1)
    entrada_edad = VistaEntrada("EDAD: ", x, 10)
    entrada_seguir = VistaEntrada("Resetear y empezar de nuevo (S/n): ", x, 12)
    
    # bucle de pantalla
    while True:
        cls()
        vista_grupo.paint()
        edad = entrada_edad.paint()
        if edad == "":
            respuesta = entrada_seguir.paint()
            if respuesta == "S":
                grupo_entradas = Grupo_Entrada()
                vista_grupo.grupo = grupo_entradas
                continue
            else:
                break

        edad = int(edad)
        grupo_entradas.add_entrada(edad)

    respuesta = entrada_seguir.paint()
    if respuesta == "S":

        locate(1, DIMENSIONS. h -2)
        Input("Pulse enter para salir")

    