import math # Importamos el módulo math para funciones matemáticas si fueran necesarias, aunque en este caso no lo es directamente, pero es buena práctica si se piensa en expansiones.

class Personaje:
    """
    Clase que representa a un personaje en el juego "Gran Fantasía".
    Cada personaje tiene un nombre, nivel y experiencia.
    """

    def __init__(self, nombre):
        """
        Método constructor para inicializar un nuevo personaje.
        Args:
            nombre (str): El nombre del personaje.
        """
        self.nombre = nombre  # Asigna el nombre al personaje.
        self.nivel = 1        # Todos los personajes inician en nivel 1.
        self.experiencia = 0  # Todos los personajes inician con 0 experiencia.

    def __str__(self):
        """
        Método especial para representar el objeto Personaje como una cadena de texto.
        Útil para imprimir el estado del personaje de forma legible.
        """
        return f"NOMBRE: {self.nombre}\nNIVEL: {self.nivel}\nEXP: {self.experiencia}"

    def get_estado(self):
        """
        Método accesador (getter) para obtener el estado actual del personaje.
        Muestra en pantalla el nombre, nivel y experiencia.
        """
        print(self) # Reutiliza el método __str__ para imprimir el estado.

    def set_estado(self, experiencia_recibida):
        """
        Método mutador (setter) para actualizar la experiencia del personaje y su nivel.
        Args:
            experiencia_recibida (int): La cantidad de experiencia a añadir o restar.
        """
        # Valida que la experiencia recibida esté dentro del rango permitido (0-99 si es positiva).
        # Aunque la descripción indica entre 0 y 99 *inclusive*, también maneja negativos para restar.
        if 0 <= experiencia_recibida <= 99 or experiencia_recibida < 0:
            experiencia_total = self.experiencia + experiencia_recibida

            # Manejo de ganancia de experiencia
            if experiencia_total >= 0:
                self.nivel += experiencia_total // 100  # Calcula cuántos niveles sube
                self.experiencia = experiencia_total % 100 # Calcula la experiencia restante para el nivel actual
            # Manejo de pérdida de experiencia
            else:
                # Si la experiencia es negativa y el personaje tiene nivel 1 y 0 experiencia, no se altera.
                if self.nivel == 1 and self.experiencia == 0:
                    self.experiencia = 0
                    self.nivel = 1
                else:
                    # Mientras la experiencia sea negativa, se baja de nivel y se ajusta la experiencia
                    while experiencia_total < 0 and self.nivel > 1:
                        self.nivel -= 1
                        experiencia_total += 100 # Añade 100 para "restar" la experiencia de un nivel bajado
                    
                    # Si al final de los descensos de nivel la experiencia sigue siendo negativa,
                    # y el nivel ha llegado a 1, se asegura que la experiencia sea 0.
                    if self.nivel == 1 and experiencia_total < 0:
                        self.experiencia = 0
                    else:
                        self.experiencia = experiencia_total
        else:
            print("Valor de experiencia no válido.") # Mensaje de error si la experiencia_recibida no está en el rango esperado inicialmente.


    def __gt__(self, otro_personaje):
        """
        Sobrecarga del operador ">" (mayor que).
        Permite comparar si el personaje actual tiene mayor nivel que otro.
        Args:
            otro_personaje (Personaje): El otro personaje con el que se compara.
        Returns:
            bool: True si el personaje actual tiene mayor nivel, False en caso contrario.
        """
        return self.nivel > otro_personaje.nivel

    def __lt__(self, otro_personaje):
        """
        Sobrecarga del operador "<" (menor que).
        Permite comparar si el personaje actual tiene menor nivel que otro.
        Args:
            otro_personaje (Personaje): El otro personaje con el que se compara.
        Returns:
            bool: True si el personaje actual tiene menor nivel, False en caso contrario.
        """
        return self.nivel < otro_personaje.nivel

    def __eq__(self, otro_personaje):
        """
        Sobrecarga del operador "==" (igual que).
        Permite comparar si el personaje actual tiene el mismo nivel que otro.
        Args:
            otro_personaje (Personaje): El otro personaje con el que se compara.
        Returns:
            bool: True si el personaje actual tiene el mismo nivel, False en caso contrario.
        """
        return self.nivel == otro_personaje.nivel

    def calcular_probabilidad_ganar(self, oponente):
        """
        Método de instancia que retorna la probabilidad de la instancia actual de ganar
        respecto de otra instancia (oponente).
        Args:
            oponente (Personaje): El personaje oponente.
        Returns:
            float: La probabilidad de ganar (33.0, 50.0, o 66.0).
        """
        if self.nivel < oponente.nivel:
            return 33.0  # Si el jugador es menor al orco, 33% de probabilidad.
        elif self.nivel > oponente.nivel:
            return 66.0  # Si el jugador es mayor al orco, 66% de probabilidad.
        else:
            return 50.0  # Si el jugador es igual al orco, 50% de probabilidad.

    @staticmethod
    def mostrar_dialogo_enfrentamiento(probabilidad):
        """
        Método estático que muestra el diálogo de enfrentamiento al orco
        y retorna la opción escogida por el jugador.
        Args:
            probabilidad (float): La probabilidad de ganar del jugador.
        Returns:
            int: La opción del jugador (1 para Atacar, 2 para Huir).
        """
        print(f"Con tu nivel actual, tienes {probabilidad:.1f}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("\n¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")
        
        while True:
            try:
                opcion = int(input())
                if opcion in [1, 2]:
                    return opcion
                else:
                    print("Opción inválida. Por favor, ingresa 1 para Atacar o 2 para Huir.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")