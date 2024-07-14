# Contains the main control logic, managing the flow of the application.
from models.model import Grupo_Entrada
from views.main_view import VistaGrupo, VistaEntrada
from simple_screen import locate, Screen_manager, Input, DIMENSIONS, cls

def run_app(): #  Manages the main loop of the application
    with Screen_manager: # Uses Screen_manager to handle the terminal display.
        grupo_entradas = Grupo_Entrada() #Initializes the models (Grupo_Entradas) and views (VistaGrupo, VistaEntrada).
        x = (DIMENSIONS.w - 37) // 2

        vista_grupo = VistaGrupo(grupo_entradas, x, 1)
        entrada_edad = VistaEntrada("AGE: ", x, 10)
        entrada_seguir = VistaEntrada("Do you want to start again? (Y/N): ", x, 12)

        # Runs a loop to: 1. Display the group view. 2. Get user input for age and whether to restart. 3. Update the group of entrance tickets based on user input. 4. Handle restarting or exiting the application based on user input.
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