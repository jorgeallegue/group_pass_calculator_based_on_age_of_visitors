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
        entrada_seguir = VistaEntrada("Do you want to start again?  (Y/N): ", x, 12)

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
            
            try:
                edad = int(edad)
                if edad < 0 or edad > 100:
                    raise ValueError("Invalid age")
                grupo_entradas.add_entrada(edad)
            except ValueError as e:
                locate(x, 12, f"Please enter an age between 0 and 100")
                locate(x, 13, "Press enter to continue")
                Input()

        # Final "controlado" del programa
        locate(1, DIMENSIONS.h - 2)
        locate(x, 13, "Clic enter to exit")
        Input()