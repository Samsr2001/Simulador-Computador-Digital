from iod.keyboard import Keyboard
from iod.screen import Screen

class IOManager:
    """Gestiona todos los dispositivos de Entrada/Salida."""

    def __init__(self):
        """Inicializa el gestor de E/S con un teclado y una pantalla."""
        self.keyboard = Keyboard()
        self.screen = Screen()

    def read_key(self) -> int:
        """
        Lee una tecla del teclado.
        Returns:
            int: El código ASCII de la tecla.
        """
        # La lógica de espera está en el propio teclado
        return self.keyboard.read_key()

    def write_char(self, value: int):
        """
        Escribe un caracter en la pantalla.
        Args:
            value (int): El código ASCII del caracter a mostrar.
        """
        self.screen.write_char(value)

    def reset(self):
        """Reinicia los dispositivos de E/S."""
        self.screen.reset()
        # El teclado no necesita reinicio de estado en este diseño
