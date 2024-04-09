import requests
from bs4 import BeautifulSoup
from hollow import Hollow
from quincy import Quincy
from shinigami import Shinigami
from visored import Visored

# Lista para almacenar los personajes creados
personajes = []


def obtener_datos_shinigamis():
    shinigamis = []
    url_base = "https://bleach.fandom.com/es/wiki/"
    url_armas = "https://bleach.fandom.com/es/wiki/Lista_de_Armas"
    respuesta = requests.get(url_armas)
    if respuesta.status_code != 200:
        raise ValueError("No se pudo obtener la información de la página")
    soup = BeautifulSoup(respuesta.text, "html.parser")
    h3 = soup.find('span', {'id': 'Zanpaku-t.C5.8D_de_Shinigamis_y_Visored'})
    tabla = h3.find_next('table')
    for fila in tabla.find_all('tr')[2:]:
        columnas = fila.find_all('td')
        if len(columnas) >= 3:
            nombre = columnas[1].text.strip()
            zanpakuto = columnas[0].text.strip()
            bankai = columnas[2].text.strip()
            shinigamis.append((nombre, zanpakuto, bankai))
    return shinigamis


def mostrar_shinigamis():
    shinigamis = obtener_datos_shinigamis()
    print("Nombre de las armas y sus shinigamis:")
    for i, shinigami in enumerate(shinigamis, 1):
        print(f"{i}. {shinigami[0]}")
        print(f"Zanpakuto: {shinigami[1]}")
        print(f"Bankai: {shinigami[2]}")
        print("")


def obtener_detalle_personaje(nombre_personaje):
    # https://bleach.fandom.com/es/wiki/Kisuke_Urahara
    # url_base = "https://bleach.fandom.com/es/wiki/Especial:Buscar?query="
    url_base = "https://bleach.fandom.com/es/wiki/"
    nombre_personaje= nombre_personaje.replace(" ", "_")
    url_personaje = url_base + nombre_personaje.strip()
    respuesta = requests.get(url_personaje)
    # capturar respuesta para el shinigami seleccionado
    soup = BeautifulSoup(respuesta.text, 'html.parser')  # parsear la respuesta de la pagina
    sumario = soup.find('div', {'id': 'toc'})
    descripcion = sumario.find_previous('p').text.strip()
    return (descripcion)





def obtener_detalle_personaje2(nombre_personaje):
    url_base = "https://bleach.fandom.com/es/wiki/"
    url_personaje = url_base + nombre_personaje.replace(" ", "_")
    respuesta = requests.get(url_personaje)
    if respuesta.status_code != 200:
        raise ValueError(f"No se pudo obtener la información de la página: {url_personaje}")
    soup = BeautifulSoup(respuesta.text, "html.parser")
    contenido_principal = soup.find('div', {'id': 'mw-content-text'})
    primer_parrafo = contenido_principal.find('p')
    if primer_parrafo:
        descripcion = primer_parrafo.text.strip()
        return descripcion
    else:
        raise ValueError("No se pudo encontrar el detalle del personaje en la página")






def crear_shinigami():
    print("---------CREAR PERSONAJE----------")
    print("Tipo de Personaje:")
    print("1. Shinigami")
    print("2. Hollow")
    print("3. Quincy")
    print("4. Visored (Shinigami con poderes Hollow)")

    tipo_personaje = input("Ingrese el número correspondiente al tipo de personaje deseado: ")

    if tipo_personaje == '1':
        mostrar_shinigamis()
        numero_shinigami = int(input("Ingrese el número del shinigami que desea: ")) - 1
        shinigami_seleccionado = obtener_datos_shinigamis()[numero_shinigami]
        nombre_shinigami = shinigami_seleccionado[0]
        zanpakuto = shinigami_seleccionado[1]
        personaje = Shinigami(nombre_shinigami, '', [], zanpakuto)
        personajes.append(personaje)
        print("Shinigami creado exitosamente.")
        detalle_personaje = obtener_detalle_personaje(nombre_shinigami)
        print("Detalle del personaje:")
        print(detalle_personaje)
    elif tipo_personaje == '2':
        nombre = input("Ingrese el nombre del Hollow: ")
        poder = input("Ingrese el poder del Hollow: ")
        habilidades = input("Ingrese las habilidades del Hollow (separadas por comas): ").split(',')
        mascara = input("Ingrese el nombre de la máscara: ")
        personaje = Hollow(nombre, poder, habilidades, mascara)
        personajes.append(personaje)
        print("Hollow creado exitosamente.")
    elif tipo_personaje == '3':
        nombre = input("Ingrese el nombre del Quincy: ")
        poder = input("Ingrese el poder del Quincy: ")
        habilidades = input("Ingrese las habilidades del Quincy (separadas por comas): ").split(',')
        arco = input("Ingrese el nombre del arco: ")
        personaje = Quincy(nombre, poder, habilidades, arco)
        personajes.append(personaje)
        print("Quincy creado exitosamente.")
    elif tipo_personaje == '4':
        nombre = input("Ingrese el nombre del Visored: ")
        poder = input("Ingrese el poder del Visored: ")
        habilidades = input("Ingrese las habilidades del Visored (separadas por comas): ").split(',')
        zanpakuto = input("Ingrese el nombre de la Zanpakuto: ")
        mascara = input("Ingrese el nombre de la máscara: ")
        personaje = Visored(nombre, poder, habilidades, zanpakuto, mascara)
        personajes.append(personaje)
        print("Visored creado exitosamente.")
    else:
        print("Tipo de personaje no válido.")


def main():
    while True:
        print("\nMenu:")
        print("1. Crear Personaje")
        print("2. Ver personajes creados")
        print("3. Ver detalles de un personaje")
        print("4. Activar habilidad o atacar")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_shinigami()
        elif opcion == '2':
            print("Personajes creados:")
            for i, personaje in enumerate(personajes, 1):
                print(f"{i}. {personaje.obtener_nombre()}")
        elif opcion == '3':
            print("Ver detalles de un personaje:")
            if personajes:
                ver_detalle = int(input("Ingrese el número del personaje del cual desea ver detalles: ")) - 1
                if 0 <= ver_detalle < len(personajes):
                    nombre_personaje = personajes[ver_detalle].obtener_nombre()
                    detalle = obtener_detalle_personaje(nombre_personaje)
                    print("Detalles del personaje:")
                    print(detalle)
                else:
                    print("Índice de personaje no válido.")
            else:
                print("No hay personajes creados.")
        elif opcion == '4':
            print("Activar habilidad o atacar")
            # Implementa la lógica según sea necesario
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
