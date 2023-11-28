import re
import json
import csv


def imprimir_menu_desafio_5():
    """
    Imprime el menú de opciones.
    Parámetro:  sin parámetros.
    Retorno: sin retorno. Imprime la menú.
    """
    print("""
OPCIONES:
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
    H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia 
(En caso de no tener, Inicializarlo con 'No Tiene').
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    Z. Salir
_____________________________________________________________________________
""")

def stark_menu_principal_desafio_5():
    """
    Llama a la función para imprimir el menú de opciones.
    Le pide al usuario que elija una opción.
    Parámetro:  sin parámetros.
    Retorno: La opción si está validada, caso contrario -1
    """
    imprimir_menu_desafio_5()
    opcion = input("Elija una de las anteriores opciones\
(A, B, C, D, E, F, G, H, I, J, K,L, M, N, O, Z): ").upper()
    print()
    
    if re.search("[A-O]{1}|[Z]{1}", opcion):
        return opcion
    else:
        return -1


def leer_archivo(nombre_ext):
    """
    Abre el archivo que se le pasa como parámetro y lo lee.
    Parámetro:  String del nombre del archivo con extensión.
    Retorno: la lista de heroes.
    """
    with open(nombre_ext) as archivo:
        datos = json.load(archivo) 
    return datos["heroes"]


def guardar_archivo(nombre_ext, contenido):
    """
    Guarda el contenido en el archivo. Los dos pasados por parámetro.
    Parámetro:  Un string con nombre de archivo y su extensión y
    otro string con el contenido a guardar.
    Retorno: Imprime cuando se crea el archivo y retorna True,
    caso contrario imprime el error y retorna False.
    """
    with open(nombre_ext, "w") as archivo:
        archivo.write(contenido)
        if archivo:
            print(f"Se creó el archivo: {nombre_ext}")
            return True
        else:
            print(f"Error al crear el archivo: {nombre_ext}")
            return False
    

def capitalizar_palabras(palabras):
    """
    Convierte las iniciales de las palabras en mayúscula.
    Parámetro:  palabra(string).
    Retorno: string de la palábra capitalizada.
    """
    return palabras.capitalize()


def obtener_nombre_capitalizado(dict_personaje):
    """
    Capitaliza el nombre del diccionario pasado por parámetro.
    Parámetro:  diccionario de un personaje.
    Retorno: string del nombre capitalizado.
    """
    return f"Nombre: {capitalizar_palabras(dict_personaje['nombre'])}"


def obtener_nombre_y_dato(dict_personaje, key):
    """
    Llama a la función para capitalizar y le pasa el diccionario recibido como parámetro.
    Reduce a dos decimales los string que contengan float o int.
    Parámetro:  diccionario de un personaje y un string de la clave.
    Retorno: Un string del nombre y la clave con su valor.
    """
    nombre = obtener_nombre_capitalizado(dict_personaje)
    if re.search("^([0-9]+\.[0-9]+)|([0-9])+$", dict_personaje[key]):
        value = float(dict_personaje[key])
        dict_personaje[key] = f"{value:.2f}"
    return f"{nombre} | {key}: {dict_personaje[key]}"

##############################################################################

def es_genero(dict_personaje, genero):
    """
    Compara si el género pasado por parámetro está como valor
    dentro de la clave género del diccionario.
    Parámetro:  un diccionario de un personaje. un string con el género.
    Retorno: True si está el género, caso contrario False .
    """
    if dict_personaje["genero"] == genero.upper():
        return True
    else:
        return False


def stark_guardar_heroe_genero(lista_personajes, genero_m_f):
    """
    Recorre la lista de personajes y llama a la función para validar género 
    y concatena un mensaje(que capitaliza los nombre con una función) 
    que luego será guardado como string.
    Parámetro:  Lista de los personajes y un string con el género m o f.
    Retorno: True si se guarda, caso contrario False. Imprime el mensaje guardado.
    """
    mensaje = ""
    for dict_personaje in lista_personajes:
        if es_genero(dict_personaje, genero_m_f):
            mensaje += f"{obtener_nombre_capitalizado(dict_personaje)},\n"
    print(mensaje)
    return guardar_archivo(f"personajes_{genero_m_f.lower()}.csv", mensaje)

############################################################################

def calcular_min_genero(lista_personajes, genero, clave):
    """
    Recorre la lista y obtiene un diccionario con el personaje con el género
    pasado como parámetro y el menor valor de la clave pasada por parámetro.
    Parámetro:  Lista de personajes, un string con el género y otro con la clave.
    Retorno: el diccionario del mínimo, caso contrario False.
    """
    minimo = None
    retorno_minimo = False

    for dict_personaje in lista_personajes:
        if dict_personaje["genero"] == genero and\
            re.search("^([0-9]+\.[0-9]+)|([0-9])+$", dict_personaje[clave]):
            if minimo == None or float(dict_personaje[clave]) < minimo:
                minimo = float(dict_personaje[clave])
                retorno_minimo = dict_personaje

    return retorno_minimo


def calcular_max_genero(lista_personajes, genero, clave):
    """
    Recorre la lista y obtiene un diccionario con el personaje con el género
    pasado como parámetro y el mayor valor de la clave pasada por parámetro.
    Parámetro:  Lista de personajes, un string con el género y otro con la clave.
    Retorno: el diccionario del máximo, caso contrario False
    """
    maximo = None
    retorno_maximo = False

    for dict_personaje in lista_personajes:
        if dict_personaje["genero"] == genero and\
            re.search("^([0-9]+\.[0-9]+)|([0-9])+$", dict_personaje[clave]):
            if maximo == None or float(dict_personaje[clave]) > maximo:
                maximo = float(dict_personaje[clave])
                retorno_maximo = dict_personaje

    return retorno_maximo


def calcular_max_min_dato_genero(lista_personajes, genero, max_o_min, clave):
    """
    Valida si es mínimo o máximo y llama a la función correspondiente.
    Parámetro:  Lista de personajes, un string con el género, otro con la clave 
    y otro con el máximo o mínimo.
    Retorno: el diccionario del mínimo o máximo, caso contrario False.
    """
    if max_o_min == "minima":
        return calcular_min_genero(lista_personajes, genero, clave)
    elif max_o_min == "maxima":
        return calcular_max_genero(lista_personajes, genero, clave)


def stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,
                                                genero, max_o_min, clave):
    """
    Llama a la función para calcular máximo o mínimo y del diccionario 
    que devuelve obtiene el nombre y dato a través de una función. 
    Luego crea un string para guardarla en un archivo.
    Parámetro:  Lista de personajes, un string con el género, otro con la clave 
    y otro con el máximo o mínimo.
    Retorno: True si se guarda, caso contrario False.
    """
    dict_personaje = calcular_max_min_dato_genero(lista_personajes, 
                                                genero, max_o_min, clave)
    nombre_dato = obtener_nombre_y_dato(dict_personaje, clave)
    if dict_personaje:
        mensaje = f"{capitalizar_palabras(clave)} {max_o_min}: {nombre_dato},"
        print(mensaje)
        formato = f"heroe_{max_o_min}_{clave}_{genero.lower()}.csv"
        return guardar_archivo(formato, mensaje)
    else:
        return False

###############################################################################

def sumar_dato_heroe_genero(lista_personajes, key, genero):
    """
    Recorre la lista y acumula el valor de la key pasada como parámetro y
    que sea del género pasado como parámetro.
    Parámetro:  Lista de personajes, un string con el género y otro con la clave.
    Retorno: un float con el acumulador, caso contrario -1.
    """
    acumulador = 0
    for dict_personaje in lista_personajes:
        if type(dict_personaje) != dict or dict_personaje == {}:
                return -1
        else:
            if dict_personaje["genero"] == genero.upper():
                acumulador += float(dict_personaje[key])

    return acumulador

def cantidad_heroes_genero(lista_personajes, genero):
    """
    Recorre la lista y obtiene un contador de los que tengan 
    el género pasado por parámetro.
    Parámetro:  Lista de personajes, un string con el género.
    Retorno: un entero con el contador.
    """
    contador_genero = 0
    for dict_personajes in lista_personajes:
        if dict_personajes["genero"] == genero.upper():
            contador_genero += 1

    return contador_genero


def dividir(dividendo, divisor):
    """
    División de dos números para sacar promedio.

    Parámetro: dividendo(int o float)
    Parámetro: divisor(int o float)
    :return: Resultado de la división(float) o False si el divisor es 0
    """
    if divisor == 0:
        return False
    resultado = dividendo / divisor
    return resultado

def calcular_promedio_genero(lista_personajes, key, genero):
    """
    Llama a tres funciones para sacar el promedio.
    Parámetro:  Lista de personajes, un string con el género y otro con la clave.
    Retorno: float con el promedio.
    """
    acumulador = sumar_dato_heroe_genero(lista_personajes, key, genero)
    contador = cantidad_heroes_genero(lista_personajes, genero)
    promedio = dividir(acumulador, contador)
    return promedio

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes, 
                                                            key, genero):
    """
    Llama a la función para calcular promedio y
    hace validaciones antes de guardarla en un archivo.
    Parámetro:  Lista de personajes, un string con el género y otro con la clave.
    Retorno: True si se guarda, caso contrario False. Imprime el mensaje o error.
    """
    if lista_personajes == {}:
        print("Error: Lista de héroes vacía.")
        return False
    
    if not re.search("^(M|m)|(F|f)$", genero):
        return False
    
    promedio = calcular_promedio_genero(lista_personajes, key, genero)
    mensaje = f'Altura promedio género {genero}: {promedio:.2f},'
    print(mensaje)
    formato = f"heroes_promedio_altura_{genero}.csv"
    return guardar_archivo(formato, mensaje)

####################################################################################

def calcular_cantidad_tipo(lista_personajes, dato_cualidad):
    """
    Crea un set con las cualidades, las recorre y las compara con cada diccionario
    recorrido y las guarda en un diccionario como clave y sus cantidades como valor.
    Parámetro:  Lista de personajes, un string con la cualidad.
    Retorno: el diccionario con las cualidades y sus cantidades,
    caso contrario un json con mensaje de error.
    """
    if lista_personajes == []:
        diccionario = {"Error": "La lista se encuentra vacía"}
        return json.dumps(diccionario, indent=4, ensure_ascii=False)
    
    dict_cualidad = {}
    set_cualidad = set([])
    for dict_personaje in lista_personajes:
        set_cualidad.add(capitalizar_palabras(dict_personaje[dato_cualidad]))

    for tipo_cualidad in set_cualidad:
        contador_cualidad = 0
        for dict_personaje in lista_personajes:
            if capitalizar_palabras(dict_personaje[dato_cualidad]) == tipo_cualidad:
                contador_cualidad += 1
        dict_cualidad[tipo_cualidad] = contador_cualidad
    return dict_cualidad


def guardar_cantidad_heroes_tipo(dict_cualidad, dato_cualidad):
    """
    Recorre el diccionario de cualidades y cantidades, lo normaliza si está vacío,
    y genera un string con un mensaje que luego guarda en un archivo.
    Parámetro:  diccionario con cualidades y cantidades, un string con la cualidad.
    Retorno: true si se guarda, caso contrario False. Imprime el mensaje.
    """
    mensaje = ""
    for clave, valor in dict_cualidad.items():
        if clave == "":
            clave = "No tiene"
        mensaje += f"Caracteristica: {dato_cualidad} {clave}- \
Cantidad de heroes: {valor},\n"
    
    formato = f"heroes_cantidad_{dato_cualidad}.csv"
    print(mensaje)
    return guardar_archivo(formato, mensaje)

def stark_calcular_cantidad_por_tipo(lista_personajes, dato_cualidad):
    """
    Llama a las funciones para calcular cantidad de cualidades y para guardarla.
    Parámetro:  Lista de personajes, un string con la cualidad.
    Retorno: True si se guarda, caso contrario False.
    """
    dict_cualidad = calcular_cantidad_tipo(lista_personajes, dato_cualidad)
    return guardar_cantidad_heroes_tipo(dict_cualidad, dato_cualidad)

#######################################################################################

def obtener_lista_de_tipos(lista_personajes, tipo_cualidad):
    """
    Crea un set con las cualidades, y si no tiene la normaliza.
    Parámetro:  Lista de personajes, un string con la cualidad.
    Retorno: un set con las cualidades.
    """
    lista_cualidades = []
    for dict_personaje in lista_personajes:
        if dict_personaje[tipo_cualidad] == "":
            lista_cualidades.append("N/a")  
        else:
            lista_cualidades.append(capitalizar_palabras(dict_personaje[tipo_cualidad]))
    set_cualidades = set(lista_cualidades)
    return set_cualidades

def normalizar_dato(valor, valor_por_defecto):
    """
    Normaliza el valor si está vacío.
    Parámetro:  dos string con valor y valor por defecto.
    Retorno: un string con el valor.
    """
    if valor == "":
        valor = valor_por_defecto
    return valor

def normalizar_heroe(dict_personaje, clave):
    """
    Normalizar valores con la clave y diccionario pasado por parámetro.
    Parámetro:  diccionario de un personaje, un string con la clave.
    Retorno: el diccionario de un personaje.
    """
    dict_personaje[clave] = capitalizar_palabras(dict_personaje[clave])
    dict_personaje[clave] = normalizar_dato(dict_personaje[clave], "N/a")
    dict_personaje["nombre"] = capitalizar_palabras(dict_personaje["nombre"])
    return dict_personaje

def obtener_heroes_por_tipo(lista_personajes, set_cualidades, tipo_cualidad):
    """
    Recorre el set de cualidades y por cada cualidad recorre la lista 
    y genera un lista
    con los nombres normalizada con la función correspondiente.
    Parámetro:  Lista de personajes, un string con la cualidad 
    y un set de cualidades.
    Retorno: el diccionario con las cualidades como clave y 
    una lista de nombres como valor.
    """
    
    dict_cualidades = {}
    for cualidad in set_cualidades:
        lista_nombre = []
        for dict_personaje in lista_personajes:
            dict_personaje = normalizar_heroe(dict_personaje, tipo_cualidad)
            if  dict_personaje[tipo_cualidad] == cualidad:
                lista_nombre.append(dict_personaje["nombre"])
        dict_cualidades[cualidad] = lista_nombre
    return dict_cualidades

def guardar_heroes_por_tipo(dict_cualidades, tipo_cualidad):
    """
    Recorre el diccionario de cualidades que contiene por cada cualidad como clave,
    una lista de nombres como valor y la concatena en un mensaje(string) que luego
    será guardada en un archivo.
    Parámetro:  diccionario de cualidades, un string con la cualidad.
    Retorno: True si se guarda, caso contrario False. Imprime el mensaje que se guarda.
    """
    mensaje = ""
    for clave, valor in dict_cualidades.items():
        mensaje += f"{tipo_cualidad} {clave}: {' | '.join(valor)},\n"
    print(mensaje)
    formato = f"heroes_segun_{tipo_cualidad}.csv"
    return guardar_archivo(formato, mensaje)

def stark_listar_heroes_por_dato(lista_personajes, tipo_cualidad):
    """
    Llama a las funciones correnpondientes para obtener el set de cualidades,
    el diccionario de cualidades y luego guardala en un archivo.
    Parámetro:  Lista de personajes, un string con la cualidad.
    Retorno: True si la guarda, caso contrario False.
    """
    set_cualidades = obtener_lista_de_tipos(lista_personajes, tipo_cualidad)
    dict_cualidades = obtener_heroes_por_tipo(lista_personajes, 
                                            set_cualidades, tipo_cualidad)
    return guardar_heroes_por_tipo(dict_cualidades, tipo_cualidad)

##########################################################################

def informar_nombres_items_c_f():
    """
    Lee los archivos con extension csv y los concatena en un string que imprime.
    Parámetro:  sin parametros.
    Retorno: sin retorno. Imprime los nombres y datos de los items c-f.
    """
    mensaje = ""
    lista = ["heroe_maxima_altura_m.csv",
        "heroe_maxima_altura_f.csv",
        "heroe_minima_altura_m.csv",
        "heroe_minima_altura_f.csv"]
    
    for elem in lista:
        with open(elem) as archivo:
            archivo = csv.reader(archivo)
            for personaje in archivo:
                mensaje += f"{''.join(personaje)}\n"

    print(mensaje)