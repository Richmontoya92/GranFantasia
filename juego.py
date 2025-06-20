import random # Importa el módulo random para generar números aleatorios.
from personaje import Personaje # Importa la clase Personaje desde el archivo personaje.py.

def jugar_gran_fantasia():
    """
    Función principal que ejecuta la escena del juego "Gran Fantasía".
    """
    print("¡Bienvenido a Gran Fantasía!")
    
    # Solicitar el nombre del personaje al jugador
    nombre_jugador = input("Por favor indique nombre de su personaje:\n")
    
    # Crear el personaje del jugador
    jugador = Personaje(nombre_jugador)
    print("\n")
    jugador.get_estado() # Mostrar el estado inicial del personaje del jugador.

    print("\n¡Oh no!, ¡Ha aparecido un Orco!")
    # Crear el personaje del Orco
    orco = Personaje("Orco")

    # Calcular la probabilidad inicial de ganar del jugador
    probabilidad_ganar = jugador.calcular_probabilidad_ganar(orco)
    
    # Mostrar el diálogo de enfrentamiento y obtener la opción del jugador
    opcion_juego = Personaje.mostrar_dialogo_enfrentamiento(probabilidad_ganar)

    # Bucle principal del juego mientras el jugador decida "Atacar"
    while opcion_juego == 1:
        # Generar un número aleatorio entre 0 y 1 para determinar el resultado del ataque
        resultado_ataque = random.uniform(0, 1)
        
        # Convertir la probabilidad a un valor entre 0 y 1 para la comparación
        probabilidad_para_comparar = probabilidad_ganar / 100.0

        if resultado_ataque <= probabilidad_para_comparar:
            # El jugador gana
            print("\n¡Le has ganado al orco, felicidades!")
            print("¡Recibirás 50 puntos de experiencia!")
            jugador.set_estado(50) # El jugador gana 50 puntos de experiencia
            orco.set_estado(-30)  # El orco pierde 30 puntos de experiencia
        else:
            # El orco gana
            print("\n¡Oh no! ¡El orco te ha ganado!")
            print("¡Has perdido 30 puntos de experiencia!")
            jugador.set_estado(-30) # El jugador pierde 30 puntos de experiencia
            orco.set_estado(50)   # El orco gana 50 puntos de experiencia
        
        # Mostrar los estados actualizados de ambos personajes
        print("\n")
        jugador.get_estado()
        print("\n")
        orco.get_estado()
        
        # Recalcular la probabilidad de ganar con los estados actualizados
        probabilidad_ganar = jugador.calcular_probabilidad_ganar(orco)
        
        # Volver a mostrar el diálogo y pedir la opción al jugador
        opcion_juego = Personaje.mostrar_dialogo_enfrentamiento(probabilidad_ganar)
    
    # Si el jugador decide huir
    if opcion_juego == 2:
        print("\n¡Has huido! El orco ha quedado atrás.")

# Punto de entrada del juego
if __name__ == "__main__":
    jugar_gran_fantasia()