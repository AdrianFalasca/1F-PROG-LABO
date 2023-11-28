from biblioteca_stark_5 import *

def stark_marvel_app_5(lista_personajes):
    """
    Realiza la ejecución principal de nuestro programa.
    Parámetros: lista de los personajes que se la pasa como parámetro
    al resto de las funciones.
    Retorno: Sin retorno.
    """
    flag_c = False 
    flag_d = False
    flag_e = False
    flag_f = False

    while True:
        opcion =  stark_menu_principal_desafio_5()
            
        match opcion:
            case "A":
                stark_guardar_heroe_genero(lista_personajes, "m")
            case "B":
                stark_guardar_heroe_genero(lista_personajes, "F")
            case "C":
                if stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,
                                                                "M", "maxima", "altura"):
                    flag_c = True
            case "D":
                if stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, 
                                                            "F", "maxima", "altura"):
                    flag_d = True
            case 'E':
                if stark_calcular_imprimir_guardar_heroe_genero(lista_personajes, 
                                                            "M", "minima", "altura"):
                    flag_e = True
            case "F":
                if stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,
                                                            "F", "minima", "altura"):
                    flag_f = True
            case "G":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, 
                                                                        "altura", "M")
            case "H":
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,
                                                                        "altura", "F")
            case "I":
                if flag_c and flag_d and flag_e and flag_f:
                    informar_nombres_items_c_f()
                else:
                    print("Debe elegir primero los items c, d, e y f")
            case "J":
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_ojos")
            case "K":
                stark_calcular_cantidad_por_tipo(lista_personajes, "color_pelo")
            case "L":
                stark_calcular_cantidad_por_tipo(lista_personajes, "inteligencia")
            case "M":
                stark_listar_heroes_por_dato(lista_personajes, "color_ojos")
            case "N":
                stark_listar_heroes_por_dato(lista_personajes, "color_pelo")
            case "O":
                stark_listar_heroes_por_dato(lista_personajes, "inteligencia")
            case "Z":
                print("Salida exitosa!!!")
                break                        
            case _:
                print("Letra incorrecta. Intente nuevamente.\n")


lista_personajes = leer_archivo("stark_5/data_stark.json")
stark_marvel_app_5(lista_personajes)