import pygame
from utils.enums import Colors
from utils.constants import MEMORY_SIZE, CELL_MARGIN
from core.memory_cell import MemoryCell

class MemoryPanel:
    """Panel que visualiza la memoria RAM."""

    def __init__(self, x, y, width, height, memory):
        """
        Inicializa el panel de memoria.
        Args:
            x (int): Posición X.
            y (int): Posición Y.
            width (int): Ancho.
            height (int): Alto.
            memory (Memory): La instancia de la memoria.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.memory = memory
        self.font = pygame.font.Font(None, 20)  # Aumentar tamaño de fuente
        self.title_font = pygame.font.Font(None, 28)
        self.title_font.set_bold(True)

        self.cells = []
        self._create_cells()

    def _create_cells(self):
        """Crea las celdas visuales para la memoria, calculando su tamaño dinámicamente."""
        cols = 16
        rows = MEMORY_SIZE // cols

        # Calcular dimensiones disponibles para la grilla
        available_width = self.rect.width - (2 * 10) # Margen de 10px a cada lado
        available_height = self.rect.height - 60 # Espacio para el título y margen

        # Calcular tamaño total por celda (incluyendo margen)
        cell_total_width = available_width / cols
        cell_total_height = available_height / rows
        
        # Calcular tamaño neto de la celda (descontando margen)
        cell_width = cell_total_width - CELL_MARGIN
        cell_height = cell_total_height - CELL_MARGIN

        start_x = self.rect.x + 10
        start_y = self.rect.y + 50

        for i in range(MEMORY_SIZE):
            row = i // cols
            col = i % cols
            # Calcular la posición de la celda
            x = start_x + col * cell_total_width
            y = start_y + row * cell_total_height
            
            self.cells.append(MemoryCell(x, y, cell_width, cell_height, i))

    def update_cells(self):
        """Actualiza los valores de las celdas y el resaltado."""
        all_values = self.memory.get_all_values()
        last_accessed = self.memory.last_accessed_address

        for i, cell in enumerate(self.cells):
            cell.value = all_values[i]
            cell.highlighted = (i == last_accessed)

    def draw(self, surface):
        """
        Dibuja el panel de memoria.
        Args:
            surface (pygame.Surface): La superficie donde dibujar.
        """
        pygame.draw.rect(surface, Colors.GRAY.value, self.rect, 2)
        
        title_surf = self.title_font.render("RAM", True, Colors.WHITE.value)
        title_rect = title_surf.get_rect(center=(self.rect.centerx, self.rect.top + 20))
        surface.blit(title_surf, title_rect)

        self.update_cells()
        for cell in self.cells:
            cell.draw(surface, self.font)
