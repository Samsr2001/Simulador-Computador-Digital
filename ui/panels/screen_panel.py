import pygame
from utils.enums import Colors

class ScreenPanel:
    """Panel que simula la pantalla de salida (teletipo)."""

    def __init__(self, x, y, width, height, io_manager):
        """
        Inicializa el panel de la pantalla.
        Args:
            x (int): Posición X.
            y (int): Posición Y.
            width (int): Ancho.
            height (int): Alto.
            io_manager (IOManager): El gestor de E/S.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.io_manager = io_manager
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.title_font = pygame.font.Font(None, 28)
        self.title_font.set_bold(True)
    def draw(self, surface):
        """
        Dibuja el panel de la pantalla.
        Args:
            surface (pygame.Surface): La superficie donde dibujar.
        """
        pygame.draw.rect(surface, Colors.GRAY.value, self.rect, 2)
        
        title_surf = self.title_font.render("Output", True, Colors.WHITE.value)
        title_rect = title_surf.get_rect(center=(self.rect.centerx, self.rect.top + 20))
        surface.blit(title_surf, title_rect)

        # Muestra el buffer de la pantalla
        buffer_text = self.io_manager.screen.get_buffer()
        lines = buffer_text.split('\\n')
        
        y_offset = 50
        for line in lines:
            text_surf = self.font.render(line, True, Colors.GREEN.value)
            surface.blit(text_surf, (self.rect.x + 15, self.rect.y + y_offset))
            y_offset += 25
