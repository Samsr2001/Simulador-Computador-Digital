import time

class Keyboard:
    """Gestiona la entrada de teclado a través de un buffer en IOManager."""

    def __init__(self, io_manager):
        """
        Inicializa el teclado.
        Args:
            io_manager (IOManager): El gestor de E/S que contiene el buffer.
        """
        self.io_manager = io_manager

    def read_key(self) -> int:
        """
        Espera y obtiene una tecla del buffer del IOManager.
        Este método es bloqueante para el ciclo de la CPU, pero no para la GUI.
        Returns:
            int: El código ASCII de la tecla.
        """
        while True:
            key_code = self.io_manager.pop_key()
            if key_code is not None:
                return key_code
            # Pequeña pausa para no saturar la CPU y permitir que la GUI se actualice.
            time.sleep(0.01)

