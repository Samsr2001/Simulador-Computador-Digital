import collections
from iod.keyboard import Keyboard
from iod.screen import Screen

class IOManager:
    """Gestiona todos los dispositivos de Entrada/Salida."""

    def __init__(self):
        """Inicializa el gestor de E/S con un teclado y una pantalla."""
        self.key_buffer = collections.deque()
        self.keyboard = Keyboard(self)
        self.screen = Screen()

    def push_key(self, key_code: int):
        """Añade un código de tecla al buffer."""
        self.key_buffer.append(key_code)

    def pop_key(self) -> int | None:
        """Saca un código de tecla del buffer. Devuelve None si está vacío."""
        if self.key_buffer:
            return self.key_buffer.popleft()
        return None

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

    def write_value(self, value: int):
        """
        Escribe un valor numérico en la pantalla.
        Args:
            value (int): El número a mostrar.
        """
        self.screen.write_value(value)

    def reset(self):
        """Reinicia los dispositivos de E/S."""
        self.screen.reset()
        self.key_buffer.clear()
        # El teclado no necesita reinicio de estado en este diseño
