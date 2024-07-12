from models.model import Grupo_Entrada
from views.main_view import VistaGrupo, VistaEntrada
from simple_screen import locate, Screen_manager, Input, DIMENSIONS, cls


with Screen_manager:
    # Instanciamos lo necesario, modelos y componentes graficos
    grupo_entradas = Grupo_Entrada()
    x = (DIMENSIONS.w - 37) // 2

    vista_grupo = VistaGrupo(grupo_entradas, x, 1)
    entrada_edad = VistaEntrada("AGE: ", x, 10)
    entrada_seguir = VistaEntrada("Do you want to start again? (Y/N): ", x, 12)

    # Bucle de pantalla 
    while True:
        cls()
        vista_grupo.paint()
        edad = entrada_edad.paint()
        if edad == "":
            respuesta = entrada_seguir.paint()
            if respuesta == "Y":
                grupo_entradas = Grupo_Entrada()
                vista_grupo.grupo = grupo_entradas
                continue
            else:
                break
        
        edad = int(edad)
        grupo_entradas.add_entrada(edad)

    # Final "controlado" del programa
    locate(1, DIMENSIONS.h - 2)
    Input("Clic enter to exit")
    


    