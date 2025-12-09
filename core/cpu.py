from core.alu import ALU
# from core.control_unit import ControlUnit <- Moved to __init__
from core.memory import Memory
from iod.io_manager import IOManager

class CPU:
    """Unidad Central de Procesamiento (CPU)."""

    def __init__(self, memory: Memory, io_manager: IOManager):
        """
        Inicializa la CPU.
        Args:
            memory (Memory): El sistema de memoria.
            io_manager (IOManager): El gestor de entrada/salida.
        """
        from core.control_unit import ControlUnit  # Importación local para evitar ciclo
        
        self.memory = memory
        self.io_manager = io_manager

        # Componentes internos
        self.alu = ALU()
        self.control_unit = ControlUnit(self.memory)

        # Registros
        self.pc = 0  # Program Counter
        self.ir = 0  # Instruction Register
        self.ac = 0  # Accumulator
        self.flag_z = 0  # Zero Flag

        # Estado
        self.halted = False
        self.running = False
        self.waiting_for_input = False
        self.input_buffer = ""

    def step(self):
        """Ejecuta un único ciclo de instrucción o maneja el estado de espera."""
        if self.halted:
            return

        # Si estamos esperando una entrada de teclado
        if self.waiting_for_input:
            key = self.io_manager.pop_key()
            if key is not None:
                # Tecla Enter: finalizar la entrada
                if key == 10:
                    try:
                        self.ac = int(self.input_buffer)
                    except (ValueError, TypeError):
                        self.ac = 0
                    self.input_buffer = ""
                    self.waiting_for_input = False
                    self.io_manager.write_char(10)  # Eco de nueva línea
                    self.pc += 1
                # Tecla Retroceso: borrar último dígito
                elif key == 8:
                    if len(self.input_buffer) > 0:
                        self.input_buffer = self.input_buffer[:-1]
                        self.io_manager.write_char(8) # Eco de retroceso
                # Tecla de dígito: añadir al buffer
                elif chr(key).isdigit():
                    self.input_buffer += chr(key)
                    self.io_manager.write_char(key)

            return  # Permanecer en estado de espera

        # --- Ciclo normal Fetch-Decode-Execute ---
        
        # 1. Fetch
        self.ir = self.control_unit.fetch(self.pc)

        # 2. Decode
        instruction = self.control_unit.decode(self.ir)
        
        # 3. Execute
        # La Unidad de Control es ahora responsable de modificar el PC
        self.control_unit.execute(self)

    def run_cycle(self):
        """Wrapper para ejecutar un ciclo si la CPU está en modo 'running'."""
        if self.running and not self.halted:
            self.step()

    def run(self):
        """Inicia la ejecución continua."""
        self.running = True

    def stop(self):
        """Detiene la ejecución continua."""
        self.running = False
        
    def reset(self):
        """Reinicia la CPU y la memoria a su estado inicial."""
        self.pc = 0
        self.ir = 0
        self.ac = 0
        self.flag_z = 0
        self.halted = False
        self.running = False
        self.waiting_for_input = False
        self.input_buffer = ""
        self.memory.reset()
        self.io_manager.reset()
