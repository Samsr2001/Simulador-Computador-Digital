from typing import List
from utils.constants import MEMORY_SIZE
from core.memory_cell import MemoryCell

class Memory:
    """Representa la memoria RAM del computador."""

    def __init__(self):
        """Inicializa la memoria con celdas vacías."""
        self._cells: List[int] = [0] * MEMORY_SIZE
        self.last_accessed_address: int = -1

    def read(self, address: int) -> int:
        """
        Lee un valor de una dirección de memoria.
        Args:
            address (int): La dirección de la que leer.
        Returns:
            int: El valor almacenado en esa dirección.
        """
        if 0 <= address < MEMORY_SIZE:
            self.last_accessed_address = address
            return self._cells[address]
        # Manejar error de acceso a memoria fuera de rango si es necesario
        return 0

    def write(self, address: int, value: int):
        """
        Escribe un valor en una dirección de memoria.
        Args:
            address (int): La dirección en la que escribir.
            value (int): El valor a escribir.
        """
        if 0 <= address < MEMORY_SIZE:
            self.last_accessed_address = address
            # Asegurarse que el valor está en el rango de 16 bits
            self._cells[address] = value & 0xFFFF

    def get_all_values(self) -> List[int]:
        """Devuelve todos los valores de la memoria."""
        return self._cells

    def reset(self):
        """Reinicia todos los valores de la memoria a cero."""
        self._cells = [0] * MEMORY_SIZE
        self.last_accessed_address = -1
