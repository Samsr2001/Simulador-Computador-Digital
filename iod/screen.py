class Screen:
    """Simula una pantalla de teletipo."""

    def __init__(self, max_lines=5):
        """
        Inicializa la pantalla con un buffer.
        Args:
            max_lines (int): Número máximo de líneas a mantener en el buffer.
        """
        self._buffer = ""
        self.max_lines = max_lines

    def write_char(self, char_code: int):
        """
        Añade un caracter al buffer de la pantalla.
        Args:
            char_code (int): El código ASCII del caracter a escribir.
        """
        # Manejar la tecla de retroceso
        if char_code == 8:
            if len(self._buffer) > 0:
                self._buffer = self._buffer[:-1]
            return

        # Convierte el código ASCII a un caracter y lo añade al buffer
        self._buffer += chr(char_code)

        # Trunca las líneas más antiguas si se supera el máximo
        lines = self._buffer.split('\n')
        if len(lines) > self.max_lines:
            self._buffer = "\n".join(lines[-self.max_lines:])


    def get_buffer(self) -> str:
        """
        Devuelve el contenido actual del buffer.
        Returns:
            str: El contenido de la pantalla.
        """
        return self._buffer

    def write_value(self, value: int):
        """Añade la representación de un número al buffer."""
        self._buffer += str(value)

    def reset(self):
        """Limpia el buffer de la pantalla."""
        self._buffer = ""
