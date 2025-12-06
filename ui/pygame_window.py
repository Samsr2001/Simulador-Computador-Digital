import pygame
from utils.enums import Pantallas, Colors
from utils.constants import CLOCK_SPEED
from ui.panels.cpu_panel import CPUPanel
from ui.panels.memory_panel import MemoryPanel
from ui.panels.screen_panel import ScreenPanel
from ui.panels.control_panel import ControlPanel

class PygameWindow:
    """La ventana principal de la aplicación que contiene todos los paneles."""

    def __init__(self, cpu, memory, io_manager, program_loader):
        """
        Inicializa la ventana de Pygame.
        Args:
            cpu (CPU): La instancia de la CPU.
            memory (Memory): La instancia de la memoria.
            io_manager (IOManager): El gestor de E/S.
            program_loader (ProgramLoader): El cargador de programas.
        """
        pygame.init()
        pygame.display.set_caption("Simulador de Computador Digital")

        self.screen_size = Pantallas.BIG.value
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.is_running = True

        # Crear paneles
        self.cpu_panel = CPUPanel(20, 20, 250, 200, cpu)
        self.control_panel = ControlPanel(20, 240, 250, 340, cpu, program_loader)
        
        # Paneles de la derecha
        mem_panel_width = 714
        mem_panel_height = 540 # Altura ajustada
        self.memory_panel = MemoryPanel(290, 20, mem_panel_width, mem_panel_height, memory)
        
        screen_panel_y = self.memory_panel.rect.bottom + 20
        screen_panel_height = self.screen_size[1] - screen_panel_y - 20
        self.screen_panel = ScreenPanel(290, screen_panel_y, mem_panel_width, screen_panel_height, io_manager)


    def main_loop(self):
        """El bucle principal de la aplicación."""
        while self.is_running:
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                self.control_panel.handle_event(event)

            # Lógica del simulador
            self.cpu_panel.cpu.run_cycle()

            # Renderizado
            self.screen.fill(Colors.BLACK.value)
            self.draw_panels()
            pygame.display.flip()

            # Control de velocidad
            self.clock.tick(CLOCK_SPEED)

        pygame.quit()

    def draw_panels(self):
        """Dibuja todos los paneles en la pantalla."""
        self.cpu_panel.draw(self.screen)
        self.memory_panel.draw(self.screen)
        self.screen_panel.draw(self.screen)
        self.control_panel.draw(self.screen)
