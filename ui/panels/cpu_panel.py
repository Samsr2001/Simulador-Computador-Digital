import pygame
from utils.enums import Colors
from utils.helpers import to_hex

class CPUPanel:
    """Panel que muestra el estado de los registros de la CPU."""

    def __init__(self, x, y, width, height, cpu):
        """
        Inicializa el panel de la CPU.
        Args:
            x (int): Posición X.
            y (int): Posición Y.
            width (int): Ancho.
            height (int): Alto.
            cpu (CPU): La instancia de la CPU a monitorear.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.cpu = cpu
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 28)
        self.title_font.set_bold(True)


    def draw(self, surface):
        """
        Dibuja el panel en la superficie.
        Args:
            surface (pygame.Surface): La superficie donde dibujar.
        """
        # Dibuja el borde y el título del panel
        pygame.draw.rect(surface, Colors.GRAY.value, self.rect, 2)
        
        title_surf = self.title_font.render("CPU Registers", True, Colors.WHITE.value)
        title_rect = title_surf.get_rect(center=(self.rect.centerx, self.rect.top + 20))
        surface.blit(title_surf, title_rect)

        # Prepara y dibuja la información de los registros
        y_offset = 60
        registers = {
            "PC": f"0x{to_hex(self.cpu.pc, 12)}",
            "IR": f"0x{to_hex(self.cpu.ir, 16)}",
            "AC": f"0x{to_hex(self.cpu.ac, 16)}",
            "Z Flag": str(self.cpu.flag_z)
        }

        for name, value in registers.items():
            text = f"{name}: {value}"
            text_surf = self.font.render(text, True, Colors.WHITE.value)
            text_rect = text_surf.get_rect(topleft=(self.rect.x + 20, self.rect.y + y_offset))
            surface.blit(text_surf, text_rect)
            y_offset += 30
