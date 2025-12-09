import pygame
from utils.enums import Colors

class Button:
    """Clase simple para un botón clickeable."""
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, 28)
        self.font.set_bold(True)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, Colors.WHITE.value, self.rect, 2)
        
        text_surf = self.font.render(self.text, True, Colors.WHITE.value)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class ControlPanel:
    """Panel con los botones de control de la simulación."""

    def __init__(self, x, y, width, height, cpu, program_loader, calculator_program=None):
        """
        Inicializa el panel de control.
        Args:
            x (int): Posición X.
            y (int): Posición Y.
            width (int): Ancho.
            height (int): Alto.
            cpu (CPU): La instancia de la CPU.
            program_loader (ProgramLoader): El cargador de programas.
            calculator_program (list, optional): El programa de calculadora pre-cargado.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.cpu = cpu
        self.program_loader = program_loader
        self.calculator_program = calculator_program
        self.title_font = pygame.font.Font(None, 28)
        self.title_font.set_bold(True)
        
        self.buttons = []
        self._create_buttons()

    def _create_buttons(self):
        """Crea los botones del panel."""
        btn_width, btn_height = 120, 40
        margin = 20
        
        # Botón de Run/Stop
        self.btn_run = Button(
            self.rect.centerx - btn_width / 2,
            self.rect.y + 60,
            btn_width, btn_height,
            "Run", (0, 150, 0)
        )
        self.buttons.append(self.btn_run)

        # Botón de Step
        self.btn_step = Button(
            self.rect.centerx - btn_width/2,
            self.btn_run.rect.bottom + margin,
            btn_width, btn_height,
            "Step", (200, 100, 0)
        )
        self.buttons.append(self.btn_step)

        # Botón de Reset
        self.btn_reset = Button(
            self.rect.centerx - btn_width / 2,
            self.btn_step.rect.bottom + margin,
            btn_width, btn_height,
            "Reset", (180, 0, 0)
        )
        self.buttons.append(self.btn_reset)
        
    def handle_event(self, event):
        """
        Maneja los eventos de click en los botones.
        Args:
            event (pygame.event.Event): El evento a procesar.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.btn_run.is_clicked(event.pos):
                if self.cpu.running:
                    self.cpu.stop()
                else:
                    self.cpu.run()
            elif self.btn_step.is_clicked(event.pos):
                self.cpu.stop()
                self.cpu.step()
            elif self.btn_reset.is_clicked(event.pos):
                self.cpu.reset()
                # Carga el programa incorporado si existe, si no, usa el método anterior
                if self.calculator_program:
                    self.program_loader.load_from_list(self.calculator_program)
                else:
                    self.program_loader.load_into_memory()


    def update(self):
        """Actualiza el texto del botón Run/Stop."""
        if self.cpu.running:
            self.btn_run.text = "Stop"
            self.btn_run.color = (200, 50, 0)
        else:
            self.btn_run.text = "Run"
            self.btn_run.color = (0, 150, 0)


    def draw(self, surface):
        """
        Dibuja el panel de control.
        Args:
            surface (pygame.Surface): La superficie donde dibujar.
        """
        pygame.draw.rect(surface, Colors.GRAY.value, self.rect, 2)

        title_surf = self.title_font.render("Control", True, Colors.WHITE.value)
        title_rect = title_surf.get_rect(center=(self.rect.centerx, self.rect.top + 20))
        surface.blit(title_surf, title_rect)

        self.update()
        for button in self.buttons:
            button.draw(surface)

