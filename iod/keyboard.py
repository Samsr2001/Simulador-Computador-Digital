import pygame

class Keyboard:
    """Gestiona la entrada de teclado."""

    def __init__(self):
        """Inicializa el buffer de teclado."""
        # Este buffer podría usarse para almacenar múltiples pulsaciones si fuera necesario.
        # Por ahora, la lógica de `read_key` es bloqueante y no necesita un buffer complejo.
        pass

    def read_key(self) -> int:
        """
        Espera y captura una tecla, devolviendo su valor ASCII.
        Este es un método de bloqueo. Se debe llamar desde la CPU,
        y el bucle de Pygame debe seguir corriendo para capturar eventos.
        Returns:
            int: El código ASCII de la tecla presionada.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    # `event.unicode` devuelve el caracter como string.
                    # `ord()` lo convierte a su valor ASCII/Unicode.
                    if event.unicode and event.unicode.isprintable():
                        return ord(event.unicode)
            # Es importante ceder tiempo al sistema operativo
            pygame.time.wait(10)
