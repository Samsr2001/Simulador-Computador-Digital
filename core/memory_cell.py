import pygame
from utils.enums import Colors

class MemoryCell:
    """Representa una celda de memoria individual en la RAM."""

    def __init__(self, x, y, width, height, address):
        """
        Inicializa una celda de memoria.
        Args:
            x (int): Posición X en la pantalla.
            y (int): Posición Y en la pantalla.
            width (int): Ancho de la celda.
            height (int): Alto de la celda.
            address (int): Dirección de memoria.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.address = address
        self.value = 0
        self.highlighted = False

    def draw(self, surface, font):
        """
        Dibuja la celda de memoria en la superficie.
        Args:
            surface (pygame.Surface): Superficie donde dibujar.
            font (pygame.font.Font): Fuente para el texto.
        """
        # Dibuja el borde resaltado si está seleccionada
        if self.highlighted:
            pygame.draw.rect(surface, Colors.RED.value, self.rect, 2)
        else:
            pygame.draw.rect(surface, Colors.GRAY.value, self.rect, 1)

        # Muestra el valor en hexadecimal
        text_surf = font.render(f'{self.value:04X}', True, Colors.WHITE.value)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
